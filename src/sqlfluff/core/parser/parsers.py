"""Individual segment parsers.

Matchable objects which return individual segments.
"""

from abc import abstractmethod
import regex
from typing import Collection, Type, Optional, List, Tuple, Union

from sqlfluff.core.parser.context import ParseContext
from sqlfluff.core.parser.matchable import Matchable
from sqlfluff.core.parser.match_result import MatchResult
from sqlfluff.core.parser.segments import RawSegment, BaseSegment


class BaseParser(Matchable):
    """An abstract class from which other Parsers should inherit."""

    # Meta segments are handled seperately. All Parser elements
    # are assumed to be not meta.
    is_meta: bool = False

    @abstractmethod
    def __init__(
        self,
        raw_class: Type[RawSegment],
        name: Optional[str] = None,
        type: Optional[str] = None,
        optional: bool = False,
        **segment_kwargs,
    ) -> None:
        self.raw_class = raw_class
        self.name = name
        self.type = type
        self.optional = optional
        self.segment_kwargs = segment_kwargs or {}

    def is_optional(self) -> bool:
        """Return whether this element is optional."""
        return self.optional

    @abstractmethod
    def _is_first_match(self, segment: BaseSegment):
        """Does the segment provided match according to the current rules."""

    def _make_match_from_first_result(self, segments: Tuple[BaseSegment, ...]):
        """Make a MatchResult from the first segment in the given list.

        This is a helper function for reuse by other parsers.
        """
        # Construct the segment object
        new_seg = self.raw_class(
            raw=segments[0].raw,
            pos_marker=segments[0].pos_marker,
            type=self.type,
            name=self.name,
            **self.segment_kwargs,
        )
        # Return as a tuple
        return MatchResult((new_seg,), segments[1:])

    def match(
        self,
        segments: Union[BaseSegment, Tuple[BaseSegment, ...]],
        parse_context: "ParseContext",
    ) -> MatchResult:
        """Compare input segments for a match, return a `MatchResult`.

        Note: For matching here, we only consider the *first* element,
        because we assume that a keyword can only span one raw segment.
        """
        # If we've been passed the singular, make it a tuple
        if isinstance(segments, BaseSegment):
            segments = (segments,)

        # We're only going to match against the first element
        if len(segments) >= 1:
            # Is the first one already of this type?
            if (
                isinstance(segments[0], self.raw_class)
                and segments[0].name == self.name
                and segments[0].is_type(self.type)
            ):
                return MatchResult((segments[0],), segments[1:])
            # Does it match?
            elif self._is_first_match(segments[0]):
                return self._make_match_from_first_result(segments)
        return MatchResult.from_unmatched(segments)


class StringParser(BaseParser):
    """An object which matches and returns raw segments based on strings."""

    def __init__(
        self,
        template: str,
        raw_class: Type[RawSegment],
        name: Optional[str] = None,
        type: Optional[str] = None,
        optional: bool = False,
        **segment_kwargs,
    ):
        self.template = template.upper()
        # Create list version upfront to avoid recreating it multiple times.
        self._simple = [self.template]
        super().__init__(
            raw_class=raw_class,
            name=name,
            type=type,
            optional=optional,
            **segment_kwargs,
        )

    def simple(self, parse_context: "ParseContext", crumbs=None) -> Optional[List[str]]:
        """Return simple options for this matcher.

        Because string matchers are not case sensitive we can
        just return the template here.
        """
        return self._simple

    def _is_first_match(self, segment: BaseSegment):
        """Does the segment provided match according to the current rules."""
        # Is the target a match and IS IT CODE.
        # The latter stops us accidentally matching comments.
        return bool(self.template == segment.raw_upper and segment.is_code)


class MultiStringParser(BaseParser):
    """An object which matches and returns raw segments on a collection of strings."""

    def __init__(
        self,
        templates: Collection[str],
        raw_class: Type[RawSegment],
        name: Optional[str] = None,
        type: Optional[str] = None,
        optional: bool = False,
        **segment_kwargs,
    ):
        self.templates = {template.upper() for template in templates}
        # Create list version upfront to avoid recreating it multiple times.
        self._simple = list(self.templates)
        super().__init__(
            raw_class=raw_class,
            name=name,
            type=type,
            optional=optional,
            **segment_kwargs,
        )

    def simple(self, parse_context: "ParseContext", crumbs=None) -> Optional[List[str]]:
        """Return simple options for this matcher.

        Because string matchers are not case sensitive we can
        just return the templates here.
        """
        return self._simple

    def _is_first_match(self, segment: BaseSegment):
        """Does the segment provided match according to the current rules."""
        # Is the target a match and IS IT CODE.
        # The latter stops us accidentally matching comments.
        return bool(segment.is_code and segment.raw_upper in self.templates)


class NamedParser(BaseParser):
    """An object which matches and returns raw segments based on names."""

    def __init__(
        self,
        template: str,
        raw_class: Type[RawSegment],
        name: Optional[str] = None,
        type: Optional[str] = None,
        optional: bool = False,
        **segment_kwargs,
    ):
        self.template = template.lower()
        super().__init__(
            raw_class=raw_class,
            name=name,
            type=type,
            optional=optional,
            **segment_kwargs,
        )

    def simple(self, parse_context: ParseContext, crumbs=None) -> Optional[List[str]]:
        """Does this matcher support a uppercase hash matching route?

        NamedParser segment does NOT for now. We might need to later for efficiency.

        There is a way that this *could* be enabled, by allowing *another*
        shortcut route, to look ahead at the names of upcoming segments,
        rather than their content.
        """
        return None

    def _is_first_match(self, segment: BaseSegment):
        """Does the segment provided match according to the current rules.

        NamedParser implements its own matching function where
        we assume that ._template is the `name` of a segment.
        """
        # Case sensitivity is not supported. Names are all
        # lowercase by convention.
        return self.template == segment.name.lower()


class RegexParser(BaseParser):
    """An object which matches and returns raw segments based on a regex."""

    def __init__(
        self,
        template: str,
        raw_class: Type[RawSegment],
        name: Optional[str] = None,
        type: Optional[str] = None,
        optional: bool = False,
        anti_template: Optional[str] = None,
        **segment_kwargs,
    ):
        # Store the optional anti-template
        self.template = template
        self.anti_template = anti_template
        # Compile regexes upfront to avoid repeated overhead
        self._anti_template = regex.compile(anti_template or r"", regex.IGNORECASE)
        self._template = regex.compile(template, regex.IGNORECASE)
        super().__init__(
            raw_class=raw_class,
            name=name,
            type=type,
            optional=optional,
            **segment_kwargs,
        )

    def simple(self, parse_context: ParseContext, crumbs=None) -> Optional[List[str]]:
        """Does this matcher support a uppercase hash matching route?

        Regex segment does NOT for now. We might need to later for efficiency.
        """
        return None

    def _is_first_match(self, segment: BaseSegment):
        """Does the segment provided match according to the current rules.

        RegexParser implements its own matching function where
        we assume that ._template is a r"" string, and is formatted
        for use directly as a regex. This only matches on a single segment.
        """
        if len(segment.raw) == 0:  # pragma: no cover TODO?
            # If it's of zero length it's probably a meta segment.
            # In any case, it won't match here.
            return False
        if result := self._template.match(segment.raw_upper):
            result_string = result.group(0)
            # Check that we've fully matched
            if result_string == segment.raw_upper:
                # Check that the anti_template (if set) hasn't also matched
                return not self.anti_template or not self._anti_template.match(
                    segment.raw_upper
                )

        return False

"""A list of all Materialize SQL key words.

https://materialize.com/docs/sql/identifiers
"""

materialize_reserved_keywords = """ALL
ALTER
AND
ANY
AS
BY
CAST
CHECK
CLUSTER
CLUSTERS
CONNECTION
CONNECTIONS
CONSTRAINT
CREATE
CROSS
CURRENT
DELETE
DISTINCT
DROP
ELSE
EXISTS
FOLLOWING
FOR
FROM
FULL
GROUP
ILIKE
IN
INNER
INSERT
INTERSECT
INTO
IS
JOIN
LATERAL
LEFT
LIKE
NATURAL
NOT
NULL
NULLIF
OF
ON
OR
ORDER
RETURNING
ROW
ROWS
SELECT
SET
SINK
SINKS
TO
UNION
UNIQUE
UPDATE
USING
VALUES
WHEN
WHERE
WITH
"""

materialize_unreserved_keywords = """ACCESS
ACKS
ARN
ARRANGEMENT
ARRAY
ASC
AT
AUCTION
AUTHORITY
AVAILABILITY
AVRO
AWS
BEGIN
BETWEEN
BIGINT
BODY
BOOLEAN
BOTH
BPCHAR
BROKER
BROKERS
BUCKET
BYTES
CASCADE
CASE
CERTIFICATE
CHAIN
CHAR
CHARACTER
CHARACTERISTICS
CLIENT
CLOSE
COALESCE
COLLATE
COLUMNS
COMMIT
COMMITTED
COMPACTION
COMPRESSION
COMPUTE
CONFLUENT
COPY
COUNT
COUNTER
CREATEROLE
CREATEDB
CREATECLUSTER
CSV
CURSOR
DATABASE
DATABASES
DATUMS
DAY
DAYS
DEALLOCATE
DEBEZIUM
DEBUG
DEBUGGING
DEC
DECIMAL
DECLARE
DECORRELATED
DEFAULT
DELIMITED
DELIMITER
DESC
DETAILS
DISCARD
DISCOVER
DOT
DOUBLE
EFFORT
ELEMENT
ENABLE
ENABLED
END
ENDPOINT
ENFORCED
ENVELOPE
ESCAPE
EXCEPT
EXECUTE
EXPECTED
EXPLAIN
EXTRACT
FACTOR
FALSE
FETCH
FIELDS
FILTER
FIRST
FLOAT
FOREIGN
FORMAT
FORWARD
FULLNAME
GENERATOR
GRAPH
GREATEST
GROUPS
GZIP
HAVING
HEADER
HEADERS
HOLD
HOST
HOUR
HOURS
ID
IDEMPOTENCE
IDLE
IF
IGNORE
INCLUDE
INDEX
INDEXES
INFO
INHERIT
INLINE
INT
INTEGER
INTERSECT
INTERVAL
INTROSPECTION
ISNULL
ISOLATION
JSON
KAFKA
KEY
KEYS
KINESIS
LAST
LATEST
LEADING
LEAST
LEVEL
LIMIT
LIST
LOAD
LOCAL
LOG
LOGICAL
LOGIN
MANAGED
MAP
MARKETING
MATCHING
MATERIALIZE
MATERIALIZED
MAX
MECHANISMS
MESSAGE
METADATA
MINUTE
MINUTES
MODE
MONTH
MONTHS
MS
NAME
NAMES
NEXT
NO
NOLOGIN
NONE
NOSUPERUSER
NOTICE
NOTIFICATIONS
NULLS
OBJECTS
OFFSET
ONLY
OPERATOR
OPTIMIZED
OPTIMIZER
OPTIONS
ORDINALITY
OUTER
OVER
OWNER
PARTITION
PASSWORD
PHYSICAL
PLAN
PLANS
PORT
POSITION
POSTGRES
PRECEDING
PRECISION
PREFIX
PREPARE
PRIMARY
PRIVATELINK
PROGRESS
PROTOBUF
PUBLICATION
QUERY
QUOTE
RAISE
RANGE
RAW
READ
REAL
REFERENCES
REFRESH
REGEX
REGION
REGISTRY
REMOTE
RENAME
REPEATABLE
REPLACE
REPLICA
REPLICAS
REPLICATION
RESET
RESTRICT
RETENTION
RIGHT
ROLE
ROLES
ROLLBACK
ROTATE
S3
SASL
SCALE
SCAN
SCHEMA
SCHEMAS
SCRIPT
SECOND
SECONDS
SECRET
SECRETS
SEED
SEQUENCES
SERIALIZABLE
SERVICE
SESSION
SHOW
SIZE
SMALLINT
SNAPSHOT
SOME
SOURCE
SOURCES
SQS
SSH
SSL
START
STDIN
STDOUT
STRATEGY
STRING
SUBSCRIBE
SUBSOURCE
SUBSTRING
SUPERUSER
SYSTEM
TABLE
TABLES
TAIL
TEMP
TEMPORARY
TEST
TEXT
THEN
TICK
TIES
TIME
TIMELINE
TIMEOUT
TIMESTAMP
TOKEN
TOPIC
TPCH
TRACE
TRAILING
TRANSACTION
TRIM
TRUE
TUNNEL
TYPE
TYPES
UNBOUNDED
UNCOMMITTED
UNKNOWN
UPSERT
URL
USER
USERNAME
USERS
VALUE
VARCHAR
VARYING
VIEW
VIEWS
WARNING
WEBHOOK
WINDOW
WIRE
WITHOUT
WORK
WORKERS
WRITE
YEAR
YEARS
ZONE
ZONES
"""

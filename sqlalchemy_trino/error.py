from trino.exceptions import (  # noqa
    TrinoQueryError
)

# ref: https://github.com/trinodb/trino/blob/master/core/trino-spi/src/main/java/io/trino/spi/StandardErrorCode.java
TABLE_NOT_FOUND = 'TABLE_NOT_FOUND'
SCHEMA_NOT_FOUND = 'SCHEMA_NOT_FOUND'
CATALOG_NOT_FOUND = 'CATALOG_NOT_FOUND'

MISSING_TABLE = 'MISSING_TABLE'
MISSING_COLUMN_NAME = 'MISSING_COLUMN_NAME'
MISSING_SCHEMA_NAME = 'MISSING_SCHEMA_NAME'
MISSING_CATALOG_NAME = 'MISSING_CATALOG_NAME'

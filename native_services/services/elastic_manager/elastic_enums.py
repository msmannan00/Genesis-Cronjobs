class ELASTIC_CRUD_COMMANDS:
    S_CREATE = 1
    S_READ = 2
    S_UPDATE = 3
    S_DELETE = 4

class ELASTIC_INDEX:
    S_WEB_INDEX = "parsed_index"

class ELASTIC_CONNECTIONS:
    S_DATABASE_NAME = 'genesis-elastic_manager-search'
    S_DATABASE_PORT = 9200
    S_DATABASE_IP = 'http://localhost'

class ELASTIC_KEYS:
    S_DOCUMENT = 'm_document'
    S_FILTER = 'm_filter'
    S_VALUE = 'm_value'

class ELASTIC_REQUEST_COMMANDS:
    S_BACKUP = 1
    S_DEL_CLEAN = 2
    S_CLEAN_MONTHLY_SCORE = 3
    S_CLEAN_DAILY_SCORE = 4

class MANAGE_ELASTIC_MESSAGES:
    S_INSERT_FAILURE = "[1] Something unexpected happened while inserting"
    S_INSERT_SUCCESS = "[2] Document Created Successfully"
    S_UPDATE_FAILURE = "[3] Something unexpected happened while updating"
    S_UPDATE_SUCCESS = "[4] Data Updated Successfully"
    S_DELETE_FAILURE = "[5] Something unexpected happened while deleting"
    S_DELETE_SUCCESS = "[6] Data Deleted Successfully"
    S_READ_FAILURE = "[5] Something unexpected happened while reading"
    S_READ_SUCCESS = "[6] Data Read Successfully"
    S_COUNT_FAILURE = "[1] Something unexpected happened while counting"

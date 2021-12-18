import enum

class MONGODB_COMMANDS(enum.Enum):
    S_RESET_DICTIONARY = 1
    S_INIT_DICTIONARY = 2
    S_COUNT_DICTIONARY = 3
    S_CREATE_BACKUP = 4
    S_CREATE_STATUS = 5
    S_UPDATE_BACKUP_STATUS = 6
    S_UPDATE_DICTIONARY_STATUS = 7
    S_CLEAN_DICTIONARY = 7

class MONGODB_COLLECTIONS:
    S_INDEX_MODEL = 'index_model'
    S_BACKUP_MODEL = 'backup_model'
    S_UNIQUE_HOST_MODEL = 'unique_host'
    S_TFIDF_MODEL = 'tfidf_model'
    S_DICTIONARY_MODEL = 'dictionary_model'
    S_CRAWLABLE_URL_MODEL = 'crawlable_url_model'
    S_APP_STATUS_MODEL = 'status_model'

class MONGO_CRUD(enum.Enum):
    S_CREATE = '1'
    S_READ = '2'
    S_UPDATE = '3'
    S_DELETE = '4'
    S_COUNT = '5'

class MONGODB_KEYS:
    S_DOCUMENT = 'm_document'
    S_FILTER = 'm_filter'
    S_VALUE = 'm_value'

class MANAGE_USER_MESSAGES:
    S_INSERT_FAILURE = "[1] Something unexpected happened while inserting"
    S_INSERT_SUCCESS = "[2] Document Created Successfully"
    S_UPDATE_FAILURE = "[3] Something unexpected happened while updating"
    S_UPDATE_SUCCESS = "[4] Data Updated Successfully"
    S_DELETE_FAILURE = "[5] Something unexpected happened while deleting"
    S_DELETE_SUCCESS = "[6] Data Deleted Successfully"
    S_READ_FAILURE = "[5] Something unexpected happened while reading"
    S_READ_SUCCESS = "[6] Data Read Successfully"
    S_COUNT_FAILURE = "[1] Something unexpected happened while counting"

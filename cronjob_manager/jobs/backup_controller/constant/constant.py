import os

class PATHS:
    S_PROJECT_PATH = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    S_BACKUP_PATH = S_PROJECT_PATH + "\\Genesis-Cronjobs\\cronjob_manager\\jobs\\backup_controller\\raw\\backup\\"
    S_EXTENDED_BACKUP_PATH = "D:\\Mongo-Backup\\"

class MONGO:
    S_COLLECTION = ['index_model', 'backup_model', 'unique_host', 'tfidf_model', 'dictionary_model', 'crawlable_url_model']

class SETTINGS:
    S_MAX_BACKUP_COUNT = 5
    S_EXTENDED_MAX_BACKUP_COUNT = 30
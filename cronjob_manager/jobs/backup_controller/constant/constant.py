import os

class PATHS:
    S_PROJECT_PATH = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    S_MONGO_BACKUP_PATH = S_PROJECT_PATH + "/Genesis-Cronjobs/cronjob_manager/jobs/backup_controller/raw/mongo_backup/"
    S_ELASTIC_BACKUP_PATH = S_PROJECT_PATH + "/Genesis-Cronjobs/cronjob_manager/jobs/backup_controller/raw/elastic_backup/"

class MONGO:
    S_COLLECTION = ['reported_websites', 'submitted_websites']

class SETTINGS:
    S_MAX_BACKUP_COUNT = 2
    S_EXTENDED_MAX_BACKUP_COUNT = 20
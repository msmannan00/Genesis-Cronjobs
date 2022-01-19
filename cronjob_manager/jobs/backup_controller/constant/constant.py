import os
from pathlib import Path

class PATHS:
    S_PROJECT_PATH = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    S_MONGO_BACKUP_PATH = S_PROJECT_PATH + "/Genesis-Cronjobs/cronjob_manager/jobs/backup_controller/raw/mongo_backup/"
    S_ELASTIC_BACKUP_PATH = S_PROJECT_PATH + "/Genesis-Cronjobs/cronjob_manager/jobs/backup_controller/raw/elastic_backup/"
    S_MONGO_EXTENDED_BACKUP_PATH = str(Path(__file__).parent.parent.parent.parent.parent.parent)+"/ftp-directory/mongo/"
    S_ELASTIC_EXTENDED_BACKUP_PATH = str(Path(__file__).parent.parent.parent.parent.parent.parent)+"/ftp-directory/elastic/"

class MONGO:
    S_COLLECTION = ['reported_websites', 'submitted_websites']

class SETTINGS:
    S_MAX_BACKUP_COUNT = 3
    S_EXTENDED_MAX_BACKUP_COUNT = 10
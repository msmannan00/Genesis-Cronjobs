import os
import shutil
from datetime import datetime
from bson import json_util
from cronjob_manager.jobs.backup_controller.backup_manager.backup_enums import BACKUP_MODEL_COMMANDS
from cronjob_manager.jobs.backup_controller.constant.constant import MONGO, PATHS, SETTINGS
from cronjob_manager.jobs.backup_controller.constant.strings import MESSAGES
from cronjob_manager.shared_model.request_handler import request_handler
from log_manager.log_controller import log
from native_services.services.mongo_manager.mongo_controller import mongo_controller
from native_services.services.mongo_manager.mongo_enums import MONGO_CRUD, MONGODB_COMMANDS


class backup_model(request_handler):
    __instance = None

    # Initializations
    def __init__(self):
        pass

    def __count_backup(self, p_path):
        APP_FOLDER = p_path
        totalDir = 0

        for base, dirs, files in os.walk(APP_FOLDER):
            for _ in dirs:
                totalDir += 1
        return totalDir

    def __remove_oldest_directory(self,p_path):
        list_of_files = os.listdir(p_path)
        full_path = [p_path+"{0}".format(x) for x in list_of_files]

        oldest_file = min(full_path, key=os.path.getctime)
        shutil.rmtree(oldest_file)

        log.g().i(MESSAGES.S_CLEAN_BACKUP)

    def __create_backup(self, p_path, p_root_path, p_max_backup_count):
        mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_UPDATE, [MONGODB_COMMANDS.S_UPDATE_BACKUP_STATUS, [True], [False]])

        if os.path.isdir(p_path) is False:

            while self.__count_backup(p_root_path) >= p_max_backup_count:
                self.__remove_oldest_directory(p_root_path)

            log.g().i(MESSAGES.S_MAKING_DIRECTORY)
            os.makedirs(p_path)

            for m_collection in MONGO.S_COLLECTION:
                log.g().i(MESSAGES.S_CREATING_BACKUP + " : " + m_collection)
                m_result = mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_READ,[MONGODB_COMMANDS.S_CREATE_BACKUP, [m_collection],[None]])

                with open(p_path + "//" + m_collection + '.json', 'w') as file:
                    file.write('[')
                    for document in m_result:
                        file.write(json_util.dumps(document))
                        file.write(',')
                    file.write(']')
            log.g().s(MESSAGES.S_BACKUP_CREATED)
        else:
            log.g().w(MESSAGES.S_BACKUP_ALREADY_CREATED)
        mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_UPDATE, [MONGODB_COMMANDS.S_UPDATE_BACKUP_STATUS, [False], [False]])

    def __init_backup(self):
        if os.path.isdir(PATHS.S_EXTENDED_BACKUP_PATH) is False:
            os.mkdir(PATHS.S_EXTENDED_BACKUP_PATH)

        m_date = datetime.today().strftime('%Y-%m-%d')

        log.g().i(MESSAGES.S_STARTING_BACKUP)
        self.__create_backup(PATHS.S_BACKUP_PATH + m_date,PATHS.S_BACKUP_PATH ,SETTINGS.S_MAX_BACKUP_COUNT)

        log.g().i(MESSAGES.S_STARTING_EXTENDED_BACKUP)
        self.__create_backup(PATHS.S_EXTENDED_BACKUP_PATH + m_date,PATHS.S_EXTENDED_BACKUP_PATH ,SETTINGS.S_EXTENDED_MAX_BACKUP_COUNT)

    # External Reuqest Manager
    def invoke_trigger(self, p_command, p_data=None):
        if p_command == BACKUP_MODEL_COMMANDS.S_START_CRONJOB:
            return self.__init_backup()


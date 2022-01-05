import threading
import warnings

from cronjob_manager.jobs.cleanup_controller.cleanup_manager.cleanup_controller import cleanup_controller
from native_services.services.mongo_manager.mongo_controller import mongo_controller
from native_services.services.mongo_manager.mongo_enums import MONGO_CRUD, MONGODB_COMMANDS

warnings.filterwarnings("ignore", category=RuntimeWarning)
from time import sleep
from log_manager.log_controller import log
from cronjob_manager.constants.cronjob_commands import DICTIONARY_CONTROLLER_COMMANDS, BACKUP_CONTROLLER_COMMANDS, \
    CLEANUP_CONTROLLER_COMMANDS
from cronjob_manager.jobs.backup_controller.backup_manager.backup_controller import backup_controller
from cronjob_manager.jobs.dictionary_controller.dictionary_manager.dictionary_controller import dictionary_controller
from cronjob_manager.application_controller.application_enums import APPICATION_MODEL_COMMANDS, CRONJOB_COMMANDS_TIMER
from cronjob_manager.shared_model.request_handler import request_handler

class application_model(request_handler):
    __instance = None
    __m_timer = 0

    # Initializations
    def __init__(self):
        pass

    def __init_dictionary(self):
        dictionary_controller.get_instance().invoke_trigger(DICTIONARY_CONTROLLER_COMMANDS.S_INIT_DICTIONARY)

    def __create_backup(self):
        backup_controller.get_instance().invoke_trigger(BACKUP_CONTROLLER_COMMANDS.S_CREATE_BACKUP)

    def __start_cleanup(self):
        cleanup_controller.get_instance().invoke_trigger(CLEANUP_CONTROLLER_COMMANDS.S_START_CLEANUP)

    def __init_cronjob(self):
        while True:
            try:
                sleep(1)
                self.__m_timer+=1

                #if self.__m_timer % CRONJOB_COMMANDS_TIMER.S_CREATE_BACKUP == 0:
                #    self.__create_backup()
                #if self.__m_timer % CRONJOB_COMMANDS_TIMER.S_INIT_DICTIONARY == 0:
                #    self.__init_dictionary()
                if self.__m_timer % CRONJOB_COMMANDS_TIMER.S_START_CLEANUP == 0:
                    self.__start_cleanup()

            except Exception as ex:
                log.g().e("APP 1 : " + str(ex))

    def __on_start_cronjob(self):
        self.__m_main_thread = threading.Thread(target=self.__init_cronjob)
        self.__m_main_thread.start()

    def __on_create_application_status(self):
        mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_UPDATE, [MONGODB_COMMANDS.S_CREATE_STATUS, [], [True]])

    # External Reuqest Manager
    def invoke_trigger(self, p_command, p_data=None):
        if p_command == APPICATION_MODEL_COMMANDS.S_START_CRONJOB:
            return self.__on_start_cronjob()
        if p_command == APPICATION_MODEL_COMMANDS.S_CREATE_APPLICATION_STATUS:
            return self.__on_create_application_status()


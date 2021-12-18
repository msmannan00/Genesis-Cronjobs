from cronjob_manager.constants.cronjob_commands import BACKUP_CONTROLLER_COMMANDS
from cronjob_manager.constants.strings import ERROR_MESSAGES
from cronjob_manager.jobs.backup_controller.backup_manager.backup_enums import BACKUP_MODEL_COMMANDS
from cronjob_manager.jobs.backup_controller.backup_manager.backup_model import backup_model
from cronjob_manager.shared_model.request_handler import request_handler

class backup_controller(request_handler):
    __instance = None
    __m_backup_model = None

    # Initializations
    @staticmethod
    def get_instance():
        if backup_controller.__instance is None:
            backup_controller()
        return backup_controller.__instance

    def __init__(self):
        if backup_controller.__instance is not None:
            raise Exception(ERROR_MESSAGES.S_SINGLETON_EXCEPTION)
        else:
            backup_controller.__instance = self
            self.__m_backup_model = backup_model()

    def __on_start(self):
        self.__m_backup_model.invoke_trigger(BACKUP_MODEL_COMMANDS.S_START_CRONJOB)

    # External Reuqest Manager
    def invoke_trigger(self, p_command, p_data=None):
        if p_command == BACKUP_CONTROLLER_COMMANDS.S_CREATE_BACKUP:
            return self.__on_start()


from cronjob_manager.constants.cronjob_commands import CLEANUP_CONTROLLER_COMMANDS
from cronjob_manager.constants.strings import ERROR_MESSAGES
from cronjob_manager.jobs.cleanup_controller.cleanup_manager.cleanup_enums import CLEANUP_MODEL_COMMANDS
from cronjob_manager.jobs.cleanup_controller.cleanup_manager.cleanup_model import cleanup_model
from cronjob_manager.shared_model.request_handler import request_handler

class cleanup_controller(request_handler):
    __instance = None
    __m_cleanup_model = None

    # Initializations
    @staticmethod
    def get_instance():
        if cleanup_controller.__instance is None:
            cleanup_controller()
        return cleanup_controller.__instance

    def __init__(self):
        if cleanup_controller.__instance is not None:
            raise Exception(ERROR_MESSAGES.S_SINGLETON_EXCEPTION)
        else:
            cleanup_controller.__instance = self
            self.__m_cleanup_model = cleanup_model()

    def __on_start(self):
        self.__m_cleanup_model.invoke_trigger(CLEANUP_MODEL_COMMANDS.S_START_CRONJOB)

    # External Reuqest Manager
    def invoke_trigger(self, p_command, p_data=None):
        if p_command == CLEANUP_CONTROLLER_COMMANDS.S_START_CLEANUP:
            return self.__on_start()


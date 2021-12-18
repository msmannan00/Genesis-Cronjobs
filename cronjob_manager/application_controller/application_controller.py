import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
from cronjob_manager.application_controller.application_enums import APPICATION_CONTROLLER_COMMANDS, APPICATION_MODEL_COMMANDS
from cronjob_manager.application_controller.application_model import application_model
from cronjob_manager.constants.strings import ERROR_MESSAGES
from cronjob_manager.shared_model.request_handler import request_handler

class application_controller(request_handler):
    __instance = None
    __m_application_model = None

    # Initializations
    @staticmethod
    def get_instance():
        if application_controller.__instance is None:
            application_controller()
        return application_controller.__instance

    def __init__(self):
        if application_controller.__instance is not None:
            raise Exception(ERROR_MESSAGES.S_SINGLETON_EXCEPTION)
        else:
            application_controller.__instance = self
            self.__m_application_model = application_model()

    def __on_start(self):
        self.__m_application_model.invoke_trigger(APPICATION_MODEL_COMMANDS.S_START_CRONJOB)

    def __on_create_application_status(self):
        self.__m_application_model.invoke_trigger(APPICATION_MODEL_COMMANDS.S_CREATE_APPLICATION_STATUS)

    # External Reuqest Manager
    def invoke_trigger(self, p_command, p_data=None):
        if p_command == APPICATION_CONTROLLER_COMMANDS.S_START_APPLICATION:
            return self.__on_start()
        if p_command == APPICATION_CONTROLLER_COMMANDS.S_CREATE_APPLICATION_STATUS:
            return self.__on_create_application_status()


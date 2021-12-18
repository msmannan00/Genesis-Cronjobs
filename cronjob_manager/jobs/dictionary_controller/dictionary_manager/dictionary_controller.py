from cronjob_manager.constants.cronjob_commands import DICTIONARY_CONTROLLER_COMMANDS
from cronjob_manager.constants.strings import ERROR_MESSAGES
from cronjob_manager.jobs.dictionary_controller.dictionary_manager.dictionary_enums import DICTIONARY_MODEL_COMMANDS
from cronjob_manager.jobs.dictionary_controller.dictionary_manager.dictionary_model import dictionary_model
from cronjob_manager.shared_model.request_handler import request_handler

class dictionary_controller(request_handler):
    __instance = None
    __m_dictionary_model = None

    # Initializations
    @staticmethod
    def get_instance():
        if dictionary_controller.__instance is None:
            dictionary_controller()
        return dictionary_controller.__instance

    def __init__(self):
        if dictionary_controller.__instance is not None:
            raise Exception(ERROR_MESSAGES.S_SINGLETON_EXCEPTION)
        else:
            dictionary_controller.__instance = self
            self.__m_dictionary_model = dictionary_model()

    def __on_start(self):
        self.__m_dictionary_model.invoke_trigger(DICTIONARY_MODEL_COMMANDS.S_START_CRONJOB)

    # External Reuqest Manager
    def invoke_trigger(self, p_command, p_data=None):
        if p_command == DICTIONARY_CONTROLLER_COMMANDS.S_INIT_DICTIONARY:
            return self.__on_start()


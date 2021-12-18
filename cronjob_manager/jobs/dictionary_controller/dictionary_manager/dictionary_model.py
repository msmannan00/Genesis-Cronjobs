import requests as requests

from cronjob_manager.helper_services.helper_method import helper_method
from cronjob_manager.jobs.dictionary_controller.constant.constant import WEB_PATHS
from cronjob_manager.jobs.dictionary_controller.constant.strings import MESSAGES
from cronjob_manager.jobs.dictionary_controller.dictionary_manager.dictionary_enums import DICTIONARY_MODEL_COMMANDS
from cronjob_manager.jobs.dictionary_controller.models.word_model import word_model
from cronjob_manager.shared_model.request_handler import request_handler
from log_manager.log_controller import log
from native_services.services.mongo_manager.mongo_controller import mongo_controller
from native_services.services.mongo_manager.mongo_enums import MONGO_CRUD, MONGODB_COMMANDS


class dictionary_model(request_handler):
    __instance = None

    # Initializations
    def __init__(self):
        pass

    def __init_dictionary(self):
        log.g().i(MESSAGES.S_DICTIONARY_UPDATE_STARTED)
        mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_UPDATE, [MONGODB_COMMANDS.S_UPDATE_DICTIONARY_STATUS, [True], [False]])
        m_response = requests.get(WEB_PATHS.S_DICT_PATH)

        if m_response.status_code == 200:
            m_empty_status = mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_COUNT, [MONGODB_COMMANDS.S_COUNT_DICTIONARY, [],[]])
            if m_empty_status>0:
                log.g().i(MESSAGES.S_RESET_DICT)
                mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_UPDATE, [MONGODB_COMMANDS.S_RESET_DICTIONARY, [],[False]])
            else:
                log.g().w(MESSAGES.S_LIST_EMPTY)

            log.g().i(MESSAGES.S_LOADING_DICT)
            for m_word in m_response.text.splitlines():
                m_word_model = word_model(m_word, False, 0, helper_method.get_mongodb_date())
                mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_UPDATE,[MONGODB_COMMANDS.S_INIT_DICTIONARY, [m_word_model], [True]])
                log.g().i(MESSAGES.S_LOADING_WORD + " : " + m_word)
            log.g().s(MESSAGES.S_FINISHED_LOADING_DICT)
        else:
            log.g().w(MESSAGES.S_RESPONSE_FAILED)
        mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_UPDATE, [MONGODB_COMMANDS.S_UPDATE_DICTIONARY_STATUS, [False], [False]])
        mongo_controller.get_instance().invoke_trigger(MONGO_CRUD.S_DELETE, [MONGODB_COMMANDS.S_CLEAN_DICTIONARY, [helper_method.get_mongodb_date()], [False]])

    # External Reuqest Manager
    def invoke_trigger(self, p_command, p_data=None):
        if p_command == DICTIONARY_MODEL_COMMANDS.S_START_CRONJOB:
            return self.__init_dictionary()


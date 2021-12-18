from native_services.services.mongo_manager.mongo_enums import MONGODB_COMMANDS, MONGODB_KEYS, MONGODB_COLLECTIONS
from native_services.shared_model.request_handler import request_handler

class mongo_request_generator(request_handler):

    def __init__(self):
        pass

    def __reset_dictionary(self):
        return {MONGODB_KEYS.S_DOCUMENT: MONGODB_COLLECTIONS.S_DICTIONARY_MODEL,MONGODB_KEYS.S_FILTER:{} ,MONGODB_KEYS.S_VALUE:{'$set': { 'm_user_generated':False}}}

    def __init_dictionary(self, p_word_model):
        return {MONGODB_KEYS.S_DOCUMENT: MONGODB_COLLECTIONS.S_DICTIONARY_MODEL,MONGODB_KEYS.S_FILTER:{'m_word': {'$eq': p_word_model.m_word}} ,MONGODB_KEYS.S_VALUE:{'$setOnInsert': {'m_user_generated': p_word_model.m_user_generated, 'm_score': p_word_model.m_score}, '$set': { 'm_last_update':p_word_model.m_last_update}}}

    def __count_dictionary(self):
        return {MONGODB_KEYS.S_DOCUMENT: MONGODB_COLLECTIONS.S_DICTIONARY_MODEL,MONGODB_KEYS.S_FILTER:{}}

    def __create_status(self):
        return {MONGODB_KEYS.S_DOCUMENT: MONGODB_COLLECTIONS.S_APP_STATUS_MODEL,MONGODB_KEYS.S_FILTER:{'m_application_status': {'$eq': True}} ,MONGODB_KEYS.S_VALUE:{ '$set': {'m_creating_backup':False, 'm_updating_dictionary':False, 'm_updating_tfidf':False}}}

    def __update_backup_status(self, p_status):
        return {MONGODB_KEYS.S_DOCUMENT: MONGODB_COLLECTIONS.S_APP_STATUS_MODEL,MONGODB_KEYS.S_FILTER:{} ,MONGODB_KEYS.S_VALUE:{ '$set': {'m_creating_backup':p_status}}}

    def __update_dictionary_status(self, p_status):
        return {MONGODB_KEYS.S_DOCUMENT: MONGODB_COLLECTIONS.S_APP_STATUS_MODEL,MONGODB_KEYS.S_FILTER:{} ,MONGODB_KEYS.S_VALUE:{ '$set': {'m_updating_dictionary':p_status}}}

    def __create_backup(self, p_collection):
        return {MONGODB_KEYS.S_DOCUMENT: p_collection,MONGODB_KEYS.S_FILTER:{}}

    def __clean_dictionary(self, p_days):
        return {MONGODB_KEYS.S_DOCUMENT: MONGODB_COLLECTIONS.S_DICTIONARY_MODEL,MONGODB_KEYS.S_FILTER:{'m_user_generated': {'$eq': True},} ,MONGODB_KEYS.S_VALUE:{}}

    def invoke_trigger(self, p_commands, p_data=None):
        if p_commands == MONGODB_COMMANDS.S_RESET_DICTIONARY:
            return self.__reset_dictionary()
        if p_commands == MONGODB_COMMANDS.S_INIT_DICTIONARY:
            return self.__init_dictionary(p_data[0])
        if p_commands == MONGODB_COMMANDS.S_COUNT_DICTIONARY:
            return self.__count_dictionary()
        if p_commands == MONGODB_COMMANDS.S_CREATE_BACKUP:
            return self.__create_backup(p_data[0])
        if p_commands == MONGODB_COMMANDS.S_CREATE_STATUS:
            return self.__create_status()
        if p_commands == MONGODB_COMMANDS.S_UPDATE_BACKUP_STATUS:
            return self.__update_backup_status(p_data[0])
        if p_commands == MONGODB_COMMANDS.S_UPDATE_DICTIONARY_STATUS:
            return self.__update_dictionary_status(p_data[0])
        if p_commands == MONGODB_COMMANDS.S_CLEAN_DICTIONARY:
            return self.__clean_dictionary(p_data[0])

# Local Imports
from cronjob_manager.shared_model.request_handler import request_handler
from native_services.services.elastic_manager.elastic_enums import ELASTIC_REQUEST_COMMANDS, ELASTIC_KEYS, ELASTIC_INDEX


class elastic_request_generator(request_handler):

    def __on_create_backup(self):
        m_query_statement = {
            "size": 1000000,
            "query": {
                "match": {
                    "script.m_sub_host": 'na'
                }
            }
        }
        return {ELASTIC_KEYS.S_DOCUMENT: ELASTIC_INDEX.S_WEB_INDEX, ELASTIC_KEYS.S_FILTER: m_query_statement}

    def invoke_trigger(self, p_commands, p_data=None):
        if p_commands == ELASTIC_REQUEST_COMMANDS.S_BACKUP:
            return self.__on_create_backup()

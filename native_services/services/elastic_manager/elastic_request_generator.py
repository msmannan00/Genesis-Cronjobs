# Local Imports
from cronjob_manager.shared_model.request_handler import request_handler
from native_services.services.elastic_manager.elastic_enums import ELASTIC_REQUEST_COMMANDS, ELASTIC_KEYS, ELASTIC_INDEX


class elastic_request_generator(request_handler):

    def __on_create_backup(self):
        m_query_statement = {
            "size": 1000000,
            "query": {
                "match": {
                    "m_sub_host": 'na'
                }
            }
        }
        return {ELASTIC_KEYS.S_DOCUMENT: ELASTIC_INDEX.S_WEB_INDEX, ELASTIC_KEYS.S_FILTER: m_query_statement}

    def __on_del_clean(self, p_min_date):
        m_query_statement = {
            "query": {
                "range": {
                    "m_date": {
                        "lte": p_min_date,
                    }
                }
            }
        }

        return {ELASTIC_KEYS.S_DOCUMENT: ELASTIC_INDEX.S_WEB_INDEX, ELASTIC_KEYS.S_FILTER: m_query_statement}

    def __on_clean_monthly(self, p_min_date):
        m_query = {
            "script": 'ctx._source.m_half_month_hits = 0',
            "query": {
                "range": {
                    "m_date": {
                        "lte": p_min_date,
                    }
                }
            }
        }

        return {ELASTIC_KEYS.S_DOCUMENT: ELASTIC_INDEX.S_WEB_INDEX, ELASTIC_KEYS.S_VALUE: m_query}

    def __on_clean_daily(self, p_min_date):
        m_query = {
            "script": 'ctx._source.m_daily_hits = 0',
            "query": {
                "range": {
                    "m_date": {
                        "lte": p_min_date,
                    }
                }
            }
        }

        return {ELASTIC_KEYS.S_DOCUMENT: ELASTIC_INDEX.S_WEB_INDEX, ELASTIC_KEYS.S_VALUE: m_query}

    def invoke_trigger(self, p_commands, p_data=None):
        if p_commands == ELASTIC_REQUEST_COMMANDS.S_BACKUP:
            return self.__on_create_backup()
        if p_commands == ELASTIC_REQUEST_COMMANDS.S_DEL_CLEAN:
            return self.__on_del_clean(p_data[0])
        if p_commands == ELASTIC_REQUEST_COMMANDS.S_CLEAN_MONTHLY_SCORE:
            return self.__on_clean_monthly(p_data[0])
        if p_commands == ELASTIC_REQUEST_COMMANDS.S_CLEAN_DAILY_SCORE:
            return self.__on_clean_daily(p_data[0])

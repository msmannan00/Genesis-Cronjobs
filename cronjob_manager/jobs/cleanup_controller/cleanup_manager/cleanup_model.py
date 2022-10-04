from cronjob_manager.helper_services.helper_method import helper_method
from cronjob_manager.jobs.cleanup_controller.cleanup_manager.cleanup_enums import CLEANUP_MODEL_COMMANDS
from cronjob_manager.jobs.cleanup_controller.constant.strings import CLEANUP_MESSAGES
from cronjob_manager.shared_model.request_handler import request_handler
from log_manager.log_controller import log
from native_services.services.elastic_manager.elastic_controller import elastic_controller
from native_services.services.elastic_manager.elastic_enums import ELASTIC_CRUD_COMMANDS, ELASTIC_REQUEST_COMMANDS


class cleanup_model(request_handler):
    __instance = None

    # Initializations
    def __init__(self):
        pass

    def __start_cleanup(self):
        log.g().i(CLEANUP_MESSAGES.S_CLEANUP_STARTING)
        log.g().i(CLEANUP_MESSAGES.S_CLEANUP_MONTHLY)
        elastic_controller.get_instance().invoke_trigger(ELASTIC_CRUD_COMMANDS.S_DELETE, [ELASTIC_REQUEST_COMMANDS.S_DEL_CLEAN, [helper_method.get_time()-12], [None]])
        log.g().i(CLEANUP_MESSAGES.S_CLEANUP_MID_MONTHLY)
        elastic_controller.get_instance().invoke_trigger(ELASTIC_CRUD_COMMANDS.S_UPDATE, [ELASTIC_REQUEST_COMMANDS.S_CLEAN_MONTHLY_SCORE, [helper_method.get_time()-6], [False]])
        log.g().i(CLEANUP_MESSAGES.S_CLEANUP_DAILY)
        elastic_controller.get_instance().invoke_trigger(ELASTIC_CRUD_COMMANDS.S_UPDATE, [ELASTIC_REQUEST_COMMANDS.S_CLEAN_DAILY_SCORE, [helper_method.get_time()-1], [None]])
        log.g().i(CLEANUP_MESSAGES.S_CLEANUP_FINISHED)
        pass

    # External Reuqest Manager
    def invoke_trigger(self, p_command, p_data=None):
        if p_command == CLEANUP_MODEL_COMMANDS.S_START_CRONJOB:
            return self.__start_cleanup()


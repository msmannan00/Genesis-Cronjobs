from cronjob_manager.application_controller.application_controller import application_controller
from cronjob_manager.application_controller.application_enums import APPICATION_CONTROLLER_COMMANDS
from settings.sitemap import SITEMAP


def load_user_website_crawler():
    pass


if __name__ == SITEMAP.M_USER_WEBSITE_CRAWLER:
    load_user_website_crawler()

application_controller.get_instance().invoke_trigger(APPICATION_CONTROLLER_COMMANDS.S_CREATE_APPLICATION_STATUS)
application_controller.get_instance().invoke_trigger(APPICATION_CONTROLLER_COMMANDS.S_START_APPLICATION)

class APPICATION_CONTROLLER_COMMANDS:
    S_START_APPLICATION = 1
    S_CREATE_APPLICATION_STATUS = 2

class APPICATION_MODEL_COMMANDS:
    S_START_CRONJOB = 1
    S_CREATE_APPLICATION_STATUS = 2

class CRONJOB_COMMANDS_TIMER:
    S_CREATE_BACKUP = 10
    S_START_CLEANUP = 10
    S_PING = 10

class CRONJOB_MESSAGES:
    S_ALIVE = "pinging alive"

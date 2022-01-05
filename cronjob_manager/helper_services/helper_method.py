# Local Imports
import datetime
import math
import time


class helper_method:

    @staticmethod
    def get_mongodb_date():
        return (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days

    @staticmethod
    def get_time():
        return math.ceil(time.time()/(60*60*24))

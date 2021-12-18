# Local Imports
import datetime

class helper_method:

    @staticmethod
    def get_mongodb_date():
        return (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days

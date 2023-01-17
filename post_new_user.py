from db_client import add_user
import sys
from pymysql.err import IntegrityError

def post_user(user_id, user_name):
    try:
        add_user(user_id, user_name)
        return 0
    except IntegrityError as err:
        message = (err.args[1])
        if ("Duplicate entry" in message):
            return 1
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        sys.exit(1)
        return 2

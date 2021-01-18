import random
from . import constant


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def http_headers():
    return {
        "User-Agent": random_user_agent(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }


def random_user_agent():
    return str(random.choice(constant.USER_AGENTS))

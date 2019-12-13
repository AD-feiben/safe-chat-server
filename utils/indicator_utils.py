import re


def is_user_id(indicator):
    return re.match(r'^[u][0-9_]*$', indicator)


def is_emil(indicator):
    return re.match(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$', indicator)

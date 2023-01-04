import re


def check_number(phone):
    if re.fullmatch('\+?[1-9]\d{6,14}', phone):
        return True
    return False
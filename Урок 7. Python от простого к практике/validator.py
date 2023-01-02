import re

def validate_num(pattern, num):
    if re.fullmatch(pattern, num):
        return True
    return False
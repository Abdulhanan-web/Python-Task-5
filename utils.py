import time
import re

def retry_send(func, retries=3):
    for i in range(retries):
        success, msg = func()
        if success:
            return True, msg
        time.sleep(2)
    return False, msg


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
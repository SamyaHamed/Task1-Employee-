import csv
import os.path
import utils.constants as const

from email_validator import validate_email, EmailNotValidError
import re
from datetime import datetime, date



def validate_employee(**kwargs):
    validators = {
        "name": name_validation,
        "email": email_validation,
        "birthday": birthday_validation,
    }
    for attr , validator in validators.items():
        value = kwargs.get(attr)
        if not validator(value):
            raise ValueError(f"Invalid value for {attr}")
    return True



def email_validation(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def name_validation(name):
    if bool(re.search(r'\d', name)):
        return False
    else:
        return True


def birthday_validation(birthday):
    try:
        if isinstance(birthday, date):
            birth_date = birthday
        elif isinstance(birthday, str):
            birth_date = datetime.strptime(birthday, const.DATE_FORMAT).date()
        else:
            return False
        age = datetime.today().year - birth_date.year
        return age >= const.MIN_AGE
    except ValueError:
        return False



def email_exists(filename,email):
    if not os.path.exists(filename):
        return False
    with open(filename,'r',newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Email'].lower() == email.lower():
                return True

        return False



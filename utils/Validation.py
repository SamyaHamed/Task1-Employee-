import csv
import os.path

from email_validator import validate_email, EmailNotValidError
import re
from datetime  import datetime

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
        birth_date = datetime.strptime(birthday, '%m/%d/%Y').date()
        age = (datetime.today().year-birth_date.year)
        return age >= 18
    except ValueError :
        return False

def email_exists(filename,email):
    if not os.path.exists(filename):
        return False
    with open(filename,'r',newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['email'].lower() == email.lower():
                return True

        return False



#name validate --> done
# pass age --> age
# date --> age
# email validate --> done

#database store data csv file






import csv
import os
from utils.Validation import *
class EmployeeManager:
    def __init__(self):
        self.employees = []


    def add_employee(self,employee,strategy,salary):
        employees_file= "data/employees.csv"
        history_file = "data/employee_history.csv"
        if email_exists(employees_file, employee.email):
            print("Employee with this email already exists.")
            return False

        file_exists = os.path.isfile(employees_file)
        with open(employees_file , mode='a',newline='', encoding = 'utf-8') as file1:
            employee_writer = csv.writer(file1)
            if not file_exists:
                employee_writer.writerow(["Name","Birthday","Email"])
            employee_writer.writerow([employee.name,employee.birthday.strftime("%m/%d/%Y"),employee.email])

        file_exists = os.path.isfile(history_file)
        with open(history_file, mode='a', newline='', encoding='utf-8') as file2:
            history_writer = csv.writer(file2)
            if not file_exists:
                history_writer.writerow(["Email","Type", "Salary", "Start Date", "End Date"])
            history_writer.writerow(
                [employee.email, strategy.__class__.__name__,salary,datetime.now().strftime("%m/%d/%Y")])

        print("Employee added successfully.")
        return True


    def search_employee(self,email):
        for emp in  self.employees:
            if emp.email == email:
                return emp
        return None


    def remove_employee(self,filename, email):
        if not os.path.exists(filename):
            print("File does not exist")
            return False

        rows = []
        removed = False

        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames

            for row in reader:
                if row["Email"].lower() != email.lower():
                    rows.append(row)
                else:
                    removed = True

        if not removed:
            print("Email not found")
            return False

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

        print("Employee removed successfully")
        return True








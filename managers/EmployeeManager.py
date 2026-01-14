import csv
import os
import utils.constants as const
from datetime import datetime
from models.Employee import Employee
from models.EmploymentHistory import EmploymentHistory
from utils.Validation import email_exists, validate_employee
import pandas as pd
from strategies.SalaryFactory import SalaryFactory


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def load_employees(self):
        if not os.path.exists(const.EMPLOYEE_FILE):
            return
        df = pd.read_csv(const.EMPLOYEE_FILE)
        for _, row in df.iterrows():
            emp = Employee(
                name=row["Name"],
                birthday=row["Birthday"],
                email=row["Email"]
            )
            self.employees.append(emp)

    def load_history(self):
        if not os.path.exists(const.HISTORY_FILE):
            return
        df = pd.read_csv(const.HISTORY_FILE)
        for _, row in df.iterrows():
            emp = self.search_employee(row["Email"])
            if not emp:
                continue
            history = EmploymentHistory(
                strategy=SalaryFactory.create_salary_strategy(row["Type"]),
                salary=pd.to_numeric(row["Salary"]),
                start_date=pd.to_datetime(row["Start Date"]).date(),
                end_date=pd.to_datetime(row["End Date"]).date()
                if pd.notna(row["End Date"]) else None
            )
            emp.history.append(history)

    def save_employees(self):
        rows=[]
        for emp in self.employees:
            rows.append({
                "Name": emp.name,
                "Birthday": emp.birthday,
                "Email": emp.email,
            })
        pd_emp = pd.DataFrame(rows)
        pd_emp.to_csv(const.EMPLOYEE_FILE,index=False)

    def save_history(self):
        rows=[]
        for emp in self.employees:
            for h in emp.history:
                rows.append({
                    "Email" : emp.email,
                    "Salary" : h.salary,
                    "Type": emp.strategy.__class__.__name__,
                    "Start Date" : h.start_date,
                    "End Date" : h.end_date,
                })
        pd_his = pd.DataFrame(rows)
        pd_his.to_csv(const.HISTORY_FILE,index=False)





    def add_employee(self,employee,strategy,salary):
        try:
            validate_employee(name=employee.name, birthday=employee.birthday, email=employee.email)
        except ValueError as e:
            print(f"Cannot add employee: {e}")

        if email_exists(const.EMPLOYEE_FILE, employee.email):
            print("Employee with this email already exists.")

        self.employees.append(employee)
        employee.add_period(strategy, salary)

        if os.path.exists(const.EMPLOYEE_FILE):
            df_emp = pd.read_csv(const.EMPLOYEE_FILE)
        else:
            df_emp = pd.DataFrame(columns=["Name", "Birthday", "Email"])

        new_emp = {
            "Name": employee.name,
            "Birthday": employee.birthday.strftime(const.DATE_FORMAT),
            "Email": employee.email
        }
        df_emp = pd.concat([df_emp, pd.DataFrame([new_emp])], ignore_index=True)
        df_emp.to_csv(const.EMPLOYEE_FILE, index=False)


        if os.path.exists(const.HISTORY_FILE):
            df_hist = pd.read_csv(const.HISTORY_FILE)
        else:
            df_hist = pd.DataFrame(columns=["Email", "Type", "Salary", "Start Date", "End Date"])
        new_hist = {
            "Email": employee.email,
            "Type": strategy.__class__.__name__,
            "Salary": salary,
            "Start Date": datetime.now().strftime("%Y-%m-%d"),
            "End Date": ""
        }
        df_hist = pd.concat([df_hist, pd.DataFrame([new_hist])], ignore_index=True)
        df_hist.to_csv(const.HISTORY_FILE, index=False)
        print("Employee added successfully.")
        return True


    def search_employee(self,email):
        for emp in  self.employees:
            if emp.email == email:
                return emp
        return None


    def remove_employee(self,filename, email):
        for emp in  self.employees:
            if emp.email == email:
                self.employees.remove(emp)
                self.save_employees()
                self.save_history()
        return None








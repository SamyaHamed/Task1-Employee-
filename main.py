from models.Employee import Employee
from strategies.SalaryStrategy import PartTimeStrategy, FullTimeStrategy
from utils.Validation import *
from managers.EmployeeManager import EmployeeManager

manager = EmployeeManager()
while True:
    print("\n\n Welcome to the Control Panel!")
    print("Please choose one of the options below to get started:")
    print("1.Add Employee \n"
          "2.Remove Employee \n"
          "3.Convert The Type Of Employee \n"
          "4.Display Employee Details\n"
          "5.Calculate Salary \n"
          "6.Exit")
    choice = input()
    match choice:
        case "1":
            name = input("Enter Employee Name: ")
            if not name_validation(name):
                print("Invalid Name")
                continue

            birthday = input("Enter your date of birth(MM/DD/YYYY): ")
            if not birthday_validation(birthday):
                print("Invalid Age")
                continue

            email = input("Enter Employee Email: ")
            if not email_validation(email):
                print("Invalid Email")
                continue

            salary = float(input("Enter Employee Salary: "))
            employee_type = input("Enter Employee Strategy(part/full): ").lower()
            if employee_type == "part":
                strategy = PartTimeStrategy()
            else:
                strategy = FullTimeStrategy()

            employee = Employee(name, birthday, email)
            manager.add_employee(employee, strategy, salary)

        case "2":
            email = input("Enter Employee Email: ").strip()
            manager.remove_employee("data/employees.csv",email)

        case"3":
            email = input("Enter Employee Email: ").strip()
            emp = manager.search_employee(email)
            if emp is None:
                print("Employee not found")
                continue

            salary = float(input("Enter Employee Salary: "))
            employee_type = input("Enter Employee Strategy(part/full): ").lower()
            if employee_type == "part":
                strategy = PartTimeStrategy()
            else:
                strategy = FullTimeStrategy()
            emp.add_period(strategy,salary)
            print("Employee Strategy Converted Successfully!")

        case "4":
            email = input("Enter Employee Email to display info:").strip()
            emp =manager.search_employee(email)
            if emp is None:
                print("Employee not found")
                continue
            emp.display()
            emp.display_history()

        case "5":
            email = input("Enter Employee Email to calculate salary:").strip()
            emp =manager.search_employee(email)
            if emp is None:
                print("Employee not found")
                continue
            print("total salary =",emp.calculate_salary())

        case "6":
            print("Exiting... Goodbye!")
            break
        case _:
            print("Invalid Choice\n")



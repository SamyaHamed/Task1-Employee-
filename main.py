from models.Employee import Employee
from strategies.SalaryStrategy import PartTimeStrategy, FullTimeStrategy
from managers.EmployeeManager import EmployeeManager
import utils.constants as const
from  utils import input_helpers
from utils.input_helpers import employee_input, add_period_input

manager = EmployeeManager()
manager.load_employees()
manager.load_history()
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
            name ,birthday ,email , salary ,strategy = employee_input()
            employee = Employee(name, birthday, email)
            manager.add_employee(employee, strategy, salary)

        case "2":
            email = input("Enter Employee Email: ").strip()
            manager.remove_employee(const.EMPLOYEE_FILE,email)

        case"3":
            email = input("Enter Employee Email: ").strip()
            emp = manager.search_employee(email)
            if emp is None:
                print("Employee not found")
                continue

            salary ,strategy = add_period_input()
            emp.add_period(strategy,salary)
            manager.save_history()
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



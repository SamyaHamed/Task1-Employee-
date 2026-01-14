from strategies.SalaryStrategy import FullTimeStrategy, PartTimeStrategy


def employee_input():
    global strategy
    name = input("Enter Employee Name: ").strip()
    birthday = input("Enter Employee Birthday(YYYY-MM-DD): ").strip()
    email = input("Enter Employee Email: ").strip()

    while True:
        try:
            salary = float(input("Enter Employee Salary: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    employee_type = input("Enter Employee Type (full/part): ").strip().lower()
    if employee_type == "full":
        strategy = FullTimeStrategy()
    elif employee_type == "part":
        strategy = PartTimeStrategy()

    return name, birthday, email, salary, strategy

def add_period_input():
    global strategy
    while True:
        try:
            salary = float(input("Enter Employee Salary: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    employee_type = input("Enter Employee Strategy(part/full): ").lower()
    if employee_type == "part":
        strategy = PartTimeStrategy()
    else:
        strategy = FullTimeStrategy()
    return  salary, strategy

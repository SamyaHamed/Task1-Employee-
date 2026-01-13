from .EmploymentHistory import EmploymentHistory
from datetime import date, datetime


class Employee:
    _id_counter = 1

    def __init__(self,name,birthday,email):
        self._employee_id = Employee._id_counter
        Employee._id_counter += 1
        self.name = name
        self.birthday = datetime.strptime(birthday, "%m/%d/%Y").date()
        self.email = email
        self.history = []



    @property
    def employee_id(self):
        return self._employee_id

    def add_period(self, strategy, salary):
        if self.history:
            self.history[-1].end_period()

        period = EmploymentHistory( strategy,salary,date.today())
        self.history.append(period)

    def calculate_salary(self):
        total = 0
        for p in self.history:
            total += p.calculate_salary()
        return total

    def display_history(self):
        for p in self.history:
            print("Employment History:")
            print("salary:" , p.salary )
            print("from:" ,p.start_date )
            print("to:",p.end_date )


    def display(self):
        print("Employee id :",self.employee_id)
        print("Employee name:",self.name)
        print("Employee age:",(date.today().year-self.birthday.year))
        print("Employee email:",self.email)








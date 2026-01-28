from .EmploymentHistory import EmploymentHistory
from datetime import date, datetime
import utils.constants as const

class Employee:
    def __init__(self,name,birthday,email):
        self.name = name
        self.birthday = datetime.strptime(birthday, const.DATE_FORMAT).date()
        self.email = email
        self.history = []




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
        print("Employee name:",self.name)
        print("Employee age:",(date.today().year-self.birthday.year))
        print("Employee email:",self.email)








from  datetime import  date
class EmploymentHistory:
    def __init__(self,strategy,salary,start_date, end_date = None):
        self.strategy = strategy
        self.salary = salary
        self.start_date = start_date
        self.end_date = end_date

    def end_period(self):
        if self.end_date is None:
            self.end_date = date.today()

    def duration_in_days(self):
        end = self.end_date or date.today()
        return (end - self.start_date).days

    def calculate_salary(self):
        return self.strategy.calculate_salary(self.salary, self.duration_in_days())


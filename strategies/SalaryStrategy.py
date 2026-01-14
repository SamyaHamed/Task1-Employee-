from abc import ABC, abstractmethod

# like interface:
class SalaryStrategy(ABC):
    @abstractmethod
    def calculate_salary(self,salary,days_worked):
        pass

class FullTimeStrategy(SalaryStrategy):
    def calculate_salary(self, salary, days_worked):
        daily = salary / 30
        return daily * days_worked


class PartTimeStrategy(SalaryStrategy):
    def calculate_salary(self, salary, days_worked):
        daily = salary /30
        return daily * days_worked * 0.5




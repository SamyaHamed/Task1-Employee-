from abc import ABC, abstractmethod

# like interface:
class SalaryStrategy(ABC):
    @abstractmethod
    def calculate_salary(self,salary,days):
        pass

class FullTimeStrategy(SalaryStrategy):
    def calculate_salary(self, salary, days):
        daily = salary / 30
        return daily * days


class PartTimeStrategy(SalaryStrategy):
    def calculate_salary(self, salary, days):
        daily = salary / 30
        return daily * days * 0.5


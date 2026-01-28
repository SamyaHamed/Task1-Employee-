from strategies.SalaryStrategy import  PartTimeStrategy,FullTimeStrategy
class SalaryFactory:
    @staticmethod
    def create_salary_strategy(strategy_type:str):
        if strategy_type == "FullTimeStrategy":
            return FullTimeStrategy()
        elif strategy_type == "PartTimeStrategy":
            return PartTimeStrategy()
        else:
            raise ValueError("Invalid strategy type")


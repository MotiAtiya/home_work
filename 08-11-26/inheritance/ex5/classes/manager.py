from .employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_cost(self):
        return super().monthly_cost() + self.bonus
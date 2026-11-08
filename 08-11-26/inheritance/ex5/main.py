from classes.employee import Employee
from classes.manager import Manager

print(Employee("Dana", 12000).monthly_cost())
print(Manager("Avi", 20000, 3000).monthly_cost())

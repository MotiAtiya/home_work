from classes.employee import Employee
from classes.manager import Manager

dana = Employee("Dana", 12000)
avi = Manager("Avi", 20000)
print(dana.describe())
print(avi.describe())
print(avi.manage(5))

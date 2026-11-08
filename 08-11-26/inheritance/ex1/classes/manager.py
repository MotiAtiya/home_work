from .employee import Employee

class Manager(Employee):
    def manage(self, size):
        return f"{self.name} manages {size} people" 
    
class Employee:
    def __init__(self, name):
        self.name = name   

    def display_name(self):   
        print(self.name)

emp = Employee("Seshadri")
emp.display_name()    
print(emp.name)

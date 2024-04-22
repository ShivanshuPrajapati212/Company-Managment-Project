class Employee:
    def __init__(self,name,id,employee_type):
        self.name = name
        self.id = id
        self.employee_type = employee_type
    def salary(self):
        print(f"Working {self.name} {self.id} {self.employee_type}")

class HourlyEmployee(Employee):
    def info(self):
        print(self.employee_type)



if __name__ == "__main__":
    ram = HourlyEmployee('Ram',8999,'Part-time')
    print(ram.salary())
    print(ram.info())
class Employee:
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name

    def display(self):
        print(f"Employee ID :{self.emp_id}")
        print(f"Employee Name :{self.name}")


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name,basic_salary,hra,bonus):
        super().__init__(emp_id, name)
        self.basic_salary=basic_salary
        self.hra=hra
        self.bonus=bonus

    def calculate_salary(self):
        return self.basic_salary + self.hra + self.bonus
    
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name,hours_worked,rate_per_hour):
        super().__init__(emp_id, name)
        self.hours_worked=hours_worked
        self.rate_per_hour=rate_per_hour

    def calculate_salary(self):
        return self.hours_worked*self.rate_per_hour
    

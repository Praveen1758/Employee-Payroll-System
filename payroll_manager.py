from employee import FullTimeEmployee,PartTimeEmployee
from file_handler import FileHandler    
from exceptions import EmployeeNotFound

class PayrollManager:
    def __init__(self):
        self.employees=FileHandler.load_employees()

    def add_employee(self,employee):
        self.employees.append(employee)

    def view_employees(self):
        if len(self.employees)==0:
            print("No Employees Found")
            return
        
        for emp in self.employees:
            print("-"*30)
            emp.display()
            print("salary:",emp.calculate_salary())

    def search_employee(self,emp_id):

        for emp in self.employees:

            if emp.emp_id ==emp_id:
                emp.display()
                print("salary: ",emp.calculate_salary())
                return 
        raise EmployeeNotFound("Employee Not Found")

    def delete_employee(self,emp_id):

        for emp in self.employees:

            if emp.emp_id==emp_id:
                self.employees.remove(emp)
                FileHandler.rewrite_file(self.employees )
                print(f"Employee {emp_id} Deleted Successfully")
                return
        print("Employee Not Found")

    def update_employee(self,emp_id):

        for emp in self.employees:
            if emp.emp_id==emp_id:
                new_name=input("Enter New Name: ")
                emp.name=new_name
                FileHandler.rewrite_file(self.employees)
                print("Employee Updated successfully")
                return
        print("Employee Not Found")

    def employee_exists(self, emp_id):

        for emp in self.employees:

            if emp.emp_id == emp_id:
                return True

        return False
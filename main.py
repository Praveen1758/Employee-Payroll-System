from employee import FullTimeEmployee, PartTimeEmployee
from payroll_manager import PayrollManager
from exceptions import EmployeeNotFound
from file_handler import FileHandler

manager = PayrollManager()

while True:

    print("\n===== Employee Payroll System =====")
    print("1. Add Full Time Employee")
    print("2. Add Part Time Employee")
    print("3. View Employees")
    print("4. Search Employee")
    print("5. Delete Employee")
    print("6. Update Employee")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        try:
            emp_id = int(input("Enter Employee ID: "))
            if manager.employee_exists(emp_id):
                print("Employee ID Already Exists")
                continue
            name = input("Enter Name: ")
            basic_salary = float(input("Enter Basic Salary: "))
            hra = float(input("Enter HRA: "))
            bonus = float(input("Enter Bonus: "))

            employee = FullTimeEmployee(
                emp_id,
                name,
                basic_salary,
                hra,
                bonus
            )

            manager.add_employee(employee)
            data = f"{emp_id},{name},FULLTIME,{basic_salary},{hra},{bonus}"
            FileHandler.save_employee(data)

            print("Employee Added Successfully")

        except ValueError:
            print("Invalid Input")

    elif choice == "2":

        try:
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            hours_worked = int(input("Enter Hours Worked: "))
            rate_per_hour = float(input("Enter Rate Per Hour: "))

            employee = PartTimeEmployee(
                emp_id,
                name,
                hours_worked,
                rate_per_hour
            )

            manager.add_employee(employee)

            print("Employee Added Successfully")

        except ValueError:
            print("Invalid Input")

    elif choice == "3":

        manager.view_employees()

    elif choice == "4":

        try:
            emp_id = int(input("Enter Employee ID: "))

            manager.search_employee(emp_id)

        except EmployeeNotFound as e:
            print(e)

        except ValueError:
            print("Invalid Employee ID")

    elif choice == "5":

        try:
            emp_id = int(input("Enter Employee ID: "))

            manager.delete_employee(emp_id)

        except ValueError:
            print("Invalid Employee ID")

    elif choice == "6":

        try:
            emp_id = int(input("Enter Employee ID: "))

            manager.update_employee(emp_id)

        except ValueError:
            print("Invalid Employee ID")

    elif choice == "7":

        print("Thank You")
        break

    else:
        print("Invalid Choice")
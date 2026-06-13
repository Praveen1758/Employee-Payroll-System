from employee import FullTimeEmployee,PartTimeEmployee

class FileHandler:

    @staticmethod
    def save_employee(data):
        with open("employees.txt","a") as file:
            file.write(data+"\n")

    @staticmethod
    def load_employees():
        employees=[]

        try:
            with open("employees.txt","r") as file:

                for line in file:

                    data=line.strip().split(",")

                    if data[2]=="FULLTIME":

                        employee=FullTimeEmployee(
                            int(data[0]),
                            data[1],
                            float(data[3]),
                            float(data[4]),
                            float(data[5])
                        )

                    elif data[2]=="PARTTIME":

                        employee=PartTimeEmployee(
                            int(data[0]),
                            data[1],
                            int(data[3]),
                            float(data[4])
                        )
                    employees.append(employee)

        except FileNotFoundError:
            pass

        return employees
    
    @staticmethod
    def rewrite_file(employees):

        with open("employees.txt", "w") as file:

            for emp in employees:

                if isinstance(emp, FullTimeEmployee):

                    data = (
                        f"{emp.emp_id},"
                        f"{emp.name},"
                        f"FULLTIME,"
                        f"{emp.basic_salary},"
                        f"{emp.hra},"
                        f"{emp.bonus}\n"
                )

                else:

                    data = (
                        f"{emp.emp_id},"
                        f"{emp.name},"
                        f"PARTTIME,"
                        f"{emp.hours_worked},"
                        f"{emp.rate_per_hour}\n"
                )

                file.write(data)
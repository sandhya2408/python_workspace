class Employee:
    def __init__(self,empno,name,qualification,salary,dept_name):
        self.empno = empno
        self.name = name
        self.qualification = qualification 
        self.salary = salary
        self.dept_name = dept_name
    def show_Info(self):
        print(f"{self.empno} - {self.name} - {self.qualification} - {self.salary} - {self.dept_name}")
    def inc_salary(self, inc_amount):
        self.salary += inc_amount
        print(f"{self.name} salary after increment :{self.salary}")
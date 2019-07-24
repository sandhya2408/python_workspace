from employee import Employee
lst_emp = []
def load_emp():
    with open("emp.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata = data.strip("\n").split(",")
            empno = int(edata[0])
            name = edata[1]
            qualification = edata[2]
            salary = int(edata[3])
            dept_name = edata[4]
            emp = Employee(empno, name, qualification, salary, dept_name)
            lst_emp.append(emp)
    print(f"total employeees count:{len(lst_emp)}")
def showDeptName():
    dnames = set(map(lambda emp:emp.dept_name , lst_emp))
    for name in dnames:
        print(name)
def showAllTheQualifications():
    qualifications = set(map(lambda emp:emp.qualification, lst_emp))
    for qual in qualifications:
        print(qual)

def maxSalaryEmp():
    sal = max(list(map(lambda emp:emp.salary, lst_emp)))
    ms = list(filter(lambda emp:emp.salary == sal,lst_emp))
    for m in ms:
        m.show_Info()
def showEmpCountByDeptName():
    pass
def showTotalSalByDeptName():
    pass
def showEmpCountByQual():
    pass

load_emp()
print("all departments...")
showDeptName()
print("all qualifications...")
showAllTheQualifications()
print("details of max salary")
maxSalaryEmp()
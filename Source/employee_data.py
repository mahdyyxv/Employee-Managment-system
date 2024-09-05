#!./bin/python
employee_data = {
        
        "ID": "0",
        "Name": "Admin",
        "Department": "IT",
        "Salary": 15000,
        "Password": "123",
        "Days of Absence": 2
}
employees_lst = [
    employee_data.copy()
]

def get_employee(employee_id):
    for emp in employees_lst:
        if emp['ID'] == employee_id:
            return emp
    return False

def add_employee(ID, Name, Depart, Salary, Passw, Days_of_abs):
    if not get_employee(ID):
        try:
            employee_data["ID"] = str(ID)
            employee_data["Name"] = Name
            employee_data["Department"] = Depart
            employee_data["Salary"] = int(Salary)
            employee_data["Password"] = Passw
            employee_data["Days of Absence"] = int(Days_of_abs)
            employees_lst.append(employee_data.copy())
            for i in employees_lst:
                print(i)
            return True
        except:
            pass
    return False


def remove_employee(emp_id):
    for emp in employees_lst:
        if emp['ID'] == emp_id:
            employees_lst.remove(emp)
            return True
    return False

def update_employee(emp_id, Name, Depart, Salary, Passw, Days_of_abs):
    for emp in employees_lst:
        if emp['ID'] == emp_id:
            try:
                emp['Name'] = Name
                emp['Department'] = Depart
                emp['Salary'] = int(Salary)
                emp['Password'] = Passw
                emp['Days of Absence'] = int(Days_of_abs)
                return True
            except:
                break
    return False
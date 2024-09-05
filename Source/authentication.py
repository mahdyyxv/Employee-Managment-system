from employee_data import get_employee

def authenticate(employee_id, password):
    global name
    employee = get_employee(employee_id)
    if employee and employee['Password'] == password :
        name = employee['Name']
        return True
    return False

def login(employee_id, password):

    if authenticate(employee_id, password):
        print("Login successful!")
        return name
        
    return False


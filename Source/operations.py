from employee_data import get_employee

def display_info(employee_id):
    employee = get_employee(employee_id)
    str_to_return = ""
    if employee:
        for key, value in employee.items():
            if key == "Password":
                continue
            str_to_return += (f"{key}: {value}\n")
    else:
        return("Employee not found.")
    return str_to_return

def calculate_bonus(employee_id):
    employee = get_employee(employee_id)
    if employee:
        bonus = employee['Salary'] * 0.1
        return(f"Bonus: {bonus}")
    else:
        return("Employee not found.")

def calculate_discount(employee_id):
    employee = get_employee(employee_id)
    if employee:
        discount = employee['Salary'] * 0.05
        return(f"Discount: {discount}")
    else:
        return("Employee not found.")

def remind_legal_holidays(employee_id):
    employee = get_employee(employee_id)
    if employee:
        holidays = 30 - employee['Days of Absence']  # Assuming 30 legal holidays per year
        return(f"Remaining legal holidays: {holidays}")
    else:
        return("Employee not found.")

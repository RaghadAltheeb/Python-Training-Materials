def get_salary(employee_dict, emp_id):
    emp= employee_dict.get(emp_id)
    return emp.get("salary","Not Found")

#def update_salary(employee_dict, emp_id, new_salary):
    
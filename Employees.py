class Employee:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def emp_info(self):
        return f"saxeli - {self.name}, gvari - {self.surname}, asaki - {self.age}, xelfasi - {self.salary}"




import csv

employee_list = []
with open('dataset1.csv', 'r') as d:
    reader = csv.reader(d)
    next(reader)

    for row in reader:
        employee_list.append(Employee(row[0], row[1], (row[2]), (row[3])))



per_with_max_age = max(employee_list, key=lambda x: x.age)
print("yvelaze didi asakis mqonde : ",per_with_max_age.emp_info())
per_with_min_salary = min(employee_list, key=lambda x: x.salary)
print("yvelaze patara xelfasis mqone: ",per_with_min_salary.emp_info())






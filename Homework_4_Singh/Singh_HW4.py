#Name:Pratik Singh
#Student id: 1001670417

import employee
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME  = 'employees.dat'

def main():
    myemp = load_emp()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(myemp)
        elif choice == ADD:
            add(myemp)
        elif choice == CHANGE:
            change(myemp)
        elif choice == DELETE:
            delete(myemp)
        elif choice == QUIT:
            exit()
    save_employees(myemp)

def load_emp():
    try:
        input_file = open(FILENAME, 'rb')

        employee_dct = pickle.load(input_file)
        input_file.close()

    except IOError:
        employee_dct = {}

    return employee_dct

def get_menu_choice():
    print()
    print("MENU")
    print("-----------------------------------")
    print("1. Look up an employee in the dictionary")
    print("2. Add a new employee to the dictionary")
    print("3. Change an existing employee's name, department and job title in the dictionary")
    print("4. Delete an employee from the dictionary")
    print("5. Quit the program")
    print()

    choice = int(input("Enter your choice: "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    return choice

def look_up(myemp):
    emp_ID = input("Enter an employee ID: ")
    print(myemp.get(emp_ID, 'That employee is not found.'))

def add(myemp):
    name = input("Enter name of the employee: ")
    emp_ID = input("Enter ID Number: ")
    dep = input("Enter department: ")
    jobtitle = input("Enter the job title: ")

    new_employee = employee.Employee(name, emp_ID, dep, jobtitle)

    if emp_ID not in myemp:
        myemp[emp_ID] = new_employee
        print("New employee has been added.")
    else:
        print("That employee already exists.")

def change(myemp):
    emp_ID = input("Enter an employee ID: ")
    if emp_ID in myemp:
        name = input("Enter the new name: ")
        dep = input("Enter the new department: ")
        jobtitle = input("Enter the new job title: ")

        changed = employee.Employee(name, emp_ID, dep, jobtitle)

        myemp[emp_ID] = changed
        print("Information updated.")
    else:
        print("That employee is not found.")

def delete(myemp):
    emp_ID = input("Enter an employee ID: ")
    if emp_ID in myemp:
        del myemp[emp_ID]
        print("Employee deleted.")
    else:
        print("That employee is not found.")


def exit():
    print("Bye.....!!!!")

    
def save_employees(myemp):
    output_file = open(FILENAME, 'wb')
    pickle.dump(myemp, output_file)
    output_file.close()

main()


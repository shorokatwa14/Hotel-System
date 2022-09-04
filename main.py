import os
import time

#This is a Practical exam in my college 
#We were three participants in this project
def customer_main_menu():
    print("\n\n\t\t\t********************\n")
    print("\t\t\t*Hello our visitor!*\n")
    print("\t\t\t********************\n\n")
    num = '1'
    while num != '5':
        time.sleep(.8)
        print("1- Show rooms categories.\n")
        print("2- Book a room.\n")
        print("3- Customer Reservation\n")
        print("4- Check out.\n")  # Delete Record
        print("5- Main menu.\n\n")
        num = input('Enter Your Choice ')

        if num == '1':
            display_room_categories()
        elif num == '2':
            book_room()
        elif num == '3':
            display_customer_reservation()
        elif num == '4':
            check_out()
        elif num == '5':
            break
        else:
            print("Wrong choice, please try again.\n\n")


def display_room_categories():
    print("\nRoom Category: ")
    print("\nTotal no. of Rooms - 50")
    print("\nOrdinary Rooms from 1 - 30")
    print("\nLuxuary Rooms from 31 - 45")
    print("\n Royal Rooms from 46 - 50\n\n")


def book_room():
    with open("room.txt", 'a') as file:
        c = 'y'
        while c == 'y':
            display_room_categories()
            r = input("Enter The Room No. you want to stay in :- ")
            if int(r) > 50:
                print("Sorry,Wrong Room Number, please try again.\n\n")
            else:
                print("Enter room type : \n")
                print("1- Single\n")
                print("2- Double\n")
                print("3- Suite\n\n")
                print("4- Main menu\n\n")
                choice = input("\t\t\tEnter your choice :")
                if int(choice) > 4 or int(choice) < 1:
                    print("Wrong choice, please try again.\n\n")
                name = input("Enter your name : ")
                if int(choice) == 1 and 1 <= int(r) <= 30:
                    print("ordinary and Single room has been booked for you Mr/Ms. " + name + '\n')
                elif int(choice) == 2 and 1 <= int(r) <= 30:
                    print("ordinary and Double room has been booked for you Mr/Ms. " + name + '\n')
                elif int(choice) == 3 and 1 <= int(r) <= 30:
                    print("ordinary and Suite has been booked for you Mr/Ms. " + name + '\n')
                elif int(choice) == 1 and 31 <= int(r) <= 45:
                    print("tLuxury and single room has been booked for you Mr/Ms. " + name + '\n')
                elif int(choice) == 2 and 31 <= int(r) <= 45:
                    print("Luxury and Double room has been booked for you Mr/Ms. " + name + '\n')
                elif int(choice) == 3 and 31 <= int(r) <= 45:
                    print("tLuxury and Suite  has been booked for you Mr/Ms. " + name + '\n')
                elif int(choice) == 1 and 46 <= int(r) <= 50:
                    print("\t\t\tRoyal and single  has been booked for you Mr/Ms. " + name + '\n')
                elif int(choice) == 3 and 31 <= int(r) <= 45:
                    print("\t\t\tRoyal and Double  has been booked for you Mr/Ms." + name + '\n')
                elif int(choice) == 3 and 31 <= int(r) <= 45:
                    print("\t\t\tRoyal and Suite  has been booked for you Mr/Ms. " + name + '\n')

                if int(choice) == 1:
                    room_type = 'Single'
                elif int(choice) == 2:
                    room_type = 'Double'
                elif int(choice) == 3:
                    room_type = 'Suite'
                if 1 <= int(r) <= 30:
                    room_c = 'Ordinary'
                elif 30 < int(r) <= 45:
                    room_c = 'Luxury'
                else:
                    room_c = 'Royal'
                file.write(name + '\t' + r + '\t' + room_c + '\t' + room_type + '\n')
                c = input('\t\t\tEnter record y/n ')
    file.close()


def customer_reservation():
    with open("room.txt", 'r') as file:
        for line in file:
            fields = line.split('\t')
            print('Name : ' + fields[0])
            print('Room No: ' + fields[1])
            print('Room Category: ' + fields[2])
            print('Room Type: ' + fields[3] + '\n')


def check_out():
    import os
    file = open("room.txt", 'r')
    tempfile = open('temp.txt', 'w')
    room_no = input('Enter Your Room Number: ')
    ok = False
    for line in file:
        fields = line.split('\t')
        if fields[1] == room_no:
            ok = True
        else:
            tempfile.write(line)
    file.close()
    tempfile.close()
    os.remove('room.txt')
    os.rename('temp.txt', 'room.txt')
    if not ok:
        print("\n\t\t\tThere is no room with such number\n")
    else:
        print("\n\t\t\tCheked out successfully\n")


def display_customer_reservation():
    room_no = input('\t\t\tEnter Room Number To Display Customer Reservation : ')
    with open("room.txt", 'r') as file:
        flag = False
        for line in file:
            fields = line.split('\t')
            if fields[1] == room_no:
                flag = True
                fields = line.split('\t')
                print('\nName : ' + fields[0])
                print('Room No: ' + fields[1])
                print('Room Category: ' + fields[2])
                print('Room Type: ' + fields[3] + '\n')
        if not flag:
            print('Customer Not Found in The Hotel System')


def add_employee():
    with open('employees.txt', 'a') as file:
        ch = 'y'
        while 'y' == ch or ch == 'Y':
            id = input('Enter employee id : ')
            name = input('Enter employee name : ')
            age = input('Enter employee age : ')
            salary = input('Enter employee salary : ')
            file = open('employees.txt', 'a')
            file.write(id + '\t' + name + '\t' + age + '\t' + salary + '\n')
            ch = input('Do you want to enter more record (y/ n) ')
        print('File successfully saved \n')


def search_employee():
    id = input('Enter employee id to search : ')
    found = False
    with open('employees.txt', 'r') as file:
        for line in file:
            part = line.split('\t')
            if part[0] == id:
                print(f"Name : {part[1]}\nAge : {part[2]}\nSalary : {part[3]}")
                found = True
        if not found:
            print(f"There is no employee with id {id}")


def display_employees():
    with open('employees.txt', 'r') as file:
        print('Id\tName\tAge\tSalary')
        print('-----------------------')
        for line in file:
            print(line)


def delete_employee():
    id = input('Enter employee id to delete : ')
    file = open('employees.txt', 'r')
    tmp = open('tmp.txt', 'x')
    found = False
    for line in file:
        part = line.split('\t')
        if part[0] == id:
            found = True
        else:
            tmp.write(line)
    file.close()
    tmp.close()
    os.remove('employees.txt')
    os.rename('tmp.txt', 'employees.txt')
    if not found:
        print('Employee not found')
    else:
        print('Employee has been deleted successfully')


def update_employee_salary():
    id = input('Enter id to update : ')
    file = open('employees.txt', 'r')
    tmp = open('tmp.txt', 'x')
    found = False
    for line in file:
        part = line.split('\t')
        if part[0] == id:
            found = True
            salary = input(f'Enter new salary for {part[1]} ')
            line = part[0] + '\t' + part[1] + '\t' + part[2] + '\t' + salary + '\n'

        tmp.write(line)
    file.close()
    tmp.close()
    os.remove('employees.txt')
    os.rename('tmp.txt', 'employees.txt')
    if not found:
        print('employee not found')
    else:
        print('employee has been updated successfully')


def employees_operations_menu():
    print("\n\n\t\t\t**********************")
    print("\t\t\t*Welcome to the System*")
    print("\t\t\t**********************\n")
    choice = '1'
    time.sleep(.8)
    while choice != '6':
        print('1- Add employee')
        print('2- search for employee')
        print('3- Display All employees')
        print('4- Update employee salary')
        print('5- Delete employee')
        print('6- Main menu')
        choice = input('Enter your choice : ')
        if choice == '1':
            add_employee()
        elif choice == '2':
            search_employee()
        elif choice == '3':
            display_employees()
        elif choice == '4':
            update_employee_salary()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            break
        else:
            print('Wrong choice, Try again')
        time.sleep(1)


def add_food():
    with open('project.txt', 'a') as file:
        c = 'y'
        while c == 'y':
            name = input('Enter name  : ')
            price = input('Enter price : ')
            code = input('Enter code : ')
            file.write(str(name) + '\t' + str(price) + '\t' + str(code) + '\n')
            c = input('Do you want to enter record again ( y/ n ) ? ')


def display_food_menu():
    with open('project.txt', 'r') as file:
        print('name \t price \t code ')
        print('----------------------------')
        for line in file:
            print(line)


def search_menu():
    price = str(input('Enter the price of food to search  for : '))
    with open('project.txt', 'r') as file:
        flag = True
        for line in file:
            field = line.split('\t')
            if field[1] == price:
                flag = False
                print('ID \t Name \t Age ')
                print('----------------------------')
                print(line)
    if flag:
        print('not found')


def delete_menu():
    import os
    price = input('Enter the price of food to delete  for : ')
    file = open('project.txt', 'r')
    tmp = open('tmp.txt', 'w')
    flag = False
    for line in file:
        field = line.split('\t')
        if field[1] == price:

            flag = True
        else:
            tmp.write(line)
    file.close()
    tmp.close()
    os.remove('project.txt')
    os.rename('tmp.txt', 'project.txt')

    if not flag:
        print('food not found')
    else:
        print('food deleted successfully')


def update_menu():
    price = input('Enter the price of food you want to update : ')
    nprice = input('Enter the new price you want : ')
    file = open('project.txt', 'r')
    tmp = open('tmp.txt', 'w')

    flag = True
    for line in file:
        field = line.split('\t')
        if field[1] == price:
            flag = False
            line = field[0] + '\t' + nprice + '\t' + field[2] + '\n'
        tmp.write(line)
    file.close()
    tmp.close()
    os.remove('project.txt')
    os.rename('tmp.txt', 'project.txt')
    if flag:
        print('not found')
    else:
        print('the price is updated')


def food_menu():
    test = '1'
    while test != '6':
        time.sleep(.8)
        print('1-Enter new food:')
        print('2-Display menu:')
        print('3-Update food price:')
        print('4-Search for food:')
        print('5-Delete  food from menu:')
        print('6-Main menu : ')
        test = input('Enter your choice:')
        if test == '1':
            add_food()
        elif test == '2':
            display_food_menu()
        elif test == '3':
            update_menu()
        elif test == '4':
            search_menu()
        elif test == '5':
            delete_menu()
        elif test == '6':
            break
        else:
            print("Wrong choice, please try again.\n\n")


def main_menu():
    print("\t\t\t**********************")
    print("\t\t\t*Welcome to the hotel*")
    print("\t\t\t**********************\n")
    choice = '1'
    while choice != '4':
        print('1- Customer')
        print('2- System Management')
        print('3- Chef')
        print('4- exit')
        choice = input('Enter your choice : ')
        if choice == '1':
            customer_main_menu()
        elif choice == '2':
            employees_operations_menu()
        elif choice == '3':
            food_menu()
        elif choice == '4':
            break
        else:
            print("Wrong choice, please try again.\n\n")


main_menu()

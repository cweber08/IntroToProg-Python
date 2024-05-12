# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using constants, variables, and print()
# Change Log: (Who, When, What)
#   cweber,5/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

from sys import exit

# define constants:
MENU: str = """""""""
----Course Registration Program----
  Select from the following menu:
   1.Register a Student for a Course
   2.Show current data
   3.Save data to a file
   4.Exit the program
------------------------------------"""""""""
# print(MENU)
FILE_NAME = "Enrollment.csv"

# variables:
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''  # I did not find a reason to use this
file_obj = None
menu_choice: str = ''
student_data: dict
students: list = []
parts: list[str]

try:
    file = open(FILE_NAME, 'r')
    for row in file.readlines():
        parts = row.strip().split(',')
        student_first_name = parts[0]
        student_last_name = parts[1]
        course_name = parts[2]
        student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
       # student_data = row.strip().split(',') --> leftover from assignment04
        students.append(student_data)
except FileNotFoundError as e:
    print('Text file not found')
    print('---Technical Information---')
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()
print(students)

while True:
    print(MENU)
    menu_choice = input("Enter a menu option 1-4: ")

# create inputs and add new students to student data list
    if menu_choice == "1":
        try:
            student_first_name = input("Please enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('The first name must be alphabetic')
            student_last_name = input("Please enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('The last name must be alphabetic')
            course_name = input("Please enter the course name: ")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            students.append(student_data)
        except ValueError as e:
            print(e)
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')

# print a string of the student data list
    elif menu_choice == "2":
        print("-" * 50)
        for student_data in students:
            print(f"Student {student_data['first_name']} {student_data['last_name']} is enrolled in {student_data['course_name']}")
        print("-" * 50)
        continue

# write data from student data list to csv
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, 'w')
            for student_data in students:
                student_first_name = student_data['first_name']
                student_last_name = student_data['last_name']
                course_name = student_data['course_name']
                file.write(f'{student_first_name},{student_last_name},{course_name}\n')
            file.close()
        except TypeError as e:
            print('csv data was malformed')
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()

    elif menu_choice == "4":
        exit()

    else:
        print("Invalid Option, please choose 1-4:")

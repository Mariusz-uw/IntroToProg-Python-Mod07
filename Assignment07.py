# ----------------------------------------------------------------------------- #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Mariusz Sokol>,<3, 12, 2025>,<Activity>
# ----------------------------------------------------------------------------- #

import json

class Person:
    """Represents a person with basic attributes."""

    def __init__(self, student_first_name: str = "", student_last_name: str = ""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

class Student(Person):
    """
    Extends Person to include course enrollment information.
    """
    def __init__(self, student_first_name: str = "", student_last_name: str = "",
                 course_name: str = ""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name
        self.course_name = course_name

class FileProcessor:
    """
    Handles file input and output operations.
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads student data from a JSON file into a list of Student objects."""
        try:
            with open(file_name, "r") as file:
                student_data.clear()
                data = json.load(file)
                for item in data:
                    student_data.append(Student(**item))
        except Exception as e:
            IO.output_error_messages("Error reading file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes student data to a JSON file."""
        try:
            with open(file_name, "w") as file:
                json.dump([student.__dict__ for student in student_data], file)
            IO.output_student_courses(student_data)
        except Exception as e:
            IO.output_error_messages("Error writing to file.", e)

class IO:
    """
    Handles user interface input/output operations.
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays an error message with optional technical details."""
        print(f"Error: {message}")
        if error:
            print(f"Technical details: {error}")

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu."""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets a menu choice from the user."""
        return input("Enter your choice: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays the current student and course enrollments."""
        print("-" * 50)
        for student in student_data:
            print(f'{student.student_first_name} {student.student_last_name}'
                  f' is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """Gets student data from the user and adds it to the list."""
        try:
            first_name = input("Enter student's first name: ")
            if not first_name.isalpha():
                raise ValueError("First name must contain only letters.")
            last_name = input("Enter student's last name: ")
            if not last_name.isalpha():
                raise ValueError("Last name must contain only letters.")
            course_name = input("Enter course name: ")
            student_data.append(Student(first_name, last_name, course_name))
            print(f"Successfully registered {first_name} {last_name}"
                  f" for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(str(e), e)
        except Exception as e:
            IO.output_error_messages("Unexpected error while entering"
                                     " student data.", e)

MENU = '''\n---- Course Registration Program ----
    Select from the following menu:\n
1. Register a Student for a course
2. Show current Data
3. Save data to a file
4. Exit the program\n'''
FILE_NAME = "Enrollments.json"
students = []

FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    choice = IO.input_menu_choice()

    if choice == '1':
        IO.input_student_data(students)
    elif choice == '2':
        IO.output_student_courses(students)
    elif choice == '3':
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

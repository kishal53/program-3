# Student Data Organizer

## Introduction

Student Data Organizer is a Python menu-driven program used to manage student records.
This project allows users to:

* Add student details
* Display all students
* Update student information
* Delete student records
* Display all subjects offered

The program uses Python data structures like List, Dictionary, Tuple, and Set.

---

# Variables Used

li = stores all student records

name = stores student name

age = stores student age

grade = stores student grade

subjects = stores subjects entered by user

ID = stores student ID

birthdate = stores student birthdate

id_bd = tuple storing ID and birthdate

dictionary = stores one student's complete data

choice = stores menu option selected by user

i = used to access each student record in loop

update_id = stores student ID for updating

update_choice = stores update option selected by user

del_id = stores student ID for deletion

found = checks whether student record exists or not

all_subjects = stores all unique subjects

---

# Logic of the Program

1. The program first displays a menu.

2. User selects an option using input.

3. Match-case statement performs different operations based on user choice.

4. Student details are stored using dictionaries inside a list.

5. Subjects are stored using sets to avoid duplicate subjects.

6. Tuple is used to store student ID and birthdate together.

7. Loops are used to search, display, update, and delete records.

8. The program runs continuously using a while loop until the user selects Exit.

---

# Conclusion

This project helps in understanding the practical use of Python data structures and menu-driven programming.
It is useful for beginners to learn how real-world data can be stored and managed using Python.

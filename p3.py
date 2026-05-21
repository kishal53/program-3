print("Welcome to Student Data Organizer!")

li = []

while True:

    print("\nSelect an Option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:

            print("\nEnter Student Details:")

            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")

            subjects = set(
                input("Enter subjects (comma separated): ").split(",")
            )

            ID = int(input("Enter student ID: "))

            birthdate = input("Enter birthdate (YYYY-MM-DD): ")

            id_bd = (ID, birthdate)

            dictionary = {
                'name': name,
                'age': age,
                'grade': grade,
                'subjects': subjects,
                'ID': id_bd[0],
                'birthdate': id_bd[1]
            }

            li.append(dictionary)

            print("Student added successfully!")

        case 2:

            print("\nDisplaying All Students:\n")

            if len(li) == 0:
                print("No student records found.")

            else:
                for i in li:
                    print("----------------------------")
                    print("ID:", i['ID'])
                    print("Name:", i['name'])
                    print("Age:", i['age'])
                    print("Grade:", i['grade'])
                    print("Subjects:", i['subjects'])
                    print("Birthdate:", i['birthdate'])

        case 3:

            update_id = int(input("Enter student ID to update: "))

            found = False

            for i in li:

                if i['ID'] == update_id:

                    print("\nWhat do you want to update?")
                    print("1. Name")
                    print("2. Age")
                    print("3. Grade")
                    print("4. Subjects")
                    print("5. Birthdate")

                    update_choice = int(input("Enter your choice: "))

                    match update_choice:

                        case 1:
                            i['name'] = input("Enter new name: ")

                        case 2:
                            i['age'] = int(input("Enter new age: "))

                        case 3:
                            i['grade'] = input("Enter new grade: ")

                        case 4:
                            i['subjects'] = set(
                                input("Enter new subjects (comma separated): ").split(",")
                            )

                        case 5:
                            i['birthdate'] = input(
                                "Enter new birthdate (YYYY-MM-DD): "
                            )

                        case _:
                            print("Invalid choice")

                    print("Student information updated successfully!")

                    found = True
                    break

            if found == False:
                print("Student ID not found.")

        case 4:

            del_id = int(input("Enter student ID to delete: "))

            found = False

            for i in li:

                if i['ID'] == del_id:

                    li.remove(i)

                    print("Student deleted successfully!")

                    found = True
                    break

            if found == False:
                print("Student ID not found.")

        case 5:

            all_subjects = set()

            for i in li:
                all_subjects.update(i['subjects'])

            print("\nSubjects Offered:")
            print(all_subjects)

        case 6:

            print("Thank you for using Student Data Organizer!")
            break

        case _:

            print("Invalid choice. Please try again.")
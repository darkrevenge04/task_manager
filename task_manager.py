import datetime

# Referenced material
# https://stackoverflow.com/questions/9750330/how-to-convert-integer-into-date-object-python
# Used to understand how to convert data to datetime

# Colours text
c = "\33[1;32m"
og = "\33[0m"

# =====importing libraries===========
#  takes data from txt files and sets them as variables.

user = open("user.txt", "r+", encoding="utf-8")
stored_user = user.readlines()
user.close()
tasks = open("tasks.txt", "r+", encoding="utf-8")
stored_tasks = tasks.readlines()
tasks.close()

# ====Login Section====

# Default values
username = ""
password = ""

accepted_usernames = []
accepted_passwords = []

# takes login details and splits them into relevant fields.
for i in range(len(stored_user)):
    accepted_usernames += stored_user[i].split(",")[:1]
    accepted_passwords += stored_user[i].replace(" ", "").replace("\n", "").split(",")[1:2]

# Checks username and password against user.txt and give appropriate responses.
while True:
    if username == "":
        username = str(input("Please enter a Username:\t"))
    if password == "":
        password = str(input("Please enter a Password:\t"))
    if username in accepted_usernames:
        position = accepted_usernames.index(username)
        if password == accepted_passwords[position]:
            print(f"welcome {c}{username}{og}")
            break
        else:
            print("Incorrect password! Please try again.")
            password = str(input("Please enter a Password:\t"))
            continue
    else:
        print("Incorrect Username and Password! Please try again")
        print("\n")
        username = ""
        password = ""
        continue

# presenting the menu to the user and making sure that the user input is converted to lower case.
if username != "admin":
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
else:
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    s - Statistics
    : ''').lower()

if menu == 'r':
    new_user = str(input("Please enter new Username:\t"))
    new_password = ""

    # asks for new user details and checks. if correct will upload to the user.txt file
    while True:
        new_password = str(input("Please enter new Password:\t"))
        new_password_confirm = str(input("Please re-enter the password:\t"))
        if new_password == new_password_confirm:
            with open("user.txt", "a+", encoding="utf-8") as user:
                user.writelines(f"\n{new_user}, {new_password}")
                print(f"The User {c}{new_user}{og} has been successfully added.")
            break
        else:
            print("The Passwords do not match. Please try again")

    # updates user details
    user = open("user.txt", "r+", encoding="utf-8")
    stored_user = user.readlines()
    user.close()
    for i in range(len(stored_user)):
        accepted_usernames += stored_user[i].split(",")[:1]
        accepted_passwords += stored_user[i].replace(" ", "").replace("\n", "").split(",")[1:2]

elif menu == 'a':
    if username == "admin":
        # gets details about task
        task_title = str(input("Please enter the task's title:\t"))
        task_description = str(input("Enter a description of the task:\t"))
        task_due_date = str(input("Enter the due date (DD/MM/YY):\t"))

        # Ensures that date is filled in
        while True:
            if task_due_date == "":
                print("task due date invalid, please try again")
                task_due_date = str(input("Enter the due date (DD/MM/YY)"))
            else:
                break

        task_due_date_formatted = datetime.datetime.strptime(task_due_date, "%d/%m/%y")
        assigned_date = datetime.datetime.today()
        assigned_user = str(input("Enter the Username of the person assigned to the task"))

        # Checks that the user exists
        while True:
            if assigned_user not in accepted_usernames:
                print(f"The user {c}{assigned_user}{og} does not exist please try again")
                assigned_user = str(input("Enter the Username of the person assigned to the task"))
            else:
                break

        # Checks that the due date is valid
        while True:
            if task_due_date_formatted < assigned_date:
                print("Due date can't be before today")
                task_due_date = str(input("Enter the due date"))
            else:
                break

        # Checks if the title form is empty
        while True:
            if task_title == "":
                print("Task title can't be blank")
                task_title = str(input("Please enter the task's title"))
            else:
                break

        # Checks if description is blank
        while True:
            if task_description == "":
                response = str(input("Task description is empty! Are you sure you wish to continue (Y/N"))
                if response.lower() == "y" or response.lower() == "yes":
                    break
                elif response.lower() == "n" or response.lower() == "no":
                    task_description = str(input("Enter a description of the task"))
                else:
                    print("Invalid response, please try again")
            else:
                break

        #  Displays all inputted task data
        def check():
            print(f"task title:\t{c}{task_title}{og}\n"
                  f"Assigned User:\t{c}{assigned_user}{og}\n"
                  f"Task Assigned Date:\t{c}{assigned_date.strftime('%d/%m/%y')}{og}\n"
                  f"Task Due Date:\t{c}{task_due_date_formatted.strftime('%d/%m/%y')}{og}\n"
                  f"Task Description:\t{c}{task_description}{og}")

        check()

        response_task_input = ""

        while True:
            if response_task_input == "":
                response_task_input = str(input("Are these details correct? (Y/N):\t"))
            elif response_task_input.lower() == "y" or response_task_input.lower() == "yes":
                with open("tasks.txt", "a+", encoding="utf-8") as tasks:
                    tasks.write(f"\n{assigned_user}, {task_title}, {task_description}, "
                                f"{assigned_date.strftime('%d/%m/%y')}, "
                                f"{task_due_date_formatted.strftime('%d/%m/%y')}, No")
                print(f"The task {c}{task_title}{og} has been created successfully")
                break
            elif response_task_input.lower() == "n" or response_task_input.lower() == "no":

                # gets details about task
                task_title = str(input("Please enter the task's title:\t"))
                task_description = str(input("Enter a description of the task:\t"))
                task_due_date = str(input("Enter the due date (DD/MM/YY):\t"))

                # Ensures that date is filled in
                while True:
                    if task_due_date == "":
                        print("task due date invalid, please try again")
                        task_due_date = str(input("Enter the due date (DD/MM/YY)"))
                    else:
                        break

                task_due_date_formatted = datetime.datetime.strptime(task_due_date, "%d/%m/%y")
                assigned_date = datetime.datetime.today()
                assigned_user = str(input("Enter the Username of the person assigned to the task"))

                # Checks that the user exists
                while True:
                    if assigned_user not in accepted_usernames:
                        print(f"The user {c}{assigned_user}{og} does not exist please try again")
                        assigned_user = str(input("Enter the Username of the person assigned to the task"))
                    else:
                        break

                # Checks that the due date is valid
                while True:
                    if task_due_date_formatted < assigned_date:
                        print("Due date can't be before today")
                        task_due_date = str(input("Enter the due date"))
                    else:
                        break

                # Checks if the title form is empty
                while True:
                    if task_title == "":
                        print("Task title can't be blank")
                        task_title = str(input("Please enter the task's title"))
                    else:
                        break

                # Checks if description is blank
                while True:
                    if task_description == "":
                        response = str(input("Task description is empty! Are you sure you wish to continue (Y/N"))
                        if response.lower() == "y" or response.lower() == "yes":
                            break
                        elif response.lower() == "n" or response.lower() == "no":
                            task_description = str(input("Enter a description of the task"))
                        else:
                            print("Invalid response, please try again")
                    else:
                        break
            else:
                print("Invalid response, please try again")
    else:
        print(f"{c}You don't have permission to access this option{og}")
    # Updates the stored task list
    tasks = open("tasks.txt", "r+", encoding="utf-8")
    stored_tasks = tasks.readlines()
    tasks.close()
# sorts task data unto relevant fields

elif menu == 'va':

    imported_task_title = []
    imported_assigned_to = []
    imported_assigned_date = []
    imported_due_date = []
    imported_status = []
    imported_description = []

    for i in range(len(stored_tasks)):
        imported_assigned_to += stored_tasks[i].split(",")[:1]
        imported_task_title += stored_tasks[i].replace("\n", "").split(",")[1:2]
        imported_description += stored_tasks[i].replace("\n", "").split(",")[2:3]
        imported_assigned_date += stored_tasks[i].replace("\n", "").split(",")[3:4]
        imported_due_date += stored_tasks[i].replace("\n", "").split(",")[4:5]
        imported_status += stored_tasks[i].replace("\n", "").split(",")[5:6]

    for i in range(len(imported_task_title)):
        print(f"Task Title:\t\t{c}{str(imported_task_title[i][1:]).capitalize()}{og}")
        print(f"Assigned User:\t{c}{str(imported_assigned_to[i]).capitalize()}{og}")
        print(f"Assigned Date:\t{c}{imported_assigned_date[i][1:]}{og}")
        print(f"Due Date:\t\t{c}{imported_due_date[i][1:]}{og}")
        print(f"Task Completed?:\t{c}{str(imported_status[i][1:]).capitalize()}{og}")
        print(f"Description:\t{c}{str(imported_description[i][1:]).capitalize()}{og}\n")

elif menu == 'vm':
    imported_task_title = []
    imported_assigned_to = []
    imported_assigned_date = []
    imported_due_date = []
    imported_status = []
    imported_description = []

    for i in range(len(stored_tasks)):
        imported_assigned_to += stored_tasks[i].split(",")[:1]
        imported_task_title += stored_tasks[i].replace("\n", "").split(",")[1:2]
        imported_description += stored_tasks[i].replace("\n", "").split(",")[2:3]
        imported_assigned_date += stored_tasks[i].replace("\n", "").split(",")[3:4]
        imported_due_date += stored_tasks[i].replace("\n", "").split(",")[4:5]
        imported_status += stored_tasks[i].replace("\n", "").split(",")[5:6]

    for i in range(len(imported_assigned_to)):
        if imported_assigned_to[i] == username:
            print(f"Task Title:\t\t{c}{str(imported_task_title[i][1:]).capitalize()}{og}")
            print(f"Assigned User:\t{c}{str(imported_assigned_to[i]).capitalize()}{og}")
            print(f"Assigned Date:\t{c}{imported_assigned_date[i][1:]}{og}")
            print(f"Due Date:\t\t{c}{imported_due_date[i][1:]}{og}")
            print(f"Task Completed?:\t{c}{str(imported_status[i][1:]).capitalize()}{og}")
            print(f"Description:\t{c}{str(imported_description[i][1:]).capitalize()}{og}\n")

        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

elif menu == 'e':
    print('Goodbye!!!')
    exit()

elif menu == "s":
    print(f"Number of total Tasks:\t{c}{len(stored_tasks)}{og}")
    print(f"Number of total Users:\t{c}{len(stored_user)}{og}")

else:
    print("You have made a wrong choice, Please Try again")

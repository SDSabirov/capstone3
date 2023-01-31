#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime,date

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
def is_registered(user_name):
    """
    This function will return if user already registered
    then return true or false 
    """
    for user in login_auth:         # login auth global variable which loads values at the begining of the program
        print(user)
        if user[0] == user_name:
            return True
    return False


def reg_user():
    '''In this block you will write code to add a new user to the user.txt file
    - You can follow the following steps:
    - Request input of a new username
    - Request input of a new password
    - Request input of password confirmation.
    - Check if the new password and confirmed password are the same.
    - If they are the same, add them to the user.txt file,
    - Otherwise you present a relevant message.'''

    new_username = input("Enter a new username: ").lower()
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")


    if is_registered(new_username):

        print("User name already exists!")
        
    else:
        
        if password == confirm_password:
            with open('user.txt','a') as f:
                f.write(f"\n{new_username}, {password}")
                print("Credentials saved\n")
        else:
                print("Passwords doesn't match\n")



def add_task():
    '''In this block you will put code that will allow a user to add a new task to task.txt file
    - You can follow these steps:
    - Prompt a user for the following: 
    - A username of the person whom the task is assigned to,
    - A title of a task,
    - A description of the task and 
    - the due date of the task.
    - Then get the current date.
    - Add the data to the file task.txt and
    - You must remember to include the 'No' to indicate if the task is complete.'''

    username = input("Please enter a username: ")
    title = input("Enter a title of the task: ")
    description = input("In few words, describe what is the task about: ")
    registration_date = datetime.today().date()
    registration_date =  registration_date.strftime("%d %b %Y")   #formating date as %d-day %b-month abbreviated %Y-year in 4 digits
    deadline = input("Enter end date dd Month yyyy: ")
    task_completion = input("Task completion status yes/no: ").capitalize()

    #opening file tasks.txt       
    with open('tasks.txt','a') as f:
                #storing variables with appropriate formatting
        f.write(f"\n{username}, {title}, {description}, {registration_date}, {deadline}, {task_completion}")
            
        print("Task successfully saved! ")

def view_all():

    '''In this block you will put code so that the program will read the task from task.txt file and
    print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
    You can do it in this way:
    - Read a line from the file.
    - Split that line where there is comma and space.
    - Then print the results in the format shown in the Output 2 
    - It is much easier to read a file using a for loop.'''
            
    #opening tasks.txt
    with open('tasks.txt','r') as f:

        for line in f:

            line=line.split(", ")   #splitting by coomma and space
            #printing varibales in requared format
            print("_"*80)
            print(f"Task:\t\t{line[1]}")
            print(f"Assigned to:\t{line[0]}")
            print(f"Date Assigned:\t{line[3]}")
            print(f"Due date:\t{line[4]}")
            print(f"Task Complete?\t{line[5]}")
            print(f"Task description:\n  {line[2]}")    
            print("_"*80)


def view_mine():
    '''In this block you will put code the that will read the task from task.txt file and
    print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
    You can do it in this way:
    - Read a line from the file
    - Split the line where there is comma and space.
    - Check if the username of the person logged in is the same as the username you have
    read from the file.
    - If they are the same print it in the format of Output 2 in the task PDF'''
            
    while True:
        # Loading all lines from tasks.txt        
        with open('tasks.txt','r') as f:
            # Dictionary to store the tasks
            tasks = {}
            key = 1

            for line in f:

                line = line.split(", ")
                # stored in a dictionary
                tasks[key] = line
                key += 1

    

        # Displaying user's tasks
            for task in tasks :
                #if user_name same as logged in user , print relative tasks
                if tasks[task][0] == user_name:
                    print("_"*80)
                    print(f"Task number:\t {task}")             
                    print(f"Task name:\t{tasks[task][1]}")
                    print(f"Assigned to:\t{tasks[task][0]}")
                    print(f"Date Assigned:\t{tasks[task][3]}")
                    print(f"Due date:\t{tasks[task][4]}")
                    print(f"Task Complete?\t{tasks[task][5]}")
                    print(f"Task description:\n  {tasks[task][2]}")    
                    print("_"*80)

            # Input to get tas number from a user
            choice = int(input("Enter task number to edit or -1 to return: "))

            # If user enter negative number it will return to main menu        
            if choice < 0:            
                return 0       

            else :
                # To avoid user accessing the task assigned to different user 
                if tasks[choice][0] != user_name:
                    print("You have selected task not in your portfolio")
                    return 0 

                else:
                    # Displaying chosen task title    
                    print(f"You've chosen task {tasks[choice][1]}")
                    
                    # Only incomplete tasks can be edited 
                    if  tasks[choice][5] == 'Yes':
                        print("Task already completed you can't make any changes !")

                    else:
                        # Options to edit or mark    
                        edit = input("Please enter if you would like to 'mark' or 'edit ").lower()

                        if edit == 'mark':
                            tasks[choice][5] = "Yes"                   
                            print("Your task has been marked as complete")

                        elif edit == 'edit':
                            # Options to edit date or user
                            changes = input("Please enter if you would like to edit submission 'date' or 'user': ").lower()

                            if changes == 'date':
                                new_date = input("Please enter new date: ")
                                tasks[choice][4] = new_date
                                print("New date is assigned !")

                            elif changes  == 'user':
                                new_user = input("Please enter new users name: ")
                                tasks[choice][0] = new_user
                                print("New user assigned")
                                
                            # Error message for option to edit date or user    
                            else:
                                print("Invalid entry !")

                        # Error message for options to edit or mark    
                        else:
                            print("Invalid entry !")

                    # Overwriting updated varibales
                    with open("tasks.txt","w") as f:

                        for task in tasks:
                            f.write(", ".join(tasks[task]))
 

def generate_report():
    """This function will generate reports from user.txt and taskk.txt,
    then it will write into task_overview.txt and user_overview.txt
    """
    # Variables for user overview
    # Users dictionary will store usernames as a keys then store lists of tasks assigned for each user
    users = {}
    number_of_users = 0

    # Variables for task overview
    total_tasks = 0
    total_completed = 0
    total_uncompleted = 0
    overdue_tasks = 0
    overdue_uncompleted =0

    # Accessing users records
    with open('user.txt','r') as f:

        for line in f:
            # counting and initilizing keys in a dictionary
            number_of_users += 1
            line = line.split(", ")
            key = line[0]
            users[key] = []

    # Accessing tasks records
    with open('tasks.txt','r') as f:

        for line in f:

            line = line.split(", ")
            # Counting number of tasks
            total_tasks +=1
            due_date = line[4]
            # Variable to store completenes of the tasks 
            status = line[5].strip("\n")
            user = line[0]
            #Appending list to a list of tasks 
            users[user].append(line[1:])
            
            # Control flow for oberdue taskks
            if datetime.strptime(due_date,"%d %b %Y").date() < date.today():
                overdue_tasks+=1
                # if tasks overdue and still not completed
                if status == "No":
                    overdue_uncompleted +=1
            # If task completed
            if status == "Yes":
                total_completed += 1

            elif status == "No":
                total_uncompleted += 1
    #calculating precentage values        
    uncompleted_percent = round((total_uncompleted/total_tasks*100),2)
    overdue_percent = round((overdue_tasks/total_tasks*100),2)

    # Generating report into task_overview.txt
    with open("task_overview.txt","w") as f:
        f.write(f"Total tasks, {total_tasks}\n")
        f.write(f"Total completed tasks, {total_completed}\n")
        f.write(f"Total incomplete tasks, {total_uncompleted}, {uncompleted_percent}%\n")
        f.write(f"Overdue tasks, {overdue_tasks}, {overdue_percent}%\n")
        f.write(f"Overdue and incomplete, {overdue_uncompleted}\n")

    # Generating report into user_overview.txt
    with open("user_overview.txt","w") as f:

        # Writing over all report values
        f.write(f"Total number of users: {number_of_users}\n")
        f.write(f"Total tasks, {total_tasks}\n")

        # Writing  reoprt for each user
        for user in users:
            # values to count user tasks
            user_tasks=0
            user_completed=0
            user_overdue = 0

            f.write(f"Username: {user}, ")

            # Travesing through each tasks assigned to the user and counting variables
            for task in users[user]:
                user_tasks+=1

                if task[4]=="Yes\n":
                    user_completed+=1

                if datetime.strptime(task[3],"%d %b %Y").date()<date.today() and task[4] == "No\n":
                    user_overdue +=1    
            #calculating over tasks assigned to user
            assigned_percent=round((user_tasks/total_tasks*100),2)

            #if user has some tasks calculating the rest of required variables, 
            if user_tasks >0:
                user_completed_percent=round((user_completed/user_tasks*100),2)
                user_not_completed=user_tasks - user_completed
                user_not_completed_percent=round((user_not_completed/user_tasks*100),2)
                user_overdue_percent=round((user_overdue/user_tasks*100),2)

                f.write(f"Total Tasks: {user_tasks} {assigned_percent}%, ")
                f.write(f"Completed : {user_completed_percent}%, ")
                f.write(f"Not completed: {user_not_completed_percent}%, ")
                f.write(f"Overdue: {user_overdue_percent}%\n")

            # else, to avoid an error as dividing number by 0 not possible
            else:
                f.write(f"Total tasks: {user_tasks} \n")

def display_stats():
    """This function will print values from 
    task_overview.txt and user_overview.txt
    """
    
    print("_"*50)

    with open('task_overview.txt','r') as f:

        for line in f:

            line = line.split(", ")
            
            for value in line:
                print(value,end = "\t")
            # outer print to move to next line
            print("")

    print("_"*50)
           
    with open('user_overview.txt','r') as f:

        for line in f:
            line = line.split(", ")

            for value in line:
                print(value,end = "\t")

            print("")
        
    print("_"*50)

#program will read and store all authentication credetials on "login_auth"
login_auth = []
with open('user.txt','r') as f:
    for line in f:
        line=line.replace(",","").split()
        login_auth.append(line)

is_admin = False          #when entering user name it will establish if user is admin or not

is_authorised = False     #to establish entered credentials 

counter = 5               #counter to iterate attempts,user will have 4 attempts

while counter > 0:
    #User enters user name and password
    user_name = input("Enter your user name:  ")
    password = input("Enter your password: ")

    #comparing username with usernames in login_auth
    for username_auth,password_auth in login_auth:
         #if both username and password exists
        if user_name == username_auth and password == password_auth:
            #if user entered with admin credentials 
            if user_name == 'admin':
                is_admin = True

            
            is_authorised = True

            counter = 0       #to stop while loop

    #esle while loop will keep asking for another attempts
    if is_authorised == False:
        print(f"Invalid credentials you have {counter-1} attempts left ")
        
    counter -= 1

#if login was successful
if is_authorised:
    print("Login Successful!")

    while True:
        #presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        
        if is_admin:
            menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - view statistics
    e - Exit
    : ''').lower()
        else:
            menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

        if menu == 'r':
            
            #only admin can register new user
            if is_admin:
                reg_user()
            else:
                print("Access denied please login as admin! ")

        elif menu == 'a':
            
            add_task()    
        
        elif menu == 'va':
            
            view_all()

        elif menu == 'vm':
            
            view_mine()
        elif menu == 'gr':
            
            generate_report()

        elif menu == 'ds':
            
            #only admin can see stats
            if is_admin:
                
                display_stats()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
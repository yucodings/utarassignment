run = True

#mainpage
def mainloop():
    print("-" * 64)
    print("Welcome to the Test Management System")
    print("-" * 64)
    print("Please pick an option: ")
    print("[1] Setup")
    print("[2] Generate Test Paper")
    print("[3] Help")
    print("\n[E] Exit")
    select = input()

    if select == "1":
        setupmenu()

    elif select == "2":
        testpaper()

    elif select == "3":
        helpmenu()

    elif select == "E" or select == "e":
        print("Goodbye")
        exit()

    else:
        print("Error: Invalid Input\nPlease Try Again.")

#mainpage[1]
def setupmenu():
    print("-" * 64)
    print("Setup Menu")
    print("-" * 64)
    print("Please pick an option: ")
    print("[1] Student Menu")
    print("[2] Courses Menu")
    print("[3] Question Banks")
    print("[4] Test Dates")
    print("\n[E] Exit")
    select2 = input()

    if select2 == "1":
        studentmenu()

    elif select2 == "2":
        coursemenu()

    elif select2 == "3":
        questionbank()

    elif select2 == "4":
        testdate()

    elif select2 == "E" or select2 == "e":
        mainloop()

    else:
        print("Error: Invalid Input\nPlease Try Again.")

#mainpage[2]
def testpaper():
    print("-" * 64)
    print("Generate Student Test Paper")
    print("-" * 64)
 
    print(courseLst)
    #there is supposed to be a list of courses here from another menu but for now it will just be this line of text
    courseid = input("Enter Course ID or E to Exit: ")

    if courseid == "E" or "e":
        mainloop()

    else:
        print("itll do something")

#mainpage[3]
def helpmenu():
    print("-" * 64)
    print("Help Menu")
    print("-" * 64)
    #here need to print the use of help menu, no idea
    print("todo")

#setup[1]    
def studentmenu():
    studentlist()
    #need to add name, add id, add nric
    print("todo")
    
#setup[2]
def coursemenu():
    print("todo")

#setup[3]
def questionbank():
    print("todo")

#setup[4]
def testdate():
    print("todo")

#Student List
def studentlist():
    print("-" * 64)
    print("Student List")
    print("-" * 64)
    print("Student ID"," "*12,"Student Name"," "*27,"NRIC Number")
    print("-" * 64)
    #need to list from up to down(not sure)
    for i in range (len(stuId)):
        print(studId," "*3,studName," "*23,nric)
    print("-" * 64)


courseCode=[]
courseDes=[]
studId=[]
studName=[]
nric=[]

while run:
    mainloop()

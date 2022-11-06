import datetime
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# option variable is used as the users choice to exceute specific actions.
# append status is used as the users choice to execute code for updating the status of a ticket.
# the add variable is used to allow the user to enter new bugs until they choose to quit.
# the updatedStatus variable is currently being used for testing on how to append an updated 
# status to a file replacing what was already there.
option = "0"
appendStatus = "yes"
add = True
bug = []
updatedStatus = []
currentTime = datetime.datetime.now()

# This function adds the lines added by the user to the empty list defined above called list[].
# It also appends a ticket number and the current date and time which is not entered by the user.
def AddToList():
    file = open("bugs.txt", 'r+')
    ticket_num = len(file.readlines()) + 1
    bug.insert(0, str(ticket_num))
    bug.append(currentTime.strftime("%x"))
    bug.append(currentTime.strftime("%X"))
    bug.append(name)
    bug.append(details)
    bug.append(severity)
    bug.append(status)

# This function takes the contents of the list above and writes it to a file called 'bugs.txt'.
def WriteToFile():
    file = open("bugs.txt", 'a')
    file.write(", ".join(bug) + "\n")
    file.close()
    bug.clear()

# This function reads lines from the file and prints them.
def ReadFile():
    file = open("bugs.txt, 'r")
    for element in file:
        print("\n" + element)

# This while loop ensures the user will repeated be asked what they would like to do after each action, giving them the option
# quit when they are ready.
while option != "3":
    option = input("What would you like to do?\n 1. Enter a new bug\n 2. Retrieve an old bug\n 3. Quit\n"  )

    # If the user chooses to enter a new bug they will enter the loop below. The outcome will add their bug to the list,
    # Show them their ticket number and write it to the file.
    if option == "1":
        while add == True:
            name = input("\n Please enter a name for the bug: ")
            details = input("Please enter the details of the bug: ")
            status = "pending"
            severity = input("what is the impact of the bug? (Low, Moderate, High): ").lower()
            if severity in ["low", "moderate", "high"]:
                add = True
                AddToList()
                print("Your ticket number is: " + str(bug[0]))
                print("Please keep note of it as you will need it to retrieve the ticket later\n")
                WriteToFile()
            
            # If they do not make a valid selection this error message is displayed and they are asked again what they 
            # would like to do.
            else:
                print("Invalid option")

            # This block of code allows the user to choose whether to add more than one bug at a time.
            answer = input("Would you like to enter another bug? (Yes/No): ").lower()
            if answer in ["yes"]:
                add = True
            elif answer in ["no"]:
                add == False
                break
        print("Your bug(s) have been saved, thank you")

    # If the user chooses retrieve an old bug, they can do so by entering their ticket number and having it read from the file
    # and printed for them.
    elif option == "2":
        file = open("bugs.txt" , "r")     
        ticket_num = int(input("Please enter your ticket number: "))
        ticket_num -= 1
        bug = file.readlines()[ticket_num].split(", ")
        updatedStatus.append(bug)
        print(updatedStatus)

        # This section currently does not work but I am trying to allow the user to update the current status of the ticket
        # they have retrieved. I am trying to read the ticket, replace the old status with the new one and then replace this 
        # line in the file so that only the ticket is updated.
        while appendStatus == "yes":
            appendStatus = input("Would you like to update the status? Yes/No: ").lower()
            if appendStatus == "yes":
                newStatus = input("What is the updated status? (In progress, Resolved or Pending?: \n").lower()
                if newStatus in ["in progress"]:
                    updatedStatus.pop()
                    updatedStatus.append(newStatus)
                    print(bug)

            # If the user does not make a valid selection this error message is displayed and they are asked again what they 
            # would like to do.
            else:
                print("Invalid option")

    # If the user selects option 3 then the program will end
    elif option == "3":
        break
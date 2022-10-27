import datetime
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

option = "0"
appendStatus = "yes"
add = True
bug = []
updatedStatus = []
currentTime = datetime.datetime.now()

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
def WriteToFile():
    file = open("bugs.txt", 'a')
    file.write(", ".join(bug))
    file.write("\n")
    file.close()
    bug.clear()
def ReadFile():
    file = open("bugs.txt", 'r')
    for element in file:
        print("\n" + element)
    file.close()

while option != "3":
    option = input("What would you like to do?\n 1. Enter a new bug\n 2. Retrieve an old bug\n 3. Quit\n"  )

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
            else:
                print("Invalid option")

            answer = input("Would you like to enter another bug? (Yes/No): ").lower()
            if answer in ["yes"]:
                add = True
            elif answer in ["no"]:
                add == False
                break
        print("Your bug(s) have been saved, thank you")

    elif option == "2":
        file = open("bugs.txt", 'r')
        ticket_num = int(input("Please enter your ticket number: "))
        ticket_num -= 1
        bug = file.readlines()[ticket_num]
        updatedStatus.append(bug)
        print(updatedStatus)

        while appendStatus == "yes":
            appendStatus = input("Would you like to update the status? Yes/No: ").lower()
            if appendStatus == "yes":
                newStatus = input("What is the updated status? (In progress, Resolved or Pending?: \n").lower()
                if newStatus in ["in progress"]:
                    updatedStatus.remove("pending")
                    updatedStatus.append(newStatus)
                    print(bug)

            else:
                print("Invalid option")

    elif option == "3":
        break
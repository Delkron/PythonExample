'''Docstring
Documentation'''
__author__ = 'David Fensling'
__version__ = '1.5'
__date__ = '26/06/2023'

global exiting
import json #This allows the program to understand which format it is using

import time #Lets the program use the terminal's set Time for any time-based functions (I used mine to let it pause and say a farewell at the end)

patients = [] #The initial variable that will be used to load the .json list

patients_file=open("patients.json", "r") #This opens the json and reads the filecontents into the variable. to read a file means to look, not touch, the data
patients = json.load(patients_file) #This saves the contents of the json list variable to the initial variable we made before
patients_file.close() #This closes the variable that the json file was opened in, preventing it from being mistakenly altered.

patients.sort() #This sorts the file alphabetically by the patient's Last Names

def entry_menu(): #This is the Entry Menu layout that will be referenced for the main program down lower
    print('''
SIT Data Entry Menu
==========================
1:  Print Patients' List
2:  Add Patient
3:  Delete Patient
4:  Exit
==========================
''')




def option_one(): #This option lists the Patients and gives them a Patient number index. Larger lists will have larger variables and better search options
    patient_number = 1
    for patient in patients:
        print(str(patient_number) + " " + patient)
        patient_number += 1
    print()
    print("Total number of registered patients is ", len(patients)) 

def option_two(): #This option adds a patient to the list, checks if they're already in there or not, then sorts them in if they're added
    print("Enter new Patient -> Lastname Firstname :")
    new_patient = input("Lastname Firstname: ")
    if new_patient in patients:
        print("Patient is already in the list")
    else:
        print("Patient is not in the list, would you like to add them?")
        print('''
========
1: Yes
2: No
========
''')
        answer = input()
        if answer == "1":
            patients.append(new_patient)
            print("Patient has been added to the list")
            patients.sort()
            patient_number = 1
            for patient in patients:
                print(str(patient_number) + " " + patient)
                patient_number += 1
            print()
            print("Total number of registered patients is ", len(patients))
        elif answer == "2":
            None
        else:
            print("Please select a valid answer!")

def option_three(): #This option allows a user to delete a patient from the list using their corrosponding Patient Number in the list
    patient_number = 1
    for patient in patients:
        print(str(patient_number) + " " + patient)
        patient_number += 1
    print("which patient would you like to remove?")
    patient_number_to_delete  = int(input())
    print("Are you sure you want to remove this patient from the list?")
    print('''
========
1: Yes
2: No
========
''')
    answer = input()
    if answer == "1":
        del patients[patient_number_to_delete - 1]
        print("Patient has been removed from the list")
        patients.sort()
        patient_number = 1
        for patient in patients:
            print(str(patient_number) + " " + patient)
            patient_number += 1
        print()
        print("Total number of registered patients is ", len(patients))
    elif answer == "2":
        None
    else:
        print("Please select a valid answer")

#This is the Exit option, and put last as it is the final of the list. It confirms if the user wishes to quit, and saves the altered list to the json after opening it with "w" or Write
def option_four():
    global exiting
    print("Are you sure, you want to quit?")
    print('''
========
1: Yes
2: No
========
''')
    exit_answer = None
    while exit_answer not in (1, 2):
        exit_answer = int(input("> "))
        if exit_answer == 1:
            patients_file = open("patients.json", "w")
            json.dump(patients, patients_file)#"Dumps" the altered list within the initial value into the re-opened and writable json, closing it afterwards and "saving" the changes
            patients_file.close()
            time.sleep(2)
            print("Patients File Saved!")
            print()
            print("Have a nice day!")
            exiting = True
        elif exit_answer == 2:
            pass
        else:
            print("Please select a valid option")
        

while 1: #This is the main part of the Program where the menu's functionality is utilized. The While loop continues perpetually until you exit the program. The defined Functions are activated down here
    entry_menu()
    exiting = False
    menu_selection = input()

    if menu_selection == "1":
        option_one()
    elif menu_selection == "2":
        option_two()
    elif menu_selection == "3":
        option_three()
    elif menu_selection == "4": 
        option_four()
        if exiting:
            break #Turns off the Program
    else:
        print("Please select a valid option")

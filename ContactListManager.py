'''Program to manages contact list using a dictionary.
The program will ask for the user's name and it will be the key and phone number to be a valur
User will be able to  perform the following functions:
Add contact
update contact
Delete conctact
Exit the program.
'''
# Create an empty dictionary
contacts = {}

#Function to add the a new user
def add_contact():
    # Ask the user for name input
    name = input('Enter your name: ')
    phoneNo = int(input('Enter your phone number: '))


    contacts[name] = phoneNo
    print("Contact succesfully added!")

#Function to search for number using the name
def search_contact():
    name = input('Enter your name: ')

    #check the name is there and print with contact.
    if name in contacts:
        print(name,"phone number is : ",contacts[name])
    else:
        print("User not found.")

#Function to update the phone number of the user
def update_contact():
    name = input('Enter your name: ')

    #check if the name is in the dictionary using if statement.
    if name in  contacts:

        phoneNo = int(input('Enter your current phone number: '))
        contacts.update({name:phoneNo})
        print(name,"Your updated phone number is :", contacts[name])

    else:
        print("User not found")

#function to delete the users contact in the dictionary
def delete_contact():

    name = input('Enter your name: ')

    #Find the contact in the deictionary and delete.
    if name in contacts:

        #Method to delete
        del contacts[name]
        print("Contact succesfully deleted",contacts)
    else:
        print("User not found")

#Function to view contacts in the contact list
def view_contacts():
    print("\n****** Contact list ******")
    print('Name: ',end="")
    print("\tPhone Number: ")
    for name, phoneNo in contacts.items():
        print(name, end="")
        print('\t',phoneNo)

#Loop
for menu in range(1,7):
    print("********** Contact list Manager **********")
    # Display the menu for the user to choose
    menu = int(input(" Choose the menu:\n 1 : Add contact\n 2 : Search contact\n 3 : Update contact\n 4 : Delete contact\n 5 : View all contacts\n 6 : Exit the program\n Enter your choice: "))

    # use the if statement to execute the user choice.
    if menu== 1:
        add_contact()
    elif menu == 2:
        search_contact()

    elif menu == 3:
        update_contact()

    elif menu == 4:
        delete_contact()

    elif menu == 5:
        view_contacts()

    elif menu == 6:
        print("Succesful exit!")
        break
    else:
        print("Invalid choice. Please try again.")



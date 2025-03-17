#1 Course Information
# room_number = {
#     "CSI101": 3004,
#     "CSI102": 4501,
#     "CSI103": 6755,
#     "NT110": 1244,
#     "CM241": 1411
# }

# instructor = {
#     "CSI101": "Haynes",
#     "CSI102": "Alvarado",
#     "CSI103": "Rich",
#     "NT110": "Burke",
#     "CM241": "Lee"
# }

# meeting_time = {
#     "CSI101": "8:00 a.m.",
#     "CSI102": "9:00 a.m.",
#     "CSI103": "10:00 a.m.",
#     "NT110": "11:00 a.m.",
#     "CM241": "1:00 p.m."
# }

# user_input = input("Enter a course number: ").upper()

# if user_input not in room_number:
#     print("Course Number is invalid")
# else:
#     print(f"Room Number: {room_number[user_input]}")
#     print(f"Instructor: {instructor[user_input]}")
#     print(f"Meeting time: {meeting_time[user_input]}")

#2 Capital Quiz
# def main():
#    sc = {
#     "Alabama": "Montgomery",
#     "Alaska": "Juneau",
#     "Arizona": "Phoenix",
#     "Arkansas": "Little Rock",
#     "California": "Sacramento",
#     "Colorado": "Denver",
#     "Connecticut": "Hartford",
#     "Delaware": "Dover",
#     "Florida": "Tallahassee",
#     "Georgia": "Atlanta",
#     "Hawaii": "Honolulu",
#     "Idaho": "Boise",
#     "Illinois": "Springfield",
#     "Indiana": "Indianapolis",
#     "Iowa": "Des Moines",
#     "Kansas": "Topeka",
#     "Kentucky": "Frankfort",
#     "Louisiana": "Baton Rouge",
#     "Maine": "Augusta",
#     "Maryland": "Annapolis",
#     "Massachusetts": "Boston",
#     "Michigan": "Lansing",
#     "Minnesota": "Saint Paul",
#     "Mississippi": "Jackson",
#     "Missouri": "Jefferson City",
#     "Montana": "Helena",
#     "Nebraska": "Lincoln",
#     "Nevada": "Carson City",
#     "New Hampshire": "Concord",
#     "New Jersey": "Trenton",
#     "New Mexico": "Santa Fe",
#     "New York": "Albany",
#     "North Carolina": "Raleigh",
#     "North Dakota": "Bismarck",
#     "Ohio": "Columbus",
#     "Oklahoma": "Oklahoma City",
#     "Oregon": "Salem",
#     "Pennsylvania": "Harrisburg",
#     "Rhode Island": "Providence",
#     "South Carolina": "Columbia",
#     "South Dakota": "Pierre",
#     "Tennessee": "Nashville",
#     "Texas": "Austin",
#     "Utah": "Salt Lake City",
#     "Vermont": "Montpelier",
#     "Virginia": "Richmond",
#     "Washington": "Olympia",
#     "West Virginia": "Charleston",
#     "Wisconsin": "Madison",
#     "Wyoming": "Cheyenne"
# }

#    state_capitals(sc)

# def state_capitals(sc):
#     correct = 0
#     incorrect = 0
#     while True:
#         for state,capital in sc.items():
#             print(f"Enter the capital for {state}")
#             user_input = input().lower()
#             if user_input == "end":
#                 print(f"You got {correct} correct and {incorrect} incorrect. ")
#                 return
#             elif user_input == capital.lower():
#                 print("correct!")
#                 correct += 1
#             else:
#                 print("incorrect!")
#                 incorrect += 1
# main()

#8 Names and Email Addresses
import pickle

def load_data():
    try:
        with open("contacts.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("No existing contact file found. Starting with an empty list.")
        return {}

def save_contacts(contacts):
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contacts, file)


def data_menu():
    print("Menu:")
    print("1. Search email address: ")
    print("2. Create new contact: ")
    print("3. Update an email address: ")
    print("4. Delete a contact: ")
    print("Exit")

def search_contact(contacts):
    name = input("Enter a name: ")
    if name not in contacts:
        print("Contact doesn't exist.")
    else:
        print(f"{name}'s email: {contacts.get(name)}")

def create_contact(contacts):
    name = input("Enter a name: ")
    if name not in contacts:
        email = input("Enter a new email: ")
        contacts[name] = email
    else:
        print("This contact already exists.")

def update_contact(contacts):
    name = input("Enter a name to update: ")
    if name not in contacts:
        print("Contact doesn't exist")
    else:
        email = input("Enter the new email: ")
        contacts[name] = email
        print("Email updated.")

def delete_contact(contacts):
    name = input("Enter a name: ")
    if name not in contacts:
        print("Contact doesn't exist.")
    else:
        del contacts[name]
        print("Contact deleted")
    

def main():
    contacts = load_data()
    while True:
        data_menu()
        option = input("Enter option 1-4(enter exit to leave): ").lower()
        if option == "exit":
            save_contacts(contacts)
            print("Data saved. Bye!")
            break
        elif option == "1":
            search_contact(contacts)
        elif option == "2":
            create_contact(contacts)
        elif option == "3":
            update_contact(contacts)
        elif option == "4":
            delete_contact(contacts)
        else:
            print("invalid option.. Try again.")

main()



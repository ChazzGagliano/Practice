#3 Date Printer

# def main():
#     date = input("Enter a date in the form (dd/mm/yyyy): ")
#     date_function(date)

# def date_function(date):
#     if date[:2] == "01":
#         print("January", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "02":
#         print("February", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "03":
#         print("March", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "04":
#         print("April", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "05":
#         print("May", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "06":
#         print("June", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "07":
#         print("July", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "08":
#         print("August", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "09":
#         print("September", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "10":
#         print("October", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "11":
#         print("November", f"{date[3:5]}," , date[6:])
#     elif date[:2] == "12":
#         print("December", f"{date[3:5]}," , date[6:])
        
# main()

#12 Pig Latin
def main():
    sentence = str(input("Enter a sentence: ")).split()
    pig_latin(sentence)

def pig_latin(sentence):
    for i in sentence:
        print(i[1:] + i[0] + "ay",  end = " ")

main()
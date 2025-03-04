#3 Date Printer
def main():
    date = input("Enter a date in (mm-dd-yyyy) format: ").split("-")
    array = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = int(date[0])
    print(f"{array[month - 1]} {date[1]}, {date[2]}")
main()



# 12 Pig Latin
def main():
    sentence = input("Enter a sentence: ").split()
    pig_latin(sentence)
    
def pig_latin(sentence):
    for i in sentence:
        print(i[1:] + i[0] + "ay", end = ' ')
main()


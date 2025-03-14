#1 Course Information
room_number = {
    "CSI101": 3004,
    "CSI102": 4501,
    "CSI103": 6755,
    "NT110": 1244,
    "CM241": 1411
}

instructor = {
    "CSI101": "Haynes",
    "CSI102": "Alvarado",
    "CSI103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

meeting_time = {
    "CSI101": "8:00 a.m.",
    "CSI102": "9:00 a.m.",
    "CSI103": "10:00 a.m.",
    "NT110": "11:00 a.m.",
    "CM241": "1:00 p.m."
}

user_input = input("Enter a course number: ").upper()

if user_input not in room_number:
    print("Course Number is invalid")
else:
    print(f"Room Number: {room_number[user_input]}")
    print(f"Instructor: {instructor[user_input]}")
    print(f"Meeting time: {meeting_time[user_input]}")
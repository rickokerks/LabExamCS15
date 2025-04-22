#Accept student names and course programs then show total students per program


university_programs = [
    {"program_name": "Computer Science", "num_students": 0},
    {"program_name": "Information Technology", "num_students": 0},
    {"program_name": "Software Engineering", "num_students": 0},
    {"program_name": "Data Science", "num_students": 0},
    {"program_name": "Cybersecurity", "num_students": 0},
    {"program_name": "Artificial Intelligence", "num_students": 0},
    {"program_name": "Business Administration", "num_students": 0},
    {"program_name": "Marketing", "num_students": 240},
    {"program_name": "Finance", "num_students": 320},
    {"program_name": "Accounting", "num_students": 310},
    {"program_name": "Economics", "num_students": 270},
    {"program_name": "Entrepreneurship", "num_students": 180},
    {"program_name": "Human Resource Management", "num_students": 210},
    {"program_name": "Mechanical Engineering", "num_students": 360},
    {"program_name": "Electrical Engineering", "num_students": 340},
    {"program_name": "Civil Engineering", "num_students": 330},
    {"program_name": "Chemical Engineering", "num_students": 190},
    {"program_name": "Industrial Engineering", "num_students": 220},
    {"program_name": "Architecture", "num_students": 280},
    {"program_name": "Interior Design", "num_students": 130},
    {"program_name": "Law", "num_students": 400},
    {"program_name": "Political Science", "num_students": 210},
    {"program_name": "Psychology", "num_students": 350},
    {"program_name": "Sociology", "num_students": 160},
    {"program_name": "Social Work", "num_students": 140},
    {"program_name": "Education", "num_students": 460},
    {"program_name": "Elementary Education", "num_students": 250},
    {"program_name": "Secondary Education", "num_students": 240},
    {"program_name": "Early Childhood Education", "num_students": 200},
    {"program_name": "Biology", "num_students": 310},
    {"program_name": "Chemistry", "num_students": 230},
    {"program_name": "Physics", "num_students": 210},
    {"program_name": "Mathematics", "num_students": 220},
    {"program_name": "Environmental Science", "num_students": 190},
    {"program_name": "Nursing", "num_students": 430},
    {"program_name": "Medical Technology", "num_students": 280},
    {"program_name": "Pharmacy", "num_students": 310},
    {"program_name": "Public Health", "num_students": 170},
    {"program_name": "Nutrition and Dietetics", "num_students": 150},
    {"program_name": "Physical Therapy", "num_students": 160},
    {"program_name": "Occupational Therapy", "num_students": 120},
    {"program_name": "Mass Communication", "num_students": 190},
    {"program_name": "Journalism", "num_students": 170},
    {"program_name": "Film and Media Studies", "num_students": 160},
    {"program_name": "Fine Arts", "num_students": 140},
    {"program_name": "Music", "num_students": 130},
    {"program_name": "Theater Arts", "num_students": 120},
    {"program_name": "Philosophy", "num_students": 100},
    {"program_name": "History", "num_students": 110},
    {"program_name": "English Literature", "num_students": 200},
    {"program_name": "Linguistics", "num_students": 130},
    {"program_name": "International Relations", "num_students": 180},
    {"program_name": "Tourism Management", "num_students": 260},
    {"program_name": "Hospitality Management", "num_students": 240},
    {"program_name": "Criminology", "num_students": 300},
    {"program_name": "Maritime Studies", "num_students": 150},
    {"program_name": "Aviation Management", "num_students": 120},
    {"program_name": "Library and Information Science", "num_students": 100},
    {"program_name": "Statistics", "num_students": 180},
    {"program_name": "Geology", "num_students": 110},
    {"program_name": "Anthropology", "num_students": 90},
    {"program_name": "Agriculture", "num_students": 200},
    {"program_name": "Forestry", "num_students": 150},
    {"program_name": "Veterinary Medicine", "num_students": 170},
    {"program_name": "Urban Planning", "num_students": 120},
    {"program_name": "Fashion Design", "num_students": 140},
    {"program_name": "Game Development", "num_students": 160}
]




loop = True

while loop:
    print("-----------STUDENT ENROLLMENT SYSTEM-----------")
    print("[1] Progarams")
    print("[2] Enroll")
    print("[3] Exit")

    program()

    choice = input()

    match choice:
        case 1:
            program()
        case 2:
            enroll()
        case 3:
            break
        case _:
            print("Invalid choice!")

    


    conEnroll = input("Do you want to enroll? [Y|N]").strip().lower()
    if conEnroll == "n":
        break


def program():
    matches = []
    programI = input("Enter progam:")
    matches = [program for program in university_programs if programI in program["program_name"].lower()]
    if matches:
        print("Program: " + str(matches[0]["program_name"]))
        print("Enrolled: " + str(matches[0]['num_students']))

def enroll():
    firstname = input("First name: ")
    lastname = input("Last name: ")
    matches = []

    while not matches:
        course = input("Course program: ").strip().lower()
        matches = [program for program in university_programs if course in program['program_name'].lower()]
        if not matches:
            print('Invalid program!')
        
    if matches: 
        numStudents = matches[0]['num_students'] + 1
        matches[0]['num_students'] = numStudents
        print('Successfully enrolled with BS in ' + str(matches[0]['program_name']))
        if numStudents == 1:
            print(str(matches[0]['num_students']) + " student is currently enrolled.")
        else:
            print(str(matches[0]['num_students']) + " students are currently enrolled.")
        
    
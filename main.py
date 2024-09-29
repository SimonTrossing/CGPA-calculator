def get_courses():
    while True:
        try:
            courses = int(input("How many courses do you take?"))
            break
        except ValueError:
            print("it needs to be a non-decimal number")
    courses_dict = {}
    for i in range(courses):
        course = input(f"what is your {i+1} course?")
        while True:
            try:
                grade = int(input(f"What was your grade in {course}?"))
                break
            except ValueError:
                print("it needs to be a non-decimal number")
        courses_dict.update({course:grade})
    return courses_dict


def calculator(grades):
    courses = list(grades.keys())
    GPA = 0
    for i in range(len(courses)):
        GPA += grades[courses[i]]
    GPA = GPA/len(courses)
    return GPA


def weaklink(grades):
    sorted_grades = sorted(grades)
    return grades[sorted_grades[0]], sorted_grades[0]


def main():
    print(weaklink(get_courses()))
    print(f"your GPA is {calculator(get_courses())}")
    
main()


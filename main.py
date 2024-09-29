def get_courses():
    courses = int(input("How many courses do you take?"))
    courses_dict = {}
    for i in range(courses):
        course = input(f"what is your {i+1} course?")
        grade = int(input(f"What was your grade in {course}?"))
        courses_dict.update({course:grade})
    return courses_dict

def calculator(grades):
    courses = list(grades.keys())
    GPA = 0
    for i in range(len(courses)):
        GPA += grades[courses[i]]
    GPA = GPA/len(courses)
    return GPA


    
    


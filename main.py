def courrses():
    courses = int(input("How many courses do you take?"))
    courses_dict = {}
    for i in range(courses):
        course = input(f"what is your {i+1} course?")
        grade = input(f"What was your grade in {course}?")
        courses_dict.update({course:grade})
    return courses_dict
    


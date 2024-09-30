class GPA_calc:
    def __init__(self):
        self.grades = self.get_courses()
        self.grade_score = {"A+":4,"A":4,"A-":3.7,"B+":3.3,"B":3,"B-":2.7,"C+":2.3,"C":2,"C-":1.7,"D+":1.3,"D":1,"F":0}

    def get_courses(self):
        while True:
            try:
                courses = int(input("How many courses do you take?"))
                break
            except ValueError:
                print("it needs to be a non-decimal number")
        courses_dict = {}
        for i in range(courses):
            course = input(f"what is your {i+1} course?")
            grade = input(f"What was your grade in {course}?")
            courses_dict.update({course:grade})
        return courses_dict


    def calculator(self):
        courses = list(self.grades.keys())
        GPA = 0
        for i in range(len(courses)):
            GPA += self.grade_score[self.grades[courses[i]]]
        GPA = GPA/len(courses)
        return GPA


    def weaklink(self):
        sorted_grades = sorted(self.grades.keys())
        return self.grades[sorted_grades[-1]], sorted_grades[-1]


def main():
    my_GPA_calc = GPA_calc()
    grade, subject = my_GPA_calc.weaklink()
    print(f"your Weakest subject was {subject} with a {grade}")
    print(f"your GPA is {my_GPA_calc.calculator()}")
main()


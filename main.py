class GPA_calc:
    def __init__(self):
        self.grades = self.get_courses()

    def get_courses(slef):
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


    def calculator(self):
        courses = list(self.grades.keys())
        GPA = 0
        for i in range(len(courses)):
            GPA += self.grades[courses[i]]
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


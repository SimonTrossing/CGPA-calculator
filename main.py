class GPA_calc:
    def __init__(self):
        self.courses = []
        self.grade_score = {"A+":4,"A":4,"A-":3.7,"B+":3.3,"B":3,"B-":2.7,"C+":2.3,"C":2,"C-":1.7,"D+":1.3,"D":1,"F":0}
        self.grades = self.get_courses()
       
       

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
            self.courses.append(course)
            grade = ""
            while grade not in self.grade_score.keys(): 
                grade = input(f"What was your grade in {course}?")
            courses_dict.update({course:grade})
        return courses_dict


    def calculator(self):
        GPA = 0
        for i in range(len(self.courses)):
            GPA += self.grade_score[self.grades[self.courses[i]]]
        GPA = GPA/len(self.courses)
        return round(GPA,2)
    

    def weakpoint(self):
        lowest_grade_point = 100
        for i in range(len(self.courses)):
            if self.grade_score[self.grades[self.courses[i]]]<lowest_grade_point:
                lowest_grade_point = self.grade_score[self.grades[self.courses[i]]]
                lowest_grade = self.grades[self.courses[i]]
                lowest_subject = self.courses[i]
        return lowest_grade, lowest_subject
    

def main():
    my_GPA_calc = GPA_calc()
    grade, subject = my_GPA_calc.weakpoint()
    print(f"your GPA is {my_GPA_calc.calculator()}")
    print(f"your weakpint is {subject} in which you got {grade}")
main()


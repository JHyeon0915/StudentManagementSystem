import pandas as pd

class CS22B:
    students = []
    assignments = []
    exams = []
    teamprojects = []

    def __init__(self, prof, data):
        self.prof = prof
        self.data = data
    
    def showAllData(self):
        print(self.data)
    
    def showSomeData(self, column_name):
        print(self.data[column_name])

    def createTeamProject(self, title, duedate, full_grade, student_names):
        teammates = [i for i in self.students for j in student_names if i.getName == j]
        t = TeamProject(title, duedate, full_grade, teammates)
        self.teamprojects.append(t)
    
    def getAverage(self,exam_type):
        avg = float(map(sum, [i for i in self.students.getGrade(exam_type)]))
        return avg

    def updateAssignmentGrade(self, student_name, number, new_grade):           # implementing in need
        self.assignments[number]


    def updateExamGrade(self, student_name, kind, new_grade):
        student_name = student_name.split(" ")
        if kind == "final":
            self.data.loc[self.data.first_name == student_name[0] and self.data.last_name == student_name[1], "final"] = new_grade
        else:
            self.data.loc[self.data.first_name == student_name[0] and self.data.last_name == student_name[1], "midterm"] = new_grade

    def updateTeamprojectGrade(self, teamname, new_grade):
        self.data.loc[self.data.team_name == teamname, "team_project"] = new_grade


class Student:
    classes = []

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def getName(self):
        return self.name
    
    def enroll(self, class_object):
        self.classes.append(class_object)

    def getGrade(self, exam_type):
        return exam_type
    
class Assignment:
    def __init__(self, title, duedate, full_grade):
        self.title = title
        self.duedate = duedate
        self.full_grade = full_grade

class TeamProject(Assignment):
    def __init__(self, title, duedate, full_grade, students):
        self.teammates = students
        super().__init__(title, duedate, full_grade)


class Exam:
    def __init__(self, kind, date, grade):
        self.kind = kind
        self.date = date
        self.full_grade = grade


def makeData(filename):
    try:
        d = pd.read_csv(filename, encoding='utf-8')
        print("File succesfully uploaded!")
    except NameError:
        print("The file does not exist.")

    return d

data = makeData(input("Type file name: "))
myclass = CS22B(input("Professor name: "),data)

DEFAULT = "What do you want to do? Choose and enter a number\n1) show all data\n2) search a data\n 3) update exam grade\n 4) update assignment grade\n 5) update team project grade\n 6) exit\n"


while(1):
    answer = input(DEFAULT)
    if answer == "1":
        myclass.showAllData()

    elif answer == "2":
        column_name = input("What column of data would you like to see?: ")
        myclass.showSomeData(column_name)

    elif answer == "3":
        exam_type = input("What type of exam grade would you like to update? (final / midterm): ")      # future concern: when there are multiple finals or midterms
        student_name = input("Who would you like to update a grade for?: ")         # future concern: when i wanna choice multiple student.
        new_grade = input("What would be the new grade?: ")
        myclass.updateExamGrade(student_name, exam_type, int(new_grade))

    elif answer == "4":
        assignment_type = input("What type of assignment grade would you like to update? Type an integer number: ")
        student_name = input("Who would you like to update a grade for?: ")
        new_grade = input("What would be the new grade?: ")
        myclass.updateExamGrade(student_name, assignment_type, int(new_grade))

    elif answer == "5":
        student_name = input("What team would you like to update a grade for?: ")
        new_grade = input("What would be the new grade?: ")
        myclass.updateTeamprojectGrade()
        
    elif answer=="6":
        print("Thank you for using this program! See you again!")
        break





import pandas as pd

class CS22B:
    students = []
    def __init__(self, prof, data):
        self.prof = prof
        self.data = data
        self.head = data.readlines()[0]

        for line in data.readlines()[1:]:             # future concern: no function to adjust along the column name
            line = line.strip().split(",")
            self.students.append(Student(id = line[0], name = line[1], midterm = line[2], final = line[3], ass1 = line[4], ass2 = line[5], ass3 = line[6], team_name = line[7], teamproject_grade=line[8]))

    def rewrite(self):
        self.data = []
        self.data.append(self.head)

        for s in self.students:
            self.data.append([s.getId(), s.getName(), s.getExamGrade("midterm"), s.getExamGrade("final"), s.getAssignmentGrade("ass1"),s.getAssignmentGrade("ass2"),s.getAssignmentGrade("ass3"),s.getTeamName(), s.getTeamGrade()])

    def showAllData(self):
        self.rewrite()
        print(self.data)
    
    def showSomeData(self, column_name):
        if column_name == "midterm" or column_name == "final":
            for student in self.students:
                print(student.getName() + ": " + student.getExamGrade(column_name))
        elif "ass" in column_name:
            for student in self.students:
                print(student.getName() + ": " + student.getAssignmentGrade(column_name))
        else:
            for student in self.students:
                print(student.getName() + ": " + student.getTeamprojectGrade())
    
    def getExamAverage(self,exam_type):
        avg = float(map(sum, [i.getExamGrade(exam_type) for i in self.students]))
        return avg
    
    def getAssignmentAverage(self, ass_title):
        avg = float(map(sum, [i.getAssignemntGrade(ass_title) for i in self.students]))
        return avg

    def updateAssignmentGrade(self, student_name, number, new_grade):
        ass_name = "ass"+number
        for student in self.students:
            if student.getName() == student_name:
                student.setAssignmentGrade(ass_name, new_grade)
                break


    def updateExamGrade(self, student_name, exam_type, new_grade):
        for student in self.students:
            if student.getName() == student_name:
                student.setExamGrade(exam_type, new_grade)
                print("Successfully updated!")
                break
        print("Couldn't update information. Try again.")


    def updateTeamprojectGrade(self, teamname, new_grade):
        for student in self.students:
            if student.getTeamProjectName() == teamname:
                student.setTeamGrade(new_grade)
                break


class Student:
    assignments = []
    def __init__(self, name, id, midterm, final, ass1, ass2, ass3, teamproject_grade, team_name):
        self.name = name
        self.id = id
        self.midterm = Exam("midterm", midterm)
        self.final = Exam("final", final)

        self.assignments.append(Assignment("ass1", ass1))
        self.assignments.append(Assignment("ass2", ass2))
        self.assignments.append(Assignment("ass3", ass3))

        self.teamproject = TeamProject(team_name, teamproject_grade)
    
    def getName(self):
        return self.name

    def getAssignmentGrade(self, ass_title):
        if "1" in ass_title:
            return self.assignments[0].getGrade()
        elif "2" in ass_title:
            return self.assignments[1].getGrade()
        elif "3" in ass_title:
            return self.assignments[2].getGrade()

    def setAssignmentGrade(self, ass_title, new_grade):
        for ass in self.assignments:
            if ass.getTitle() == ass_title:
                ass.setGrade(new_grade)

    def getExamGrade(self, kind):
        if kind == "midterm" or kind == "final":
            return self.midter.getGrade() if kind == "midterm" else self.final.getGrade()

    def setExamGrade(self, exam_type, new_grade):
        if exam_type == "midterm":
            self.midterm = new_grade
        else:
            self.final = new_grade
    
    def getTeamProjectName(self):
        return self.teamproject.getTeamName()
    
    def getTeamprojectGrade(self):
        return self.teamproject.getTeamGrade()

    def setTeamGrade(self, new_grade):
        self.teamproject.getTeamGrade = new_grade

class Assignment:
    def __init__(self, title, grade):
        self.title = title
        self.grade = grade

    def getTitle(self):
        return self.title
    
    def getGrade(self):
        return self.grade

    def setGrade(self, new_grade):
        self.grade = new_grade

class TeamProject:
    def __init__(self, team_name, grade):
        self.team_name = team_name
        self.grade = grade

    def getTeamName(self):
        return self.team_name
    
    def getTeamGrade(self):
        return self.team_grade


class Exam:
    def __init__(self, exam_type, grade):
        self.kind = exam_type
        self.grade = grade

    def setFullGrade(self, full_grade):
        self.full_grade = full_grade

    def getFullGrade(self):
        return self.full_grade


def getData(filename):
    try:
        d = open(filename, "r")
        print("File succesfully uploaded!")
    except NameError:
        print("The file does not exist.")

    return d

DEFAULT = "What do you want to do? Choose and enter a number\n1) show all data\n2) search a data\n3) update exam grade\n4) update assignment grade\n5) update team project grade\n6) exit\n"


data = getData(input("Type file name: "))
myclass = CS22B(input("Professor name: "),data)

while(1):
    answer = input(DEFAULT)
    if answer == "1":
        myclass.showAllData()

    elif answer == "2":
        column_name = input("What column of data would you like to see?: ")
        myclass.showSomeData(column_name)

    elif answer == "3":
        exam_type = input("What type of exam grade would you like to update? (final / midterm): ")      # future concern: when there are multiple finals or midterms
        student_name = input("Who would you like to update a grade for? Type full name: ")         # future concern: when i wanna choice multiple student.
        new_grade = input("What would be the new grade?: ")
        myclass.updateExamGrade(student_name, exam_type, int(new_grade))

    elif answer == "4":
        assignment_type = input("What type of assignment grade would you like to update? Type an integer number: ")
        student_name = input("Who would you like to update a grade for? Type full name: ")
        new_grade = input("What would be the new grade?: ")
        myclass.updateExamGrade(student_name, assignment_type, int(new_grade))

    elif answer == "5":
        student_name = input("What team would you like to update a grade for?: ")
        new_grade = input("What would be the new grade?: ")
        myclass.updateTeamprojectGrade()

    elif answer=="6":
        print("Thank you for using this program! See you again!")
        break





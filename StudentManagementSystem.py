import pandas as pd

class CS22B:
    students = []
    def __init__(self, prof, data):
        print()
        self.prof = prof
        self.data = data
        self.head = data[0].strip().split(",")

        for line in data[1:]:             # future concern: no function to adjust along the column name
            line = line.strip().split(",")
            self.students.append(Student(id = line[0], name = line[1], midterm = int(line[2]), final = int(line[3]), ass1 = int(line[4]), ass2 = int(line[5]), ass3 = int(line[6]), team_name = line[7], teamproject_grade = int(line[8])))

    def rewrite(self):
        self.data = []

        for s in self.students:
            self.data.append({self.head[0]: s.getId(), 
                self.head[1]: s.getName(), 
                self.head[2]: s.getGrade("midterm"), 
                self.head[3]: s.getGrade("final"), 
                self.head[4]: s.getGrade("ass1"),
                self.head[5]: s.getGrade("ass2"),
                self.head[6]: s.getGrade("ass3"),
                self.head[7]: s.getTeamName(), 
                self.head[8]: s.getGrade("teamproject")})

    def showAllData(self):
        self.rewrite()
        for i in self.data:
            print(i)
    
    def showSomeData(self, column_name):
        self.rewrite()

        if column_name == "midterm" or column_name == "final" or "ass" in column_name or "teamproject":
            for student in self.students:
                print(student.getName() + ": " + student.getGrade(column_name))
        elif column_name == "id":
            for student in self.students:
                print(student.getName() +": "+ student.getId())
        elif column_name == "teamname":
            for student in self.students:
                print(student.getName() +" is in "+ student.getTeamName())
        elif column_name == "name":
            print()
    
    def printAverage(self,title):
        avg = sum([i.getGrade(title) for i in self.students])/len(self.students)
        print("Average grade of " + title + " is ",avg," / ",self.students[0].getFullGrade(title))

    def getStudentAerage(self, name):
        for s in self.students:
            if s.getName() == name:
                grade_dict = s.getAllGrades()
                print(grade_dict)
                print("average: " + sum([i.getGrade() for i in grade_dict.values()])/len(grade_dict))
        
    def updateGrade(self, student_name, title, new_grade):
        for student in self.students:
            if student.getName() == student_name:
                student.setGrade(title, new_grade)
                print("Successfully updated!")
                break
    
    def updateGrade(self, teamname, new_grade):
        for student in self.students:
            if student.getTeamName() == teamname:
                student.setGrade("teamproject", new_grade)
                print("Successfully Updated " + student.getName()+"'s team project grade!")
                print("\n")

class Grade:
    full_grade = 0

    def __init__(self, grade):
        self.grade = grade

    def getGrade(self):
        return self.grade

    def setGrade(self, new_grade):
        self.grade = new_grade

    def getFullGrade(self):
        if self.full_grade == 0:
            return int(input("You have not set full_grade. Enter the full grade. "))
        return self.full_grade

class Student:
    grades = {}
    assignments = []
    def __init__(self, name, id, midterm, final, ass1, ass2, ass3, teamproject_grade, team_name):
        self.name = name
        self.id = id
        self.grades["midterm"] = Grade(midterm)
        self.grades["final"] = Grade(final)
        self.grades["ass1"] = Grade(ass1)
        self.grades["ass2"] = Grade(ass2)
        self.grades["ass3"] = Grade(ass3)

        self.grades["teamproject"] = Grade(teamproject_grade)
        self.teamproject = TeamProject(team_name)
    
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getGrade(self, title):
        return self.grades[title].getGrade()

    def setGrade(self, title, new_grade):
        self.grades[title].setGrade(new_grade)
    
    def getTeamName(self):
        return self.teamproject.getTeamName()
    
    def getAllGrades(self):
        return self.grades

    def getFullGrade(self, title):
        return self.grades[title].getFullGrade()
    
class Assignment:
    def __init__(self, title):
        self.title = title

    def getTitle(self):
        return self.title


class TeamProject:
    def __init__(self, team_name):
        self.team_name = team_name

    def getTeamName(self):
        return self.team_name


class Exam(Grade):
    full_grade = 0

    def __init__(self, exam_type, grade):
        self.kind = exam_type
        self.grade = grade

    def isFullGradeSet(self):
        return True if self.full_grade != 0 else False

    def setFullGrade(self, full_grade):
        self.full_grade = full_grade

    def getFullGrade(self):
        return self.full_grade


def getData(filename):
    try:
        d = open(filename, "r")
        print("File succesfully uploaded!")
        return d
    except FileNotFoundError:
        return -1
            

DEFAULT = "What do you want to do? Choose and enter a number\n\
            1) show all data\n\
            2) search a student's data\n\
            3) update a exam / an assignment grade\n\
            4) update team project grade\n\
            5) get average of a exam / an assignment\n\
            6) get average of all grades of one student\n\
            7) exit\n"

def main():
    data = 0
    while(data > -1):
        data = getData(input("Type file name: "))
    
    myclass = CS22B(input("Professor name: "),data.readlines())

    while(1):
        answer = input(DEFAULT)
        if answer == "1":
            myclass.showAllData()

        elif answer == "2":
            column_name = input("What column of data would you like to see?: ")
            myclass.showSomeData(column_name)

        elif answer == "3":
            title = input("What type of exam grade would you like to update? (final / midterm / assignment name): ")      # future concern: when there are multiple finals or midterms
            student_name = input("Who would you like to update a grade for? Type full name: ")         # future concern: when i wanna choice multiple student.
            new_grade = int(input("What would be the new grade?: "))
            myclass.updateGrade(student_name, title, new_grade)

        elif answer == "4":
            team_name = input("What team would you like to update a grade for?: ")
            new_grade = input("What would be the new grade?: ")
            myclass.updateGrade(team_name, new_grade)
        
        elif answer == "5":
            title = input("What type of average of grade would you like to see? (final / midterm / assignemnt name / teamproject): ")
            myclass.printAverage(title)

        elif answer == "6":
            student_name = input("Who would you like to get the average score of?: ")
            myclass.getStudentAverage()

        elif answer=="7":
            print("Thank you for using this program! See you again!")
            break

main()
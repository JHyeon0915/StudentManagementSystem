class CS22B:
    def __init__(self, prof, data):
        self.students = []
        self.prof = prof
        self.head = data[0].strip().split(",")

        for line in data[1:]:               # future concern: no function to adjust along the column name
            line = line.strip().split(",")
            self.students.append(Student(line[0], line[1], int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]), line[7], int(line[8])))
            
    def showAllData(self):
        for s in self.students:
            print(self.head[0],":",s.getId(),end=", ")
            print(self.head[1],":",s.getName(),end=", ")
            print(self.head[2],":",s.getGrade("midterm"),end=", ")
            print(self.head[3],":",s.getGrade("final"),end=", ")
            print(self.head[4],":",s.getGrade("ass1"),end=", ")
            print(self.head[5],":",s.getGrade("ass2"),end=", ")
            print(self.head[6],":",s.getGrade("ass3"),end=", ")
            print(self.head[7],":",s.getName(),end=", ")
            print(self.head[8],":",s.getGrade("teamproject"),end="\n")
    
    def showSomeData(self, column_name):
        if column_name == "midterm" or column_name == "final" or "ass" in column_name or column_name == "teamproject":
            for student in self.students:
                print(student.getName() + ":",student.getGrade(column_name), end="\n")
        elif column_name == "id":
            for student in self.students:
                print(student.getName() +": "+ student.getId(), end="\n")
        elif column_name == "teamname":
            for student in self.students:
                print(student.getName() +" is in "+ student.getTeamName(), end="\n")
        elif column_name == "name":
            for student in self.students:
                print(student.getName())
        else:
            print("No such column name like that.",end="\n")
    
    def printAverage(self,title):
        avg = sum([i.getGrade(title) for i in self.students])/len(self.students)
        print("Average grade of " + title + " is ",avg," / ",self.students[0].getFullGrade(title))

    def getStudentAverage(self, name):
        for s in self.students:
            if s.getName() == name:
                grade_dict = s.getAllGrades()
                for i in grade_dict:
                    print(i,":",grade_dict[i].getGrade())
                print(name,"'s average grade:",sum([i.getGrade() for i in grade_dict.values()])/len(grade_dict),end="\n")
                break
        
    def updateGrade(self, student_name, title, new_grade):
        for student in self.students:
            if student.getName() == student_name:
                student.setGrade(title, new_grade)
                print("Successfully updated!", end="\n")
                break
        print("\n")
    
    def updateTeamGrade(self, teamname, new_grade):
        for student in self.students:
            if student.getTeamName() == teamname:
                student.setGrade("teamproject", new_grade)
                print("Successfully Updated " + student.getName()+"'s team project grade!")
        print("\n")

class Grade:
    def __init__(self, grade):
        self.full_grade = 0
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
    def __init__(self,id,name, midterm, final, ass1, ass2, ass3, team_name,teamproject_grade):
        self.name = name
        self.id = id
        self.grades = {}
        self.grades["midterm"] = Exam("midterm", midterm)
        self.grades["final"] = Exam("final",final)
        self.grades["ass1"] = Assignment("ass1",ass1)
        self.grades["ass2"] = Assignment("ass2",ass2)
        self.grades["ass3"] = Assignment("ass3",ass3)
        self.grades["teamproject"] = TeamProject(team_name, teamproject_grade)

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getGrade(self, title):
        return self.grades[title].getGrade()

    def setGrade(self, title, new_grade):
        self.grades[title].setGrade(new_grade)
    
    def getTeamName(self):
        return self.grades["teamproject"].getTeamName()
    
    def getAllGrades(self):
        return {i: self.grades[i] for i in self.grades.keys()}

    def getFullGrade(self, title):
        return self.grades[title].getFullGrade()


class Assignment(Grade):
    def __init__(self, title, grade):
        self.title = title
        super().__init__(grade)

    def getTitle(self):
        return self.title


class TeamProject(Grade):
    def __init__(self, team_name, grade):
        self.team_name = team_name
        super().__init__(grade)

    def getTeamName(self):
        return self.team_name


class Exam(Grade):
    def __init__(self, exam_type, grade):
        self.kind = exam_type
        super().__init__(grade)

def getData(filename):
    try:
        d = open(filename, "r")
        print("File succesfully uploaded!")
        return d
    except FileNotFoundError:
        print("File does not exist!")
        exit(-1)
            

DEFAULT = "What do you want to do? Choose and enter a number\n\
            1) show all data\n\
            2) search a data\n\
            3) update a exam / an assignment grade\n\
            4) update team project grade\n\
            5) get average of a exam / an assignment\n\
            6) get average of all grades of one student\n\
            7) exit\n"

def main():
    data = getData(input("Type file name: "))
    myclass = CS22B(input("Professor name: "), data.readlines())

    while(1):
        answer = input(DEFAULT)
        if answer == "1":
            myclass.showAllData()

        elif answer == "2":
            column_name = input("What column of data would you like to see? (id, name, final, midterm, assignment name, team_name, teamproject): ")
            myclass.showSomeData(column_name)

        elif answer == "3":
            title = input("What type of exam grade would you like to update? (final / midterm / assignment name): ")      # future concern: when there are multiple finals or midterms
            student_name = input("Who would you like to update a grade for? Type full name: ")         # future concern: when i wanna choice multiple student.
            new_grade = int(input("What would be the new grade?: "))
            myclass.updateGrade(student_name, title, new_grade)

        elif answer == "4":
            team_name = input("What team would you like to update a grade for?: ")
            new_grade = input("What would be the new grade?: ")
            myclass.updateTeamGrade(team_name, new_grade)
        
        elif answer == "5":
            title = input("What type of average of grade would you like to see? (final / midterm / assignemnt name / teamproject): ")
            myclass.printAverage(title)

        elif answer == "6":
            student_name = input("Who would you like to get the average score of?: ")
            myclass.getStudentAverage(student_name)

        elif answer=="7":
            print("Thank you for using this program! See you again!")
            break

main()
class CS22B:
    students = []
    assignments = []
    exams = []
    teamprojects = []

    def __init__(self, prof):
        self.prof = prof
    
    def enrollStudent(self, student_object):
        self.students.append(student_object)

    def createAssignment(self, title, duedate):
        a = Assignment(title, duedate)
        self.assignments.append(a)

    def createExam(self, kind, date):
        e = Exam(kind, date)
        self.exams.append(e)

    def createTeamProject(self, title, duedate, student_names):
        teammates = [i for i in self.students for j in student_names if i.getName == j]
        t = TeamProject(title, duedate, teammates)
        self.teamprojects.append(t)


class Student:
    classes = []
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def getName(self):
        return self.name
    
    def enroll(self, class_object):
        self.classes.append(class_object)
    
class Assignment:
    def __init__(self, title, duedate):
        self.title = title
        self.duedate = duedate

class TeamProject(Assignment):
    def __init__(self, title, duedate, students):
        self.teammates = students
        super().__init__(title, duedate)


class Exam:
    def __init__(self, kind, date):
        self.kind = kind
        self.date = date
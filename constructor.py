class student:
    marks=[]
    def __init__(self,rollno):
        self.roll=rollno
        self.rollno=rollno
    def input_marks(self):
        for i in range(3):
            self.marks.append(int(input()))
    def display(self):
        print("rollno=",self.roll)
        print("marks=")
        for i in range(3):
            print(" %d"%(self.marks[i]))
stu1=student(101)
print("rollno=",stu1.roll)
stu1.input_marks()
stu1.display()

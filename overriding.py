class Person:
    def _init_(self,name,age,contact):
        self.name = name
        self.age = age
        self.contact = contact
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Contact:",self.contact)

# s = Person("Yash",18,989003040)
# s.display()

class student(Person):
    marks = []
    avg = 0
    def _init(self,sapid,prog,rollno,name,age,contact): #init is used to create constructor with two _ __ must use self in every function in case of class
        Person._init_(self,name,age,contact)
        self.rollno = rollno
        self.sapid = sapid
        self.prog = prog
        # can also be self.rollno = rollno 
    def input_marks(self):
        for i in range(3):
            self.marks.append(int(input("Enter marks = ")))
    def avge(self):
        c = 0
        for i in range(len(self.marks)):
            c = c + self.marks[i]
        self.avg = c // len(self.marks)
        return self.avg
    def grd(self):
        if(self.avg >= 80 and self.avg<= 100):
            grade = '0'
        else:
            grade = 'F'
        return grade
    def display(self):
        print('Roll no = ',self.rollno)
        print("Sap Id:",self.sapid)
        print("Progamme:",self.prog)
        print('Marks = ')
        for i in range(3):
            print('Marks %d'%(self.marks[i]))
        print("Average = ",self.avge())
        print("Grade = ", self.grd())
        
        # to call display from here
        #Person.display(self) or #self.display()
        
stu1 = student(5001022,"B.tech",101,name = 'aman',age = 10,contact= 90)

stu1.input_marks()

stu1.display()
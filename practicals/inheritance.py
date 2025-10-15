#concepts of functions, inheritance and objects
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(self.name)
        print(self.age)

#inherited class

class student(person):
    def __init__(self,name,age,courses=None):
        super().__init__(name, age)    # call constructor of person
        if courses is None:
            self.courses=[]
        else:
            self.courses=courses

    
    def add_course(self,course_name):
        self.courses.append(course_name)

Chandrayan=student("Chandrayan",18,["Mern"])
Arpita = person("Arpita",18)

Chandrayan.display()
Arpita.display()

Chandrayan.add_course("Python")
Chandrayan.display()
#  variables are containers for storing data values
# shared among all instances of a class
# defined outside the constructor 
# allow you to share data among objects create from that class

class student:

    # class variable
    class_year = 2026
    num_students = 0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.num_students += 1

student1 = student("Vilas",25)
student2 = student("Aniket",26)
student3 = student("Rahul",27)
student4 = student("Samarth",28)



print(f"my gruduating class of {student.class_year} has {student.num_students} students.")
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(student3.name)
print(student3.age)
print(student4.name)
print(student4.age)


    
    
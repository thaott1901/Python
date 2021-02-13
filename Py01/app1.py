from Student import Student

student1 = Student("A", "CS", 3.5, False)
student2 = Student("B", "BA", 3.1, False)

print(student1.on_honor_roll())
print(student1.gpa)
print(student2.on_honor_roll())
print(student2.gpa)
import Translator

employee_file = open("a.txt", "r")
phrase = employee_file.readline()
# print(employee_file.read())
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.write("\nXxxxxx")

employee_file.close()

print(Translator.translate(phrase))


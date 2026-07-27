employee = {
    "name": "ali", "age":20}
location = {"city": "lahore"}
employee.update(location)
print(employee)


info = {}
name = input("Enter name: ")
city = input("Enter city: ")
print('data in info')
print(info.setdefault('pName',name))
print(info.setdefault('pCity',city))
print(info)


#create dictionary

students = {
    "Ali": {"age": 19, "course": "Python"},
    "Fatima": {"age": 17, "course": "Java"},
    "Minahil": {"age": 20, "course": "C#"}

}
print(students)

std_name = input("Enter student name: ").lower()
for name, course in students.items():
    name1 = name.lower()
    if name1 == std_name:
        print(course['course'])
        break
else:
    print("Student not found")







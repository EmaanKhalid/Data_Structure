names = {'ali', 'ahmad', 'fatima'}
#print(names, len(names))
names.add('bilal')
print(names, len(names))

subjects = {"Python", "Java"}
subject = []
while True:
    course= input("enter atleast 3 subjects:")
    subject.append(course)
    print (subject)
    choice = input("Do you want to add another subject? (yes/no): ").lower()
    if choice == "no":
        break
if len(subject)>3:
    subjects.update(subject)

print("Updated subjects:", subjects)

delete = input("Enter subject name to delete: ").lower()
if delete in subjects:
    subjects.remove(delete)
print("Subject set after deleting subject:", subjects)
#ask the user to enter student names until they type done
students = []

while True:
    name =input('enter student name:')
    if name =='done' or name == 'Done':
        break
    students.append(name)
print(students)


#print even numbers
even_numbers = []
for i in range(2,101):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)



# find lowest and largest marks
marks = [76, 45, 98, 67, 88]
marks.sort()
print(marks)
min_marks =marks[-1]
max_marks =marks[0]

for i in marks:
    if i > max_marks:
        max_marks = i
    if i < min_marks:
        min_marks = i
print("min_marks", min_marks)
print("max_marks", max_marks)



#stack implementation
# Create an empty stack
stack = []

# Maximum capacity of the stack
MAX_SIZE = 5

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(stack) == MAX_SIZE:
            print("Stack is full! Can't push another item.")
        else:
            item = input("Enter element to push: ")
            stack.append(item)
            print(item, "pushed successfully.")

    elif choice == "2":
        if len(stack) == 0:
            print("Stack is empty! Nothing to pop.")
        else:
            removed = stack.pop()
            print(removed, "popped successfully.")

    elif choice == "3":
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack (Top → Bottom):")
            for item in reversed(stack):
                print(item)

    elif choice == "4":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")

# Getting count and index

fruits_tuple = ('Mango', 'Apple', 'Orange','Mango','Grapes','Apple')
print(fruits_tuple)
name = input('Enter fruit name from above option: ').lower()
fruits = tuple(fruit.lower() for fruit in fruits_tuple)

count = fruits.count(name)
index= fruits.index(name)
print(f"count of {name} is {count}")
print(f'index of {name} is {index}')

# Finding sum and average of tuple elements
def sum_avg_tuple(tuple_1):
    total = 0
    avg =0
    for i in tuple_1:
        total += i
        avg = total/len(tuple_1)

    return total, avg

tpl =(1,2,3,4)
tpl2=sum_avg_tuple(tpl)
print(tpl2)

#upacking
(sum, avg) = sum_avg_tuple(tpl)
print(sum, avg)
print('total sum of tuple elements:',sum)
print('total average of tuple elements:',avg)

#getting multiple values from user in tuple
list1 = []
while True:
    print("1. enter number")
    print("2. Exit")
    choice = input('Enter your choice: ')
    if choice == '1':
        items = int(input('Enter your number: '))
        list1.append(items)
    elif choice == '2':
        break

new_tuple = tuple(list1)
print(new_tuple)


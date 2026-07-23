lst_2 = list()
for i in range(1,6):
    lst_2.append(i)

print(lst_2)

#updating the value at a specific index
lst_2[1] = 'a'
print('lst_2 after updating using index:',lst_2)

#updating the value using slicing
lst_2[2:4] = [2,'f',5.5]
print('lst_2 after updating with slicing:',lst_2)

list1 = [1,2,3,4,5]
x=list1.append(6)
print(x)

#creating and initializing tuple
tuple_1 = (1, 2, 3,'abc','xyz',6,7,8,[5,4,3])
print(tuple_1[8][1])

#tuple_1[1]= 'tyu' #give an error
#print(tuple_1)

lst = tuple_1[8]
print(lst)
lst[1]= 'fgh'
print(lst)

tuple_2 = tuple(lst)
tuple_1 += tuple_2
print(tuple_1)


#for i in tuple_1:
    #print(i)

j = 0
tpl = 1,2,3,4
while j < len(tpl):
    print(tpl[j])
    j+=1

#count() checks only top level elements not inside nested list or tuple
tuple_2 = ((4, 5), 1, (4, 5), [4, 5], (2,), 4, 5)
print(tuple_2.count(5))



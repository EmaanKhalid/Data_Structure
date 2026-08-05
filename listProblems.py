#Find the average of all numbers.
lst = [2,3,4,2,6,8]
#sum = 0
'''for ch in lst:
    sum += ch
result = sum/len(lst)
print(result)'''

#Check whether a given number exists in the list.
num = int(input("Enter a number to search: "))
'''for ch in lst:
    if ch == num:
        print(ch)
        break
    else:
        print('Number not found')'''

#Count how many times a number appears
'''count = 0
for ch in lst:
    if ch == num:
        count +=  1

print(f'{num} appears:',count, 'times')'''

#Find the index of the first occurrence.
for i,ch in enumerate(lst):
    if num==ch:
        print(i,num)


   #if ch == num:
        #print(i)
       # break



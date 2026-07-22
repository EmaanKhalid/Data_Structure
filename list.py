#creating an empty list
#fast direct method
lst_1 = []
print('empty list:', lst_1)

#creating using list() constructor
#slow looks for class and calls constructor
lst_2 = list()
print('empty list using constructor:', lst_2)

#adds only one item
lst_1.append(1)
print('Elements in lst_1 using append:',lst_1)

#adds multiple elements from iterable.
lst_1.extend([14, 43, 37])
print('Elements in lst_1 using extend:',lst_1)

#adds at specific index
lst_1.insert(2, 3)
print('Elements in lst_1 using insert:',lst_1)
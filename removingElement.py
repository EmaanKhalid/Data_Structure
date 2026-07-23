#remove
#worst case o(n)
list1 = [1,2,3,4,3,1,6,5,6]
list1.remove(6)
print(list1)

#pop()
#o(1)
lst = [10, 20, 30, 40, 50]
x = lst.pop()
print(x)
print(lst)

#pop(index)
#o(n)
a = lst.pop(1)
print(a)

#clear
#o(n)
lst.clear()
print(lst)

#index() checks position of element
#o(n) worst case
b=list1.index(3)
print(b)

#count() occurrence
#o(n)
c = list1.count(6)
print(c)

#sort()
#o(n) best case
lst = [4,1,3,2]
lst.sort()
print(lst)

#reverse
#O(n)
lst.reverse()
print(lst)

#copy
#O(n)
lst2 = lst.copy()
print(lst2)
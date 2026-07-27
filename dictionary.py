#Creating dictionary
dict_one = {"name": "Laiba", "age": 19, "city": "Lahore"}
#print(dict_one["name"])
#print(dict_one["age"])

#Adding items in dictionary
dict_one["gender"] = "Female"
dict_one["status"] = "student"
#print(dict_one)

#adding multiple values using list
dict_2 = {'name': ['Ali', 'Mehwish', 'faizan', 'Ayesha'],
          'age': [19, 25, 20, 22],
          'city': ['Lahore', 'Sialkot', 'Murree', 'Karachi'],
          'gender':['Male', 'Female', 'Male', 'Female']}
#print(dict_2)

#deleting key using del
#del dict_one['age']
#print(dict_one)

#deleting specific value of key
#del dict_2['city'][-1]
#print(dict_2)

#deleting using pop()
#popped_value = dict_one.pop('gender')
#print(dict_one)
#print(popped_value)

#deleting specific value of key using pop
popped_value1 = dict_2['gender'].pop(0)
print(dict_2)
print(popped_value1)

#print('dict 2 before deleting value:',dict_2)
#popped_value2 = dict_2.popitem()
#print(popped_value2)
#print('dict 2 after deleting:',dict_2)

print("Name:", dict_one["name"])
x = dict_one.get("name")
print(x)
#print("Name:", dict_one.get("name"))
print("Occupation:", dict_one.get("occupation",'not exist'))


#print("Occupation:", dict_one.setdefault("occupation",'student'))




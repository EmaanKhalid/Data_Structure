import copy
house = [["Bed"], ["Table"]]
house2 = copy.copy(house)
print("shallow copy")
print('House:',house)

print('House2:',house2)
house2[0].append(["chair"])
print('House2:',house2)
print('House:',house)


house3 = copy.deepcopy(house)

print('House3:',house3)
house3[0]=['chair']
print('House3:',house3)
print('House:',house)



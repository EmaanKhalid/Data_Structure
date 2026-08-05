#finding duplicates
'''txt = input("Enter a word: ")
ch_freq = dict()
lst =[]
for ch in txt:
    frequency = txt.count(ch)
    ch_freq[ch] = frequency
    if frequency > 1 and ch not in lst:
        lst.append(ch)
print(ch_freq)
print(lst)'''

#character with highest frequency
'''txt = input("Enter a word: ")
ch_freq = dict()
ch =''
for ch in txt:
    frequency = txt.count(ch)
    ch_freq[ch] = frequency
print(ch_freq)
#print("Character with highest frequency: ",max(ch_freq, key=ch_freq.get))

#Remove duplicate characters while keeping the first occurrence.
list1 = ''.join(list(ch_freq.keys()))
print(list1)'''

#all non repeating characters
txt = input("Enter a word: ")
lst = []

for ch in txt:
    if txt.count(ch) == 1:
        lst.append(ch)
print(lst)



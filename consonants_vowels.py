#Count vowels and consonants.
'''txt = input('Enter your text: ').lower()
lst1 = []
lst2 =[]
vowels_count = 0
consonants_count = 0
for letter in txt:
    if letter in 'aeiou':
        vowels_count += 1
        lst1.append(letter)
    else:
       lst2.append(letter)
       consonants_count = consonants_count +1
print('List of vowels:',lst1)
print('vowels_count:',vowels_count)
print('List of consonants:',lst2)
print('consonants_count:',consonants_count)'''

#Check whether two strings are anagrams.
'''txt1 = input("Enter a word: ")
txt2 = input("Enter another word: ")
txt1 = sorted(txt1)
txt2 = sorted(txt2)

if len(txt1) == len(txt2) and txt1 == txt2:
    print("Both strings are anagrams")
else:
    print("Both strings are not anagrams")'''

#Check whether a string is a palindrome.
'''txt1 = input("Enter a word: ").lower()
txt2 = txt1[::-1]
if txt1 == txt2:
    print("string is palindrome")
else:
    print("string is not palindrome")'''

#Reverse each word of a sentence.
txt1 = input("Enter a word: ")
txt2 = txt1.split(' ')
'''for ch in txt2:
    ch2 = ch[::-1]
    print(ch2)'''
#Reverse the order of words.
#print(txt2[::-1])

#Capitalize the first letter of every word (without using title())
'''ch3 = ''
for ch in txt2:
    ch1 = ch[0].upper()
    ch2 = ch1 + ch[1:]
    ch3 = ch3 + ' '+ ch2
print(ch3)'''

#Find the longest word in a sentence.
max = txt2[0]
min = txt2[0]
for ch in txt2:
    if len(ch) > len(max):
        max = ch
    elif len(ch) < len(min):
        min = ch
print('Longest word is:',max)
print('Shortest word is:',min)

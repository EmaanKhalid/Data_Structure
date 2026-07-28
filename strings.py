#split and capitalize

text = "hello world"
print(text)
txt2= text.split(" ")
print(txt2[0].capitalize() + ' '+ txt2[1].capitalize())

#lowercase and casefold
text2 = "LIßI"
print(text2.lower())
print(text2.casefold())


#-----
name = input("Enter your name: ")
new_name= name.strip()
if new_name == "":
    print("Username cannot be empty.")
else:
    print('Welcome,',new_name,"\n",'Length:',len(new_name))


#-----
fruits = input("Enter your fruits: ").split(',')
new_list = []
for fruit in fruits:
    x=fruit.strip()
    if x!="":
        new_list.append(x)
if len(new_list)==3:
    print('Total fruits: ',len(new_list))
    print('First fruit: ',new_list[0])
    print('Last fruit: ',new_list[-1])
else:
    print('please enter 3 fruits')
print(new_list)


#----
letters = input("Enter 5 letters: ").split()

if len(letters) == 5:
    hyphen = "-"
    star = "*"
    word = "".join(letters)
    hyphen1 = hyphen.join(letters)
    star1 = star.join(letters)
    print("Word: ",word)
    print("Hyphen: ", hyphen1)
    print("Star: ", star1)
else:
    print("please enter 5 letters")

#-----
sentence = input("Enter a sentence: ")
sentence1 = sentence.lower()
print('Original: ', sentence)
if 'python' in sentence1:
    new_sentence = sentence1.replace("python","Java")
    print('Updated: ',new_sentence)
else:
    print("Python not found in the sentence.")

#----------
sentence_2 = input("Enter a sentence: ").lower()
word1 = input('Enter a word to search: ').lower()

if word1 in sentence_2:
    print("Word Found")
    print('First index: ',sentence_2.find(word1))
    print('Occurrences: ',sentence_2.count(word1))
    print('Starts with word: ', sentence_2.startswith(word1))
    print('Ends with word: ', sentence_2.endswith(word1))
else:
    print("Word Not Found")



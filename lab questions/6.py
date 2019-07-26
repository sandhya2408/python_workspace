sentence = input("enter a string")
sentence.lower()
for i in sentence:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    else:
        print(i,end = "")

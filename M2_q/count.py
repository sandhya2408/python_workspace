'''9.	Write a program to find the word(s) that occur maximum and minimum number of times in the given paragraph. Also, display those words next to their respective count.

Input:
"Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3."
'''
data = "Comprehensions are a feature of Python which I would really miss if I ever have to leave it . Comprehensions are constructs that allow sequences to be built from other sequences . Several types of comprehensions are supported in both Python 2 and Python 3 .".lower()

d = dict()
c = 0
words = data.split()
for word in words:
    if d.get(word) == None:
        d[word] = 1
    else:
        d[word] += 1
max = 0
for j in d:
    if d[j] > max:
        max = d[j]
print(f"{j}:{d[j]}times")
'''10.	Write a program to count the number of unique words and the number of occurrences of each of those words from the question provided below.
Input:
"How much wood would a woodchuck chuck if the woodchuck could chuck wood ?"
Output:
Number of unique words: x
abcd: p times
efgh: q times
rstu: t times
'''
data = "How much wood would a woodchuck chuck if the woodchuck could chuck wood ?"
d = dict()
c = 0
words = data.split()
for word in words:
    if d.get(word) == None:
        d[word] = 1
    else:
        d[word] += 1
for j in d:
    if d[j] == 1:
        c += 1
        print(f"{j}:{d[j]} times")
print(f"unique count {c}")
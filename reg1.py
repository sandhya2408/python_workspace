import re
inp = "12,14-15,18,13-2"
lst = re.sub(r"-",",",inp)
res = list(lst.split(","))
print(res)
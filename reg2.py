import re
inp = "1007 lakshman 1008 karthik 1009 ramesh 1010 suresh"
res = re.findall(r"\d+",inp)
print(res)
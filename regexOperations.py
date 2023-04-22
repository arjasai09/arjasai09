import re


Names = """Gabriel is 99 and Manoj is 22
     Vamsi is 24 and Trinadh is 25"""


ages = re.findall(r'\d{1,3}', Names)
names  = re.findall(r'[A-Z][a-z]*', Names)

print(names)
print(ages)


d = {}
x = 0
for i in names:
    d[i] = ages[x]
    x += 1

print(d)

print(len(d))

x = -2 ** (-3)

print(abs(x))



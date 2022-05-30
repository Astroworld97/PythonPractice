import math

x = 1234554321
s = str(x)
stkStart = []
stkEnd = []
retval = True
for i in range(0, math.floor(len(s) / 2)):
    stkStart.append(s[i])
    stkEnd.append(s[len(s) - 1 - i])

for i in range(0, math.floor(len(stkStart))):
    a = stkStart.pop()
    b = stkEnd.pop()
    if a != b:
        retval = False

print(retval)

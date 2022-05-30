import math


def isPalindrome():
    s = "racecar"
    s = s.lower()
    edit = ""
    for i in s:
        if i.isalnum() == True:
            edit += i
    s = edit
    stkStart = []
    stkEnd = []
    for i in range(0, floor(len(s) / 2)):
        stkStart.append(s[i])
        stkEnd.append(s[len(s) - i - 1])
    if len(stkStart) != len(stkEnd):
        return False
    for i in range(0, floor(len(s) / 2)):
        a = stkStart.pop()
        b = stkEnd.pop()
        if a != b:
            return False
    return True

if __name__ == '__main__':
    s = input()

    alphaNum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    i = ''

    for i in s:

        if i.isalnum():
            alphaNum = True

        if i.isalpha():
            alpha = True

        if i.isdigit():
            digit = True

        if i.islower():
            lower = True

        if i.isupper():
            upper = True

    print(alphaNum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
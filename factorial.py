def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return "NA"
    else:
        return n * recur_factorial(n - 1)


def specific_factorial(n):
    return (recur_factorial(n)) ** (1 / 3)


for i in range(1, 101):
    print("for " + str(i) + ": " + str(specific_factorial(i) / (1000 * 60 * 60 * 24)))

# 27-08-19
dic = {}


def Factorial(n):
    if n in dic:
        return dic[n]
    elif n == 0:
        val = 1
    else:
        val = n * Factorial(n - 1)
    dic[n] = val
    return val

print(Factorial(3))
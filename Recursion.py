def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


# print(fac(7))

def sum1ToN(n):
    if n == 0:
        return 0
    else:
        return n + sum1ToN(n - 1)


# print(sum1ToN(10))

def printNto1(n):
    if n == 1:
        print(n)
    else:
        print(n)
        printNto1(n - 1)


# printNto1(7)

def print1toN(n):
    if n == 1:
        print(n)
    else:
        print1toN(n - 1)
        print(n)


# print1toN(7)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(7))

def binarySearch(lo, hi, x, l):
    sfs
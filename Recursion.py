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
    if hi < lo:
        return None
    mid = (lo+hi)//2
    if x == l[mid]:
        return mid
    elif l[mid] < x:
        return binarySearch(mid+1, hi, x, l)
    else:
        return binarySearch(lo, mid-1, x, l)

# l = [1,2,3,4,5,6,7,8,9,10]
# print(binarySearch(0,9,5,l))

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
        return 1
    else:
        return n + printNto1(n - 1)


# print(printNto1(7))

def print1toN(n):
    if n == 1:
        return 1
    else:
        return print1toN(n - 1) + n


# print(print1toN(7))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(7))

def binarySearch(lo, hi, x, l):
    if hi < lo:
        return None
    mid = (lo + hi) // 2
    if x == l[mid]:
        return mid
    elif l[mid] < x:
        return binarySearch(mid + 1, hi, x, l)
    else:
        return binarySearch(lo, mid - 1, x, l)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binarySearch(0,9,5,l))

def move(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print('move disk', n, 'from', from_rod, 'to', to_rod)
    else:
        move(n - 1, from_rod, aux_rod, to_rod)
        print('move disk', n, 'from', from_rod, 'to', to_rod)
        move(n - 1, aux_rod, to_rod, from_rod)


# move(3,'A','C','B')

def sum1(n, l):
    if n is 0:
        return 0
    elif n is 1:
        return l[0]
    else:
        return sum1(n - 1, l) + l[n - 1]


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum1(len(l), l))


def sum2(l, fromI, toI):
    if fromI > toI:
        return 0
    elif fromI == toI:
        return l[toI]
    else:
        return l[fromI] + sum2(l, fromI + 1, toI)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum2(l, 0, len(l) - 1))

def sum3(l):
    n = len(l)

    if n is 0:
        return 0
    elif n is 1:
        return l[0]
    else:
        return l[0] + sum3(l[1:])


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum3(l))

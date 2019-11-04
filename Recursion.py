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

def printForw(L, i):  # print list forward
    if i < len(L):
        print(L[i], end=' ')
        printForw(L, i + 1)
    else:
        print()


def printBack(L, i):  # print list backward
    if i < len(L):
        printBack(L, i + 1)
        print(L[i], end=' ')
    else:
        print()


# L = [2, 3, 5, 7, 11]
# print(L)
# printForw(L, 0)
# printBack(L, 0)


def printlistForw(l, n):
    if n > 1:
        printlistForw(l, n - 1)
        print(l[n - 1], end=' ')
    elif n == 1:
        print(l[0], end=' ')


# l2 = [1, 2, 3]
# print(l2)
# printlistForw(l2, len(l2))


# --------------------------
def printlistBkw(l, n):
    if n > 1:
        print(l[n - 1], end=' ')
        printlistBkw(l, n - 1)
    elif n == 1:
        print(l[0], end=' ')


# l2 = [1, 2, 3]
# print(l2)
# printlistBkw(l2, len(l2))


def app(l, n):
    if n == 1:
        l.append(1)
    else:
        app(l, n - 1)
        l.append(n)


# l = [0]
# app(l, 5)
# print(l)


def appB(l, n):
    if n == 1:
        l.append(1)
    else:
        l.append(n)
        appB(l, n - 1)


# l = [0]
# appB(l, 5)
# print(l)

class node():
    def __init__(self, d, nxt=None):
        self.data = d
        if nxt is None:
            self.next = None
        else:
            self.next = nxt


def printList(h):
    if h is not None:
        print(h.data, end=' ')
        printList(h.next)


def createLLL1(h, i):  # create linked list from list 1
    global fromList
    if i >= 0:
        last = node(fromList[i], h)
        p = createLLL1(last, i - 1)
        return p
    else:
        return h


# fromList = [2, 5, 4, 8, 6, 7, 3, 1]
# print('---- createLLL1 -----')
# h = createLLL1(None, len(fromList) - 1)  # 2nd parameter = last index
# printList(h)
# print('\n---------------------')


def createLLL2(h, l):  # create linked list from list 2
    if l != []:
        p = node(l[-1], h)
        p = createLLL2(p, l[:-1])
        return p
    else:
        return h


# list = [2, 5, 4, 8, 6, 7, 3, 1]
# print('----- createLLL2 ------')
# h = createLLL2(None, list)
# printList(h)
# print('\n-----------------------')


def createLLL3(i, last_i, l):  # create linked list from list 3
    if i is last_i:
        return node(l[i])
    else:
        h2 = createLLL3(i + 1, last_i, l)
        h = node(l[i], h2)
        return h


# print('----- createLLL3 ------')
# list = [2, 5, 4, 8, 6, 7, 3, 1]
# h = createLLL3(0, len(list) - 1, list)
# printList(h)
# print('\n-----------------------')


def createLL1(start, n):  # create linked list 1 to n
    if start is n:
        return node(n)
    else:
        last = createLL1(start + 1, n)
        l1 = node(start, last)
        return l1


# h = createLL1(1,5)
# print('-----createLL 1-----')
# printList(h)
# print('\n--------------------')


def createLL2(n, back):  # create linked list 1 to n
    if n is 1:
        return node(1, back)
    else:
        l2 = node(n, back)
        l1 = createLL2(n - 1, l2)
        return l1


# h = createLL2(5, None)
# print('-----createLL 2-----')
# printList(h)
# print('\n--------------------')


# knapsack
def printSack(sack, maxi):
    global good
    global name
    for i in range(maxi + 1):
        print(good[sack[i]], end=' ')
        # print(name[sack[i]],good[sack[i]], end=' ')
    print()


def pick(sack, i, mLeft, good_i):
    global N
    global good
    if good_i < N:  # have something left to pick
        price = good[good_i]  # good-price
        if mLeft < price:  # cannot afford that good_i
            pick(sack, i, mLeft, good_i + 1)  # try to pick next good
        else:  # can buy
            mLeft -= price  # pay
            sack[i] = good_i  # pick that good_i to the sack at i
            if mLeft == 0:  # done
                printSack(sack, i)
            else:  # still have moneyLeft
                pick(sack, i + 1, mLeft, good_i + 1)
            pick(sack, i, mLeft + price, good_i + 1)  # take the item off the sack for other solutions


good = [20, 10, 5, 5, 3, 2, 20, 10]
name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk', 'cookie']
N = len(good)  # numbers of good

sack = N * [-1]  # empty sack
print(sack)
mLeft = 20  # money left
i = 0  # sack index
good_i = 0  # good index
pick(sack, i, mLeft, good_i)

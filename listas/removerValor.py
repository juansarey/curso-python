def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    l1[1:3] = []
    ## Write your code here
    return l1

l1 = removeList()
print(l1)


def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    l1.remove(l2[0])
    l1.remove(l2[1])
    return l1

l1 = removeList()
print(l1)


def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    for elem in l2:
        l1.remove(elem)
    return l1

l1 = removeList()
print(l1)
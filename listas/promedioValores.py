def getAverage():
    l1 = [1, 4, 9, 10, 23]
    longitud = len(l1)
    n = 0
    for l in l1:
        n += l
    avg = n/longitud ## Calculate the average here
    return avg

avg = getAverage()
print(avg)



def getAverage():
    l1 = [1, 4, 9, 10, 23]
    avg = sum(l1)/len(l1)  
    return avg
    
avg = getAverage()
print(avg)
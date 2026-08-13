def findMaximum(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

list = [1, 2, 3, 4, 5 , 20, 7, 8, 9, 10]
print(findMaximum(list))

def findMaximumValueIndex(list):
    maximum = list[0]
    index = 0
    for i, value in enumerate(list):
        if value > maximum:
            maximum = value 
            index = i
    return [index, maximum]

list = [1, 2, 3, 4, 5 , 20, 7, 8, 9, 10]
print(findMaximumValueIndex(list))
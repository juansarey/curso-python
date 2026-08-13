import math
def calculateSinCosTan(x):
    #write your function here
    sine = math.sin(x)#calculate sine
    cos = math.cos(x)#calculate cosine
    tan = math.tan(x)#calculate tangent 
    return [sine, cos, tan]

x = 0
sine, cos, tan = calculateSinCosTan(x)
print("Sine of ", x, " is: ", sine)
print("Cosine of ", x, " is: ", cos)
print("Tangent of ", x, " is: ", tan)
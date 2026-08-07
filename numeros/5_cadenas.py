a = "abc"

#usamos len() para obtener la longitud de una cadena
def getStr(s):
    n1 = s[0] * 3
    n2 = s[1] * 3
    n3 = s[2] * 3
    s = n1 + n2 + n3
    strlen = len(s)
    return [s, strlen]

getStr(a)
[s, strlen] = getStr(a)
print(s)
print(strlen)


# def getStr(s):
#   s=s[:1] + s[0] + s[1:]# Transform the string 
#   s=s[:1] + s[0] + s[1:]
#   s=s[:3] + s[3] + s[3:]
#   s=s[:3] + s[3] + s[3:]
#   s=s[:6] + s[6] + s[6:]
#   s=s[:6] + s[6] + s[6:]
#   # Update the length of string
#   strlen = len(s)
#   return [s, strlen]

# print(getStr("abc"))
# print(getStr("xyz"))
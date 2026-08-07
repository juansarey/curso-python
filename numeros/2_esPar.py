
# def esPar():
#     a = 4
#     sosPar = a % 2
#     return sosPar

# print(esPar())


# para ingresar un numero por teclado, debemos usar la funcion input(), 
# esta funcion devuelve un string, por lo que debemos convertirlo a int o 
# float segun sea el caso
numero = input("Ingrese un numero: ")
numero = int(numero)

def esPar(n):
    verificacion = numero % 2
    if (verificacion) == 0:
        resultado = print("es un numero par")
    else:
        resultado = print("es un numero impar")
    return resultado

esPar(numero)

################################
def checkParity(n):
    result = (n % 2)
    return result
print("Odd parity", checkParity(17))
print("Even parity", checkParity(16))
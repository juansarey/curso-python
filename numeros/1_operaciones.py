a = 2
print(type(a)) #int 

b = 2.5
print(type(b)) #float

#operaciones basicas con numeros

print(a + b)
print((a + b) * 2)



#hacemos una funcion que haga una operacion matematica
def Mathop():
    division_clasica = 3/2
    division_entera = 3//2
    modulo = 3%2
    potencia = 3**2

    """retornamos los resultados de las operaciones, el return sirve 
    # para devolver un valor de la funcion pero no para imprimirlo, 
    # si queremos imprimirlo debemos usar print"""
    # si ponemos el return entre corchetes, nos devuelve una tupla, 
    # si lo ponemos entre parentesis nos devuelve una lista
    return [division_clasica, division_entera, modulo, potencia]

#desempaquetamos la tupla que nos devuelve la funcion Mathop() en 4 variables
#si no hacemos esto, nos devuelve una tupla con los 4 valores, 
# pero no podemos acceder a ellos individualmente
[division_clasica, division_entera, modulo, potencia] = Mathop()
print("division clasica: ", division_clasica)
print("division entera: ", division_entera)
print("modulo: ", modulo)
print("potencia: ", potencia)




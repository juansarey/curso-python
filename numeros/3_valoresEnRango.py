lim_inf = input("ingrese el limite inferior: ")
lim_inf = float(lim_inf)

lim_sup = input("ingrese el limite superior: ")
lim_sup = float(lim_sup)

def inRange(x, y):
    if x < (1/3) < y:
        return True
    else:
        return False

inRange(lim_inf, lim_sup)
import math
def area_triangulo(base, altura):
    if base > 0 and altura > 0:
        ar = (base * altura) / 2
        return ar
    else:
        print("Las medidas ingresadas no corresponden a un triángulo.")
        return None
base = float(input("Ingrese la longitud de la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = area_triangulo(base, altura)
    print("El área del triángulo es:", area)

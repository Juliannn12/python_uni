listado = {'ANGOLA', 'COLOMBIA', 'VENEZUELA', 'MÉXICO', 'HOLANDA'}

while True:
    pais = input('Ingrese un país para verificar si está en la lista: ').upper()

    if pais in listado:
        print(f"{pais} sí está en la lista.")
    else:
        print(f"{pais} no está en la lista.")



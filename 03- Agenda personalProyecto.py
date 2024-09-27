contactos = {}

def agregar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el teléfono del contacto: ")
    correo = input("Introduce el correo electrónico del contacto: ")
    contactos[nombre] = {"telefono": telefono, "correo": correo}

def buscar_contacto():
    nombre = input("Introduce el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {contactos[nombre]['telefono']}")
        print(f"Correo electrónico: {contactos[nombre]['correo']}")
    else:
        print(f"No se encontró el contacto {nombre}")

def editar_contacto():
    nombre = input("Introduce el nombre del contacto a editar: ")
    if nombre in contactos:
        nuevo_telefono = input("Introduce el nuevo teléfono del contacto: ")
        nuevo_correo = input("Introduce el nuevo correo electrónico del contacto: ")
        contactos[nombre]["telefono"] = nuevo_telefono
        contactos[nombre]["correo"] = nuevo_correo
        print(f"Contacto {nombre} editado correctamente")
    else:
        print(f"No se encontró el contacto {nombre}")

def eliminar_contacto():
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado correctamente")
    else:
        print(f"No se encontró el contacto {nombre}")

while True:
    print("**Agenda personal**")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = int(input("Introduce una opción: "))

    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        buscar_contacto()
    elif opcion == 3:
        editar_contacto()
    elif opcion == 4:
        eliminar_contacto()
    elif opcion == 5:
        break
    else:
        print("Opción no válida.")

print("**Hasta pronto!**")

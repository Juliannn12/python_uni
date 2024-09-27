import numpy as np

def generar_matriz_aleatoria(filas, columnas):
    return np.random.randint(2, size=(filas, columnas))

def multiplicar_matrices_aleatorias(filas_a, columnas_a, columnas_b):
    matriz_a = generar_matriz_aleatoria(filas_a, columnas_a)
    matriz_b = generar_matriz_aleatoria(columnas_a, columnas_b)
    producto = np.dot(matriz_a, matriz_b)
    return matriz_a, matriz_b, producto
filas_a = 10
columnas_a = 10
columnas_b = 10
matriz_a, matriz_b, producto = multiplicar_matrices_aleatorias(filas_a, columnas_a, columnas_b)
print("Matriz A:")
print(matriz_a)
print("\nMatriz B:")
print(matriz_b)
print("\nProducto de las matrices:")
print(producto)
|
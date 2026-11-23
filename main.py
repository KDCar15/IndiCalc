import validaciones as v

# Imprimir la matriz A
def imprimir_matriz(A, end="\n"):
    for i in A:
        for j in i:
            print(j, end=" ")
        print()
    print(end, end="")

# Función del método numérico de Jacobi
def jacobi(A, b, tolerancia, max_iter):
    # 1. Validaciones
    # 1.1. Comprobar que la matriz sea cuadrada
    if not v.comprobar_matrizcuadrada(A):
        print("Error: La matriz debe ser cuadrada")
        return

    # 1.2. Comprobar que la longitud del vector B sea igual al
    # numero de columnas de A
    if len(A) != len(b):
        print("Error: El vector b no es compatible con la matriz A")
        return

    # 1.3. Comprobar que la diagonal de A no contenga 0
    if not v.comprobar_diagonal(A):
        print("Error: La diagonal no puede contener 0")
        return
    
    # 2. Metodo Jacobi
    print("Implementación pendiente")
    
matriz0 = [[1, 2, 0],[4, 5, 0],[6,7,0]]
matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

vector0 = [1, 1, 1, 1]
vector = [1, 1, 1]

imprimir_matriz(matriz0)
imprimir_matriz(matriz)

jacobi(matriz0, vector, 0.0005, 5)
jacobi(matriz, vector0, 0.0005, 5)

print("Hello world")

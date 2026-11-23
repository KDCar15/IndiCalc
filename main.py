def imprimir_matriz(A, end="\n"):
    for i in A:
        for j in i:
            print(j, end=" ")
        print()
    print(end, end="")
def comprobar_matrizcuadrada(A):
    for i in range(len(A)):
        if len(A) != len(A[i]):
            return False
    return True

def jacobi(A, b, tolerancia, max_iter):
    # 1. Comprobar que la matriz sea cuadrada
    if not comprobar_matrizcuadrada(A) :
        print("La matriz no es cuadrada")
    else:
        print("La matriz es cuadrada")
    
matriz0 = [[1, 2],[4, 5],[6,7]]
matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    
imprimir_matriz(matriz0)
imprimir_matriz(matriz)

jacobi(matriz0, 0, 0.0005, 5)
jacobi(matriz, 0, 0.0005, 5)

print("Hello world")

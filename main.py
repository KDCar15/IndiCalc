import jacobi as j

# Imprimir la matriz A
def imprimir_matriz(A, end="\n"):
    for i in A:
        for j in i:
            print(j, end=" ")
        print()
    print(end, end="")
            
matriz = [[10, 2, 1],[1, 10, 2],[2, 1, 10]]
vector = [13, 13, 13]
imprimir_matriz(matriz)

x, salida = j.jacobi(matriz, vector, 0.0005, 5)
print(salida)
print(x)

print("Hello world")

# Función para comprobar que la matriz A sea cuadrada
def comprobar_matrizcuadrada(A):
    for i in range(len(A)):
        if len(A) != len(A[i]):
            return False
    return True

# Funcion para comprobar que la diagonal de A no tenga 0
def comprobar_diagonal(A):
    for i in range(len(A)):
        if A[i][i] == 0:
            return False
    return True

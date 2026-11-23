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

def validar_jacobi(A, b):
    mensaje = ""

    # 1.1. Comprobar que la matriz sea cuadrada
    if not comprobar_matrizcuadrada(A):
        mensaje = "La matriz debe ser cuadrada"

        return False, mensaje

    # 1.2. Comprobar que la longitud del vector B sea igual al
    # numero de columnas de A
    if len(A) != len(b):
        mensaje = "El vector b no es compatible con la matriz A"
        return False, mensaje

    # 1.3. Comprobar que la diagonal de A no contenga 0
    if not comprobar_diagonal(A):
        mensaje = "La diagonal no puede contener 0"
        return False, mensaje

    return True, mensaje

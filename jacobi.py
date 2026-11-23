import validaciones as v

# Función del método numérico de Jacobi
def jacobi(A, b, tolerancia, max_iter):
    # 0. Inicializacion de variables
    salida = ""
    iteraciones = 0

    # 1. Validaciones
    validar, mensaje = v.validar_jacobi(A, b)
    if not validar:
        print(f"Error: {mensaje}")
        return

    # 2. Metodo Jacobi
    x = [0.0] * len(b)
    for k in range(max_iter):
        x_nuevo = [0.0] * len(b)

        # Calcular aproximaciones nuevas
        for i in range(len(b)):
            suma = 0.0
            for j in range(len(b)):
                if i != j:
                    suma += A[i][j] * x[j]
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        error = 0.0
        for i in range(len(b)):
            diferencia = abs(x_nuevo[i] - x[i])

            if diferencia > error:
                error = diferencia

        salida += f"Iteracion #{k+1}\n"
        salida += f"-------------------------------------\n"
        salida += f"X: {x}\n"
        salida += f"X nuevo: {x_nuevo}\n"
        salida += f"Error: {error}\n"
        salida += f"-------------------------------------\n"

        x = x_nuevo
        iteraciones += 1

        if error < tolerancia:
            return x

    salida += f"Información: Se alcanzo el número máximo de iteraciones\n"
    
    salida += f"\n"
    salida += f"-------------------------------------\n"
    salida += f"!!! RESULTADOS !!!\n"
    salida += f"-------------------------------------\n"
    salida += f"Vector X: {x}\n"
    salida += f"Iteraciones realizadas: {iteraciones}\n"
    salida += f"Error: {error}\n"
    salida += f"-------------------------------------\n"

    return x, salida

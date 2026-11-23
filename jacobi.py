
import validaciones as v

# Funcion del metodo numerico de Jacobi
def jacobi(A, b, tolerancia, max_iter):

    # 0. Inicializacion de variables
    salida = ""
    iteraciones = 0

    # 1. Validaciones
    validar, mensaje = v.validar_jacobi(A, b)

    if not validar:
        salida += f"Error: {mensaje}\n"
        return -1, salida

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

        # Calcular error
        error = 0.0

        for i in range(len(b)):

            diferencia = abs(x_nuevo[i] - x[i])

            if diferencia > error:
                error = diferencia

        # Registrar iteracion
        salida += f"Iteracion #{k + 1}\n"
        salida += "-------------------------------------\n"
        salida += f"X: {x}\n"
        salida += f"X nuevo: {x_nuevo}\n"
        salida += f"Error: {error}\n"
        salida += "-------------------------------------\n"

        x = x_nuevo[:]
        iteraciones += 1

        # Comprobar convergencia
        if error < tolerancia:
            break

    # 3. Resultados
    if error < tolerancia:
        salida += "Informacion: Convergencia alcanzada\n"
    else:
        salida += "Informacion: Se alcanzo el numero maximo de iteraciones\n"

    salida += "\n"
    salida += "-------------------------------------\n"
    salida += "!!! RESULTADOS !!!\n"
    salida += "-------------------------------------\n"
    salida += f"Vector X: {x}\n"
    salida += f"Iteraciones realizadas: {iteraciones}\n"
    salida += f"Error: {error}\n"
    salida += "-------------------------------------\n"

    return x, salida

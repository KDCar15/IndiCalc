import validaciones as v

def gauss_seidel():
    # 0. Inicializar variables
    salida = ""
    iteraciones = 0
    convergencia = False

    # 1. Validacion
    validar, mensaje = v.validar_jacobi(A,b)

    if not validar:
        raise ValueError(mensaje)
    if tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva")
    if max_iter <= 0:
        raise ValueError("El numero maximo de iteraciones debe ser positivo")

    # 2. Metodo de Gauss Seidel
    x = [0.0] * len(b)
    for k in range(max_iter):
        x_anterior = x[:]
        
        for i in range(n):
            if i != j:
                if j < i:
                    suma += A[i][j] * x[j]
                else:
                    suma += A[i][j] * x_anterior[j]
        error = 0.0
        for i in range(len(b)):
            diferencia = abs(x[i] - x_anterior[i])
            if diferencia > error:
                error = diferencia

        # Registrar iteracion
        salida += f"Iteracion #{k + 1}\n"
        salida += "-------------------------------------\n"
        salida += f"X: {x}\n"
        salida += f"X anterior: {x_anterior}\n"
        salida += f"Error: {error}\n"
        salida += "-------------------------------------\n"
        
        if error > tolerancia:
            convergencia = True
            break

        iteraciones += 1

    salida += "\n"
    salida += "-------------------------------------\n"
    salida += "!!! RESULTADOS !!!\n"
    salida += "-------------------------------------\n"
    salida += f"Vector X: {x}\n"
    salida += f"Iteraciones realizadas: {iteraciones}\n"
    salida += f"Error: {error}\n"
    if(convergencia):
        salida += f"Convergencia: Si\n"
    else:
        salida += f"Convergencia: No\n"
    salida += "-------------------------------------\n"

    return x, salida, convergencia

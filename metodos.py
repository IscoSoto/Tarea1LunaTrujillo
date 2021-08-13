# Ricardo Luna y Javier Trujillo
# Tarea 1
# Archivo de métodos

import math
# Importa la librería math de Python.

# Método multiple_op


def multiple_op(X):
    # Inicio del método.
    if type(X) == int and X >= 0:
        # Ejecuta el siguiente código si el valor ingresado al método
        # es un número entero positivo (o 0).
        a = X * X
        # Operación 1 del método, multiplica el valor ingresado por sí mismo.
        b = 2 ** X
        # Operación 2 del método, eleva 2 al valor ingresado.
        c = math.factorial(X)
        # Operación 3 del método, calcula el factorial del valor ingresado.
        array = []
        # Se crea un array inicialmente vacío.
        array.append(a)
        # Se agrega el resultado de la operación 1 al array.
        array.append(b)
        # Se agrega el resultado de la operación 2 al array.
        array.append(c)
        # Se agrega el resultado de la operación 3 al array.
        return array
    # Devuelve un array con los resultados de las 3 operaciones.
    else:
        # Si el valor ingresado no cumple las condiciones
        # definidas anteriormente, ejecuta el siguiente código.
        return "E-303: Error en tipo de dato ingresado."
    # Regresa un mensaje de error.


# Método verify_array_op
def verify_array_op(array):
    # Inicio del método.
    k = []
    # Define un array vacío k, que será usado
    # para guardar el resultado final del método.
    for X in array:
        # Ejecuta el siguiente código por
        # cada elemento dentro del array de entrada.
        if type(X) == int and X >= 0:
            # Si se cumple que el elemento es un número entero positivo
            # (o cero), ejecuta el siguiente código.
            a_int = multiple_op(X)
            # Lleva a cabo el método multiple_op con un número del array,
            # y guarda el resultado en la variable a_int.
            k.append(a_int)
            # Agrega el array obtenido en a_int al array
            # k definido anteriormente.
        else:
            # En caso de que el elemento no sea un un número entero positivo
            # (o cero), se ejecuta el siguiente código.
            return "E-304: Error en tipo de dato ingresado dentro del array."
        # Retorna un mensaje de error.
    return k
# Devuelve el array k, un único array con todos los otros arrays resultantes.

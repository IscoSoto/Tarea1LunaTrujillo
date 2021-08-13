# Ricardo Luna y Javier Trujillo
# Tarea 1
# Archivo de prueba

from metodos import multiple_op
# Importa multiple_op desde archivo de métodos
from metodos import verify_array_op
# Importa verify_array_op desde archivo de métodos
import random
# Importa la librería random de Python.
import math
# Importa la librería math de Python.


def test1():  # Se define la función para probar el caso 1.
    print("Caso de éxito para multiple_op:\n")
    # Salida de texto.
    num = random.randint(1, 10)
    # Genera un número entero aleatorio en el rango de 1 a 10.
    M = multiple_op(num)
    # Aplica el método multiple_op al número aleatorio
    # y guarda el resultado en la variable M.
    print("Número aleatorio:", num, "\nResultado de multiple_op:", M, "\n\n")
    # Salida de texto, indica el número aleatorio y el resultado de multiple_op
    for elemento in M:
        assert type(elemento) == int
    # Verifica que cada elemento dentro del array M sea un número entero.
    assert M[0] == num * num
    # Verifica un resultado correcto para el primer elemento de M.
    assert M[1] == 2 ** num
    # Verifica un resultado correcto para el segundo elemento de M.
    assert M[2] == math.factorial(num)
    # Verifica un resultado correcto para el tercer elemento de M.


def test2():  # Se define la función para probar el caso 2.
    print("Caso de éxito para verify_array_op:\n")
    # Salida de texto.
    n1 = random.randint(1, 10)
    # Genera un número entero aleatorio en el rango de 1 a 10.
    n2 = random.randint(1, 10)
    # Genera un número entero aleatorio en el rango de 1 a 10.
    n3 = random.randint(1, 10)
    # Genera un número entero aleatorio en el rango de 1 a 10.
    AR = [n1, n2, n3]
    # Genera un array con los 3 números aleatorios generados (n1, n2 y n3).
    K = verify_array_op(AR)
    # Aplica el método verify_array_op al array
    # AR y guarda el resultado en la variable K.
    print("Array generado:", AR, "\nResultado de verify_array_op:", K, "\n\n")
    # Salida de texto, indica el array generado con números aleatorios
    # y el resultado del método.
    for array in K:
        # Repite el siguente código para cada array dentro de K.
        for elemento in array:
            assert type(elemento) == int
        # Verifica que cada elemento dentro de cada array sea un número entero.
    assert(K) == [multiple_op(n1), multiple_op(n2), multiple_op(n3)]
    # Verifica resultados correctos dentro de cada array dentro de K.


def test3():  # Se define la función para probar el caso 3.
    print("Caso negativo para multiple_op:\n")
    # Salida de texto.
    var = 'c'
    # Define una variable como una letra.
    N = multiple_op(var)
    # Se ejecuta la función multiple_op con la
    # letra definida anteriormente. El resultado se guarda en la variable N.
    print("Entrada a función:", var, "\nResultado de multiple_op:", N, "\n\n")
    # Salida de texto, con el valor de c y el
    # resultado del multiple_op con dicha variable.
    assert(N) == "E-303: Error en tipo de dato ingresado."
    # Verifica que el valor retornado por multiple_op
    # y guardado en N sea el código de error correcto.


def test4():  # Se define la función para probar el caso 4.
    print("Caso negativo para verify_array_op:\n")
    # Salida de texto.
    AR_2 = ['x', 'y', "xqc"]
    # Crea un array AR_2, que contiene letras y un string.
    L = verify_array_op(AR_2)
    # Ejecuta el método verify_array_op con AR_2, y guarda el resultado en L.
    print("Array generado:", AR_2, "\nResultado de verify_array_op:", L, "\n")
    # Salida de texto, con el valor de AR_2 y el resultado del método.
    assert(L) == "E-304: Error en tipo de dato ingresado dentro del array."
    # Verifica que el valor retornado por verify_array_op
    # y guardado en L sea el código de error correcto.


test1()  # Llamado a la función de prueba 1.
test2()  # Llamado a la función de prueba 2.
test3()  # Llamado a la función de prueba 3.
test4()  # Llamado a la función de prueba 4.

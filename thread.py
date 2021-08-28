import threading
import time
import argparse


# Función para crear la lista con elementos distintos.
def makeList(tam):
    lista = []
    for i in range(0, tam):
        lista.append(i)
    return lista


# Función para ejecutar el recorrido con 1 hilo.
# Se eleva cada elemento del array al cuadrado.
def powOneThread(lista):
    res = []
    for val in lista:
        num = val ** 2
        res.append(num)
        time.sleep(0.01)


# Función para ejecutar el recorrido con 4 hilos.
def powFourThreads(lista):
    ln = len(lista)
    p1 = lista[0:round(ln / 4)]
    p2 = lista[round(ln / 4):round(ln / 2)]
    p3 = lista[round(ln / 2):round(3 * ln / 4)]
    p4 = lista[round(3 * ln / 4):ln]
    t1 = threading.Thread(target=powOneThread, args=(p1,))
    t2 = threading.Thread(target=powOneThread, args=(p2,))
    t3 = threading.Thread(target=powOneThread, args=(p3,))
    t4 = threading.Thread(target=powOneThread, args=(p4,))
    threads = [t1, t2, t3, t4]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


# Flujo principal
# Funciones de argparse, para recibir argumentos
# por la terminal de Linux.
parser = argparse.ArgumentParser(description='Elevar elementos al cuadrado.')
parser.add_argument('X', type=int, help='# de elementos dentro del array')
parser.add_argument('-t', '--txt', action='store_true', help='Guardar en .txt')
args = parser.parse_args()

# Crea la lista con X elementos.
lista = makeList(args.X)

# Inicio de recorrido con 1 hilo.
# El tiempo se guarda en la variable T1.
inicio = time.time()
powOneThread(lista)
fin = time.time()
T1 = fin - inicio

# Inicio de recorrido con 4 hilos.
# El tiempo se guarda en la variable T2.
inicio2 = time.time()
powFourThreads(lista)
fin2 = time.time()
T2 = fin2 - inicio2

# Revisa si se escogió guardar los datos en un .txt.
if args.txt:
    # Guarda datos dentro del .txt.
    file = open('Tiempos.txt', 'w')
    file.write('Tiempo de ejecución con un hilo: ' + str(T1) + ' segundos.\n')
    file.write('Tiempo de ejecución con 4 hilos: ' + str(T2) + ' segundos.\n')
    file.close()
    # Salida en terminal.
    print("Resultados guardados en Tiempos.txt")
else:
    # Si no se desea guardar en .txt, imprime datos en terminal.
    print("Tiempo de ejecución con un hilo: ", T1)
    print("Tiempo de ejecución con 4 hilos: ", T2)

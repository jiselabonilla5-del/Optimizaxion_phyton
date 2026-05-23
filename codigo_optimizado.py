import time
import math
import numpy as np

inicio = time.time()

limite = 100000

numeros = np.arange(2, limite)

def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

primos = [n for n in numeros if es_primo(n)]

fin = time.time()

print("Cantidad de números primos:", len(primos))
print("Tiempo optimizado:", fin - inicio, "segundos")
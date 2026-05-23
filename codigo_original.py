import time

inicio = time.time()

primos = []

for num in range(1, 100000):
    es_primo = True

    if num < 2:
        es_primo = False
    else:
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break

    if es_primo:
        primos.append(num)

fin = time.time()

print("Cantidad de números primos:", len(primos))
print("Tiempo de ejecución:", fin - inicio, "segundos")
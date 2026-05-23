import matplotlib.pyplot as plt

# CAMBIA estos valores por tus tiempos reales
tiempo_original = 96.88313031196594
tiempo_optimizado = 0.5479168891906738

versiones = ["Original", "Optimizado"]
tiempos = [tiempo_original, tiempo_optimizado]

plt.figure(figsize=(6,4))

plt.bar(versiones, tiempos)

plt.title("Comparación de tiempos de ejecución")
plt.xlabel("Versiones")
plt.ylabel("Tiempo (segundos)")

plt.savefig("comparacion_tiempos.png")

plt.show()
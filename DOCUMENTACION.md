# Optimización de Código en Python

## Introducción

En este proyecto se analizó un programa en Python encargado de calcular números primos en un rango de 1 a 100000.

El código original presentaba problemas de rendimiento debido a que realizaba demasiadas iteraciones innecesarias para verificar si un número era primo.

Para mejorar la eficiencia del programa se aplicaron diferentes técnicas de optimización y herramientas de análisis de rendimiento.

---

# Código Original

El algoritmo original verificaba todos los números desde 2 hasta n-1 para determinar si un número era primo.

Esto generaba un tiempo de ejecución elevado debido a la gran cantidad de operaciones realizadas.

Archivo utilizado:

- codigo_original.py

---

# Técnicas de Optimización Aplicadas

Se aplicaron las siguientes mejoras:

## 1. Reducción de Iteraciones

Se optimizó el algoritmo utilizando únicamente divisiones hasta la raíz cuadrada del número.

:contentReference[oaicite:0]{index=0}

Esto disminuyó considerablemente la cantidad de operaciones.

---

## 2. Uso de List Comprehensions

Se utilizó list comprehension para generar listas de manera más eficiente y legible.

Ejemplo:

```python
primos = [n for n in numeros if es_primo(n)]
```

---

## 3. Uso de NumPy

Se utilizó NumPy para trabajar con arrays optimizados y mejorar el rendimiento del procesamiento numérico.

---

# Resultados

| Versión | Tiempo de Ejecución |
|---|---|
| Código Original | PEGAR_TIEMPO |
| Código Optimizado | PEGAR_TIEMPO |

La versión optimizada presentó una mejora significativa en comparación con el código original.

---

# Análisis con cProfile

Se utilizó la herramienta cProfile para analizar el rendimiento del programa y detectar las funciones que consumían más tiempo de ejecución.

Archivos generados:

- profiling_original.txt
- profiling_optimizado.txt

Los resultados mostraron que la validación de números primos era la operación más costosa del programa original.

Después de la optimización, el tiempo de procesamiento se redujo considerablemente.

---

# Gráficos

Se creó un gráfico utilizando Matplotlib para comparar visualmente los tiempos de ejecución entre ambas versiones del código.

Archivo generado:

- comparacion_tiempos.png

---

# Conclusiones

Las optimizaciones aplicadas permitieron mejorar significativamente el rendimiento del programa.

Reducir iteraciones innecesarias, utilizar estructuras más eficientes y apoyarse en librerías como NumPy ayuda a desarrollar aplicaciones más rápidas y eficientes.

El uso de herramientas de profiling como cProfile facilita la identificación de cuellos de botella y permite optimizar el código de manera más efectiva.

---

# Repositorio GitHub

https://github.com/jiselabonilla5-del/Optimizaxion_phyton
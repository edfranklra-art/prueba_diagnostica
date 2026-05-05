# Problema 3: Conjetura de Collatz

Este programa es un demostrador interactivo de la **Conjetura de Collatz** aplicado a un rango de números enteros.

## Funcionamiento
El algoritmo recibe un intervalo [p, q] y, para cada número, aplica las siguientes reglas hasta llegar a 1:
* Si el número es **par**: n = n / 2
* Si el número es **impar**: n = 3n + 1

## Requisitos de la Tarea
Para que la demostración se ejecute, el programa valida la **Regla de Suficiencia**:
> El límite superior **q** debe ser al menos 100 veces el límite inferior **p** (q \geq 100p).

## Instrucciones de ejecución en VS Code

1. Abra la carpeta del proyecto en **Visual Studio Code**.
2. Abra el archivo `problema3.py`.
3. Ejecute el script haciendo clic en el botón **Run Python File** (icono de Play arriba a la derecha) o abra una terminal integrada y escriba:
   ```bash
   python problema3.py
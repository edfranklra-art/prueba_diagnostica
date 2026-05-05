# Problema 2: Validador de Notación FEN

Este script valida si una cadena de texto cumple con el estándar **Forsyth-Edwards Notation (FEN)**.

## Reglas de Validación Aplicadas:
1. **Seis campos obligatorios:** Posición, turno, enroque, captura al paso, reloj de media jugada y número de jugada.
2. **Integridad del tablero:** Verifica que cada una de las 8 filas sume exactamente 8 casillas (contando piezas y espacios vacíos).
3. **Piezas válidas:** Solo acepta `P, N, B, R, Q, K` (blancas) y `p, n, b, r, q, k` (negras).
4. **Campos especiales:** Valida que el turno sea `w/b` y que el enroque/al paso sigan el formato oficial.


## Instrucciones de ejecución en VS Code

1. Abra la carpeta del proyecto en **Visual Studio Code**.
2. Abra el archivo `problema2.py`.
3. Ejecute el script haciendo clic en el botón **Run Python File** (icono de Play arriba a la derecha) o abra una terminal integrada y escriba:
   ```bash
   python problema2.py
def secuencia_collatz(n):
    """Calcula la secuencia de Collatz y la devuelve como una lista."""
    pasos = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos.append(n)
    return pasos

def ejecutar_collatz_interactivo():
    print("=== DEMOSTRACIÓN DE LA CONJETURA DE COLLATZ ===")
    print("Reglas: Si n es par → n/2 | Si n es impar → 3n + 1")
    
    while True:
        print("\n" + "-"*50)
        entrada = input("Presione Enter para iniciar o escriba 'salir': ").lower()
        if entrada == 'salir':
            break
            
        try:
            p = int(input("Ingrese el inicio del intervalo (p): "))
            q = int(input("Ingrese el fin del intervalo (q): "))
            
            # Validación de la regla q >= 100p
            if q < 100 * p:
                print(f"\nNo se puede aplicar la demostración.")
                print(f"Regla: q ({q}) debe ser mayor o igual a 100 * p ({100*p})")
                continue

            print(f"\nEjemplo: {p} ≤ n ≤ {q}")
            
            # Proceso de demostración para cada número n
            for n in range(p, q + 1):
                resultado = secuencia_collatz(n)
                # Convertimos la lista de números a una cadena separada por flechas
                cadena_pasos = " → ".join(map(str, resultado))
                print(f"n={n}: {cadena_pasos}")

            print("\nDemostrado...")

        except ValueError:
            print("ERROR: Ingrese números enteros válidos.")

if __name__ == "__main__":
    ejecutar_collatz_interactivo()
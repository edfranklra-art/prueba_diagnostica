import re

def validar_fen(fen):
    # 1. Dividir los 6 campos
    campos = fen.split(' ')
    if len(campos) != 6:
        return False, "Debe tener exactamente 6 campos separados por espacios."

    posicion, turno, enroque, al_paso, media_jugada, plena_jugada = campos

    # 2. Validar Estructura de la Posición (Campo 1)
    filas = posicion.split('/')
    if len(filas) != 8:
        return False, "La posición debe tener 8 filas separadas por '/'."
    
    for fila in filas:
        suma_casillas = 0
        for char in fila:
            if char.isdigit():
                suma_casillas += int(char)
            else:
                if char.lower() not in 'pnbrqk':
                    return False, f"Pieza inválida encontrada: {char}"
                suma_casillas += 1
        if suma_casillas != 8:
            return False, f"Una fila no suma 8 casillas (suma: {suma_casillas})."

    # 3. Validar Turno (Campo 2)
    if turno not in ['w', 'b']:
        return False, "El turno debe ser 'w' (blancas) o 'b' (negras)."

    # 4. Validar Enroque (Campo 3)
    if not re.match(r'^(KQkq|K?Q?k?q?|-)$', enroque) or enroque == '':
        return False, "Campo de enroque inválido (use KQkq o -)."

    # 5. Validar Al Paso (Campo 4)
    if not re.match(r'^([a-h][36]|-)$', al_paso):
        return False, "Casilla de captura al paso inválida."

    return True, "Formato FEN válido."

# --- Bloque de prueba interactiva ---
if __name__ == "__main__":
    print("--- Validador de Notación FEN ---")
    print("Escribe 'salir' para terminar.")
    
    while True:
        entrada = input("\nIntroduce la cadena FEN: ")
        if entrada.lower() == 'salir': break
        
        es_valido, mensaje = validar_fen(entrada)
        
        if es_valido:
            print(f"Resultado: ✅ {mensaje}")
        else:
            print(f"Resultado: ❌ ERROR: {mensaje}")
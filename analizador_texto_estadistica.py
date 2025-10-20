import string
from collections import Counter

def main():
    print("ANALIZADOR DE TEXTOS CON ESTADÍSTICAS")
    
    while True:
        print("\nOpciones de entrada:")
        print("1. Ingresar texto por consola.")
        print("2. Cargar texto desde archivo.")
        print("3. Salir.")
        
        opcion = input("\nSeleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            texto = ingresar_texto_consola()
        elif opcion == "2":
            texto = leer_archivo()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            continue
            
        if texto:
            procesar_texto(texto)
        else:
            print("No se pudo obtener el texto para analizar.")

def ingresar_texto_consola():
    print("\nIngrese el texto (presione 'Enter'' dos veces para finalizar):")
    lineas = []
    while True:
        linea = input()
        if not linea:
            break
        lineas.append(linea)
    return '\n'.join(lineas)

def leer_archivo():
    nombre_archivo = input("\nIngrese la ruta del archivo: ").strip()
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Error al leer archivo: {str(e)}.")
    return None

def procesar_texto(texto):
    # Limpieza y preparación del texto.
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation))
    palabras = texto_limpio.lower().split()
    
    # Cálculo de estadísticas.
    estadisticas = {
        'caracteres_con_espacios': len(texto),
        'caracteres_sin_espacios': len(texto.replace(' ', '')),
        'total_palabras': len(palabras),
        'palabra_mas_larga': max(palabras, key=len) if palabras else '',
        'frecuencia_palabras': Counter(palabras)
    }
    
    mostrar_resultados(estadisticas)

def mostrar_resultados(estats):
    print("\n")
    print("ESTADÍSTICAS")
    
    print(f"Caracteres totales (con espacios): {estats['caracteres_con_espacios']}")
    print(f"Caracteres totales (sin espacios): {estats['caracteres_sin_espacios']}")
    print(f"Total de palabras: {estats['total_palabras']}")
    print(f"Palabra más larga: '{estats['palabra_mas_larga']}' ({len(estats['palabra_mas_larga'])} caracteres)")
    
    print("\nPalabras más frecuentes:")
    for palabra, freq in estats['frecuencia_palabras'].most_common(10):
        print(f"{palabra}: {freq} ocurrencias")

if __name__ == "__main__":
    main()
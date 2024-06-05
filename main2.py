#!/usr/bin/python3

def son_anagramas(cadena1, cadena2):
    """Inicia la validacion de las cadenas

    Args:
        cadena1 (string): Cadena a comparar
        cadena2 (string): Cadena a comparar

    Returns:
        boolean: True o False
    """
    # Eliminar espacios y convertir las cadenas a minúsculas para ignorar diferencias de mayúsculas/minúsculas y espacios
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()
    
    # Verificar si las longitudes de las cadenas son de diferentes longitudes
    if len(cadena1) != len(cadena2):
        return False
    
    # Contar la frecuencia de cada letra en ambas cadenas usando Counter
    from collections import Counter
    contador1 = Counter(cadena1)
    print (contador1)
    contador2 = Counter(cadena2)
    print (contador2)
    
    # Comparar los contadores si iguales True, caso contrareio False
    return contador1 == contador2

def valida(cadena1, cadena2):
    """Función para inicial la validación

    Args:
        cadena1 (string): Cadena a comparar
        cadena2 (string): Cadena a comparar
    """
    resultado = son_anagramas(cadena1, cadena2)
    print(f'¿Son anagramas "{cadena1}" y "{cadena2}"? {resultado}')

# Ejemplos de uso
##############################################
cadena1 = "Escuchar"
cadena2 = "charsecu"

va = valida(cadena1, cadena2)

##############################################
cadena1 = "Hola"
cadena2 = "Aloh"

va = valida(cadena1, cadena2)

##############################################
cadena1 = "Hola"
cadena2 = "Adios"

va = valida(cadena1, cadena2)

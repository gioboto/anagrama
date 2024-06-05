#!/usr/bin/python3

def validaanagrama(txt1, txt2):
    """Función para inicar la validación ingreando los caracteres de las cadenas a listas

    Args:
        txt1 (string): Cadena de caracteres
        txt2 (string): Cadena de caracteres

    Returns:
        boolean: True o False
    """
    lista1 = []
    lista2 = []
    lista1= list(txt1)
    lista2= list(txt2)
    print(lista1)
    print(lista2)
    lista1.sort()
    lista2.sort()
    res = comparalistas(lista1, lista2)
    return res


def comparalistas(l1, l2):
    """Compara las listas ordenadas (se diferencia mayúsculas y minúsculas)

    Args:
        l1 (list): Lista que contienen los caracteres de la cadena
        l2 (list): Lista que contienen los caracteres de la cadena

    Returns:
        boolean: True o False
    """
    if l1 == l2:
        print("Es anagrama")
        return True
    else:
        print("No es anagrama")
        return False

# Ejemplos de uso
##############################################
cadena1 = "escuchar"
cadena2 = "charsecu"

va = validaanagrama(cadena1, cadena2)
print (va)

##############################################
cadena1 = "Hola"
cadena2 = "Aloh"

va = validaanagrama(cadena1, cadena2)
print (va)
##############################################
cadena1 = "Hola"
cadena2 = "Adios"

va = validaanagrama(cadena1, cadena2)
print (va)
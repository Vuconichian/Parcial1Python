#Desarrollar una función recursiva que permita contar cuantas veces
#aparece una determinada palabra, en un vector de palabras.

def contador_palabra_especifica(vector, palabra):
    if len(vector) == 0:
        return 0
    else:
        if vector[0] == palabra:
            return 1 + contador_palabra_especifica(vector[1:], palabra)
        else:
            return contador_palabra_especifica(vector[1:], palabra) 




vector_de_palabras = ['hola', 'mundo', 'mundo', 'hola', 'hola', 'mundo', 'hola', 'mundo']

palabra_a_contar = 'hola'
total = contador_palabra_especifica(vector_de_palabras, palabra_a_contar)
print(f"{palabra_a_contar} aparece un total de: {total} veces.")

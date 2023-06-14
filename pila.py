
class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

#agrega un dato a la pila
    def push(self, dato):
        self.__elements.append(dato)

#quita un dato de la pila
    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

#devuelve el tamaño de la pila
    def size(self):
        return len(self.__elements)

#devuelve el dato que esta encima de la pila, o sea el ultimo agregado
    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]
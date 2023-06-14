class Lista:
    def __init__(self):
        self.__elements = []

    def criterio_comparacion(self, value, criterio):
        if isinstance(value, (int, str, bool)):
            return value
        else:
            dic_atributos = value.__dict__
            if criterio in dic_atributos:
                return dic_atributos[criterio]
            else:
                print('No se puede ordenar por este criterio')
                return None

    def insert(self, value, criterio=None):
        if criterio is None:
            self.__elements.append(value)
        else:
            if len(self.__elements) == 0 or self.criterio_comparacion(value, criterio) >= self.criterio_comparacion(self.__elements[-1], criterio):
                self.__elements.append(value)
            elif self.criterio_comparacion(value, criterio) < self.criterio_comparacion(self.__elements[0], criterio):
                self.__elements.insert(0, value)
            else:
                index = 1
                while self.criterio_comparacion(value, criterio) >= self.criterio_comparacion(self.__elements[index], criterio):
                    index += 1
                self.__elements.insert(index, value)

    def search(self, search_value, criterio=None):
        if self.size() == 0:
            return None

        position = None
        first = 0
        last = self.size() - 1
        while first <= last and position is None:
            middle = (first + last) // 2
            if search_value == self.criterio_comparacion(self.__elements[middle], criterio):
                position = middle
            elif search_value > self.criterio_comparacion(self.__elements[middle], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def search_r(self, search_value, first, last, criterio=None):
        if first > last:
            return None

        middle = (first + last) // 2
        if search_value == self.criterio_comparacion(self.__elements[middle], criterio):
            return middle
        elif search_value > self.criterio_comparacion(self.__elements[middle], criterio):
            return self.search_r(search_value, middle + 1, last, criterio)
        else:
            return self.search_r(search_value, first, middle - 1, criterio)

    def delete(self, value, criterio=None):
        if self.size() == 0:
            return None

        pos = self.search(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
            return return_value
        else:
            return None

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def order_by(self, criterio=None, reverse=False):
        if self.size() == 0:
            return

        dic_atributos = self.__elements[0].__dict__
        if criterio in dic_atributos:
            self.__elements.sort(key=lambda valor: valor.__dict__[criterio], reverse=reverse)
        else:
            print('No se puede ordenar por este criterio')

    def get_element_by_value(self, value):
        if self.size() == 0:
            return None

        pos = self.search(value)
        if pos is not None:
            return self.__elements[pos]
        else:
            return None

    def get_element_by_index(self, indice):
        if self.size() == 0 or indice < 0 or indice >= self.size():
            return None

        return self.__elements[indice]

    def set_value(self, value, new_value, criterio=None):
        if self.size() == 0:
            return

        pos = self.search(value, criterio)
        if pos is not None:
            self.__elements.pop(pos)
            self.insert(new_value, criterio)
# Dada una lista con nombres de personajes de la saga de Avengers ordenados por nombre del superhéroes, 
#de los cuales se conoce: nombre del superhéroe, nombre del personaje (puede ser vacio), grupo al que (perteneces puede ser vacio),
# año de aparición, por ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
#Resolver las siguientes tareas:
# a. Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje;
# b. Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e indicar cuantos son.
# c. Mostrar de manera descendente los superhéroes que pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de la galaxia”.
# d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960.
# e. Hemos detectado que la superhéroe “Black Widow” está mal cargada por un error de tipeo, figura como “Vlanck Widow”, modifique 
#dicho superhéroe para solucionar este problema.
# f. Dada una lista auxiliar con los siguientes personajes (‘BlackCat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
#información), agregarlos a la lista principal en el caso de no estar cargados.
# g. Mostrar todos los personajes que comienzan con C, P o S.
# h. Cargue al menos 20 superheroes a la lista.

from cola import Cola
from lista import Lista

class Superheroe:
    def __init__(self, nombre_superheroe, nombre_personaje, grupo, anio_aparicion):
        self.nombre_superheroe = nombre_superheroe
        self.nombre_personaje = nombre_personaje
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion

lista_superheroes = Lista()

lista_superheroes.insert(Superheroe('Mole Man', 'Ben Grimm', 'Los cuatro fantásticos', 1961))
lista_superheroes.insert(Superheroe('Mujer invisible', 'Susan Storm', 'Los cuatro fantásticos', 1961))
lista_superheroes.insert(Superheroe('Sr Fantastico', 'Reed Richards', 'Los cuatro fantásticos', 1961))
lista_superheroes.insert(Superheroe('Antorcha Humana', 'Johnny Storm', 'Los cuatro fantásticos', 1961))
lista_superheroes.insert(Superheroe('Capitana Marvel', 'Carol Danvers', 'Vengadores', 1968))
lista_superheroes.insert(Superheroe('Star-Lord', 'Peter Jason Quill', 'Guardianes de la galaxia', 1976))
lista_superheroes.insert(Superheroe('Groot', 'Groot', 'Guardianes de la galaxia', 1969))
lista_superheroes.insert(Superheroe('Drax', 'Arthur Douglas', 'Guardianes de la galaxia', 1973))
lista_superheroes.insert(Superheroe('Vlanck Widow', 'Natalia Alianovna', 'Los vengadores', 2010))


# Punto A
capitana_marvel_found = False
nombre_personaje = None

for i in range(lista_superheroes.size()):
    heroe = lista_superheroes.get_element_by_index(i)
    if heroe.nombre_superheroe == 'Capitana Marvel':
        capitana_marvel_found = True
        nombre_personaje = heroe.nombre_personaje
        break

if capitana_marvel_found:
    print(f"A. Capitana Marvel está en la lista. Su nombre de personaje es: {nombre_personaje}")
else:
    print("A. Capitana Marvel no está en la lista.")

# Punto B
cola_guardianes = Cola()
for indice in range(lista_superheroes.size()):
    heroe = lista_superheroes.get_element_by_index(indice)
    if heroe.grupo == 'Guardianes de la galaxia':
        cola_guardianes.arrive(heroe.nombre_superheroe)

cantidad_guardianes = cola_guardianes.size()
print(f"B. En el grupo 'Guardianes de la galaxia' hay {cantidad_guardianes} superhéroes.")

# Punto C
grupos = ['Los cuatro fantásticos', 'Guardianes de la galaxia']
for grupo in grupos:
    print(f"C. Superhéroes del grupo '{grupo}':")
    lista_superheroes.order_by(criterio='nombre_superheroe', reverse=True)
    for indice in range(lista_superheroes.size()):
        heroe = lista_superheroes.get_element_by_index(indice)
        if heroe.grupo == grupo:
            print(heroe.nombre_superheroe)

# Punto D
print("D. Superhéroes con nombres de personajes que aparecieron después de 1960:")
lista_superheroes.order_by(criterio='anio_aparicion')
for indice in range(lista_superheroes.size()):
    heroe = lista_superheroes.get_element_by_index(indice)
    if heroe.nombre_personaje != '' and heroe.anio_aparicion > 1960:
        print(heroe.nombre_superheroe)

# Punto E
posicion_vlanck = lista_superheroes.search('Vlanck Widow', criterio='nombre_superheroe')
if posicion_vlanck is not None:
    lista_superheroes.get_element_by_index(posicion_vlanck).nombre_superheroe = 'Black Widow'

# Punto F
lista_auxiliar = [
    ('Black cat', 'Felicia Sara Hardy', 'Vengadores', 1979),('Hulk', 'Bruce Banner', 'Vengadores', 1962),('Loki', 'Loki Laufeyson', 'Gigantes de Hielo', 1949),
    ('Rocket Raccoon', 'Rocket Raccoon', 'Guardianes de la galaxia', 1979)]
for personaje in lista_auxiliar:
    nombre_superheroe = personaje[0]
    if lista_superheroes.search(nombre_superheroe, criterio='nombre_superheroe') is None:
        lista_superheroes.insert(Superheroe(*personaje))

# Punto G
print("G. Personajes que empiezan con C, P o S:")
lista_superheroes.order_by(criterio='nombre_personaje')
for indice in range(lista_superheroes.size()):
    heroe = lista_superheroes.get_element_by_index(indice)
    nombre_personaje = heroe.nombre_personaje
    if nombre_personaje != '' and nombre_personaje[0] in ['C', 'P', 'S']:
        print(nombre_personaje)

# Punto H
lista_superheroes.insert(Superheroe('Chamber', 'Vincent Fabron', 'Centinelas', 2021))
lista_superheroes.insert(Superheroe('Viper', 'Sabine Callas', 'Controladores', 2022))
lista_superheroes.insert(Superheroe('Omen', 'Wraith', 'Controladores', 2021))
lista_superheroes.insert(Superheroe('Raze', 'Tayane Alves', 'Duelistas', 2022))
lista_superheroes.insert(Superheroe('Gekko', 'Mateo Armendáriz De la Fuente', 'Iniciadores', 2023))
lista_superheroes.insert(Superheroe('Yoru', 'Ryo Kiritani', 'Duelistas', 2022))
lista_superheroes.insert(Superheroe('Skye', 'Kirra Foster', 'Iniciadores', 2021))
lista_superheroes.insert(Superheroe('Sage', 'Lingying Wei ', 'Centinelas', 2022))
lista_superheroes.insert(Superheroe('Brimstone', 'Liam Byrne', 'Controladores', 2021))
lista_superheroes.insert(Superheroe('Breach', 'Erik Torsten', 'Iniciadores', 2022))
lista_superheroes.insert(Superheroe('Phoenix', 'Jamie Adeyemi', 'Duelistas', 2021))
lista_superheroes.insert(Superheroe('Reyna', 'Zyanya Mandrogón', 'Duelistas', 2022))
lista_superheroes.insert(Superheroe('Killjoy', 'Klara Böhringer', 'Centinelas', 2021))
lista_superheroes.insert(Superheroe('Sova', 'Sasha Novikov ', 'Iniciadores', 2022))
lista_superheroes.insert(Superheroe('Jett', 'Sunwoo Han', 'Duelistas', 2021))
lista_superheroes.insert(Superheroe('Neon', 'Tala Nicole Dimaapi Valdez', 'Duelistas', 2022))
lista_superheroes.insert(Superheroe('Astra', 'Efia Danso', 'Controladores', 2021))
lista_superheroes.insert(Superheroe('Harbour', 'Varun Batra', 'Controladores', 2022))
lista_superheroes.insert(Superheroe('Cypher', 'Amir El Amari ', 'Centinelas', 2021))
lista_superheroes.insert(Superheroe('Kay-O', '', 'Iniciadores', 2022))

print(f"H. La lista contiene {lista_superheroes.size()} Superheroes.")

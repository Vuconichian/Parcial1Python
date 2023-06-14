from pila import Pila

pila = Pila()

pila.push({"planeta": "Marte", "capturado": "Jabba the Hutt", "recompensa": 500})
pila.push({"planeta": "Pluton", "capturado": "Lando Calrissian", "recompensa": 300})
pila.push({"planeta": "Saturno", "capturado": "No hubo capturas", "recompensa": 0})
pila.push({"planeta": "Jupiter", "capturado": "Han Solo", "recompensa": 3000})
pila.push({"planeta": "Venus", "capturado": "Yoda", "recompensa": 100})
pila.push({"planeta": "Urano", "capturado": "Luke Skywalker", "recompensa": 1000})
pila.push({"planeta": "Neptuno", "capturado": "Mace Windu", "recompensa": 400})
pila.push({"planeta": "Mercurio", "capturado": "No hubo capturas", "recompensa": 0})

# Punto A
print("A. Planetas visitados:")
pila_temp = Pila()
while pila.size() > 0:
    mision = pila.pop()
    print(mision["planeta"])
    pila_temp.push(mision)
pila = pila_temp

# Punto B
creditos_totales = 0
pila_temp = Pila()
while pila.size() > 0:
    mision = pila.pop()
    creditos_totales += mision["recompensa"]
    pila_temp.push(mision)
pila = pila_temp
print("B. Total de créditos:", creditos_totales)

# Punto C
numero_de_mision = None
planeta_de_captura = None
pila_temp = Pila()
while pila.size() > 0:
    mision = pila.pop()
    if mision["capturado"] == "Han Solo":
        numero_de_mision = pila_temp.size() + 1
        planeta_de_captura = mision["planeta"]
    pila_temp.push(mision)
pila = pila_temp

if numero_de_mision is not None:
    print("C. Han Solo fue capturado en la misión número", numero_de_mision)
    print("Planeta de la captura:", planeta_de_captura)
else:
    print("C. No se encontró la misión en la que capturó a Han Solo.")

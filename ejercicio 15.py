
from lista import Lista

lista_entrenadores = Lista()

entrenadores = [ {"nombre": "Juan","torneos_ganados": 2, "batallas_perdidas":6 ,"batallas_ganadas": 25, "pokemons" : Lista() },
                 {"nombre": "Maria","torneos_ganados":8, "batallas_perdidas": 9,"batallas_ganadas": 20,"pokemons" : Lista() },
                 {"nombre": "Pedro","torneos_ganados":12, "batallas_perdidas": 8,"batallas_ganadas": 31,"pokemons" : Lista() }
            ]

pokemons = [{"nombre":"Tyrantrum", "nivel": 12 ,"tipo":"fuego", "subtipo":"planta", "entrenador": "Juan" },
            {"nombre":"Wingull", "nivel": 180 ,"tipo":"agua","subtipo":"volador", "entrenador": "Juan"},
            {"nombre":"Wolverine", "nivel":3  ,"tipo":"fuego"  ,"subtipo":"terreno", "entrenador": "Pedro" },
            {"nombre":"Tyrantrum"  , "nivel": 12 ,"tipo":"fuego"  ,"subtipo":"planta", "entrenador": "Maria" },
            {"nombre":"Wingull" , "nivel": 18 ,"tipo":"agua"  ,"subtipo":"volador", "entrenador": "Pedro" },
            {"nombre":"Tyrantrum"  , "nivel": 12 ,"tipo":"fuego"  ,"subtipo":"planta", "entrenador": "Maria" },
            {"nombre":"Gigante" , "nivel": 21 ,"tipo":"agua","subtipo":"volador", "entrenador": "Juan" },
            {"nombre":"Rayo" , "nivel":3  ,"tipo":"fuego"  ,"subtipo":"terreno", "entrenador": "Pedro" }
]


for entrenador in entrenadores:
    lista_entrenadores.insertar(entrenador, 'nombre')

for pokemon in pokemons:
    pos = lista_entrenadores.busqueda(pokemon['entrenador'], 'nombre')
    if(pos > -1):
        del pokemon['entrenador']
        lista_entrenadores.obtener_elemento(pos)['pokemons'].insertar(pokemon, 'nombre')

#Punto A
buscado = input('Ingrese nombre de entrenador a buscar ')
pos = lista_entrenadores.busqueda(buscado,'nombre')
if (pos > -1 ):
    print('La cantidad de pokemons del entrenador es ',lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio())
print()

#Punto B
for i in range (lista_entrenadores.tamanio()):
    pos = lista_entrenadores.obtener_elemento(i)
    if (pos["torneos_ganados"] > 3):
        print("El entrenador ", pos["nombre"], " ha ganado mas de 3 torneos.")
print()

#Punto C
maximo = 0 
pos_maximo = -1

for i in range(lista_entrenadores.tamanio()):
    if(lista_entrenadores.obtener_elemento(i)['torneos_ganados'] > maximo):
        maximo = lista_entrenadores.obtener_elemento(i)['torneos_ganados'] 
        pos_maximo = i

entrenador_max = lista_entrenadores.obtener_elemento(pos_maximo)
print("El entrenador con mayor cantidad de torneos ganados es: ")
print(entrenador_max['nombre'])
print()

nivel_maximo = 0
pos_maximo2 = -1

for i in range(entrenador_max["pokemons"].tamanio()):
    if(entrenador_max["pokemons"].obtener_elemento(i)["nivel"] > nivel_maximo):
        nivel_maximo = entrenador_max["pokemons"].obtener_elemento(i)["nivel"]
        pos_maximo2 = i

pokemon_max = entrenador_max["pokemons"].obtener_elemento(pos_maximo2)
print("El pokemon de mayor nivel del entrenador con mayor cantidad de torneos ganados es : ")
print(pokemon_max['nombre'])
print()

#Punto D 
buscado = input('Ingrese nombre del entrenador para ver sus pokemons: ')
pos = lista_entrenadores.busqueda(buscado,'nombre')
if (pos > -1 ):
    print('pokemons del entrenador : ',buscado)
    lista_entrenadores.obtener_elemento(pos)['pokemons'].barrido()
print()

#Punto E 
mayor_batallas = ""
for i in range(lista_entrenadores.tamanio()):
    pos = lista_entrenadores.obtener_elemento(i)
    total = (pos["batallas_ganadas"]+ pos["batallas_perdidas"])
    if (((pos["batallas_ganadas"]/total)*100) > 79):
        mayor_batallas += (pos["nombre"] + "  ")
print ("Entrenadores cuyo porcentaje de batallas ganados sea mayor al 79%:  ", mayor_batallas)

print()
# Punto F 
cont_fuego_planta = ""
cont_agua_volador= ""
for i in range (lista_entrenadores.tamanio()):
    pos1 = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda("fuego","tipo")
    if (pos1 > -1):
        pos2 = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda("planta","subtipo")
        if (pos2 > -1):
            cont_fuego_planta += (lista_entrenadores.obtener_elemento(i)["nombre"]+ "  ")

for i in range (lista_entrenadores.tamanio()):
    pos1 = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda("agua","tipo")
    if (pos1 > -1):
        pos2 = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda("volador","subtipo")
        if (pos2 > -1):
            cont_agua_volador += (lista_entrenadores.obtener_elemento(i)["nombre"]+ "  ")      


print("Entrenadores que tienen pokemons de tipo fuego y subtipo planta: ",cont_fuego_planta)
print("Entrenadores que tienen pokemons de tipo agua y subtipo volador: ",cont_agua_volador)
print()

#Punto G 
cont_nivel = 0
cant_pokemons = 0
buscado = input('Ingrese nombre del entrenador para ver el promedio de nivel sus pokemons: ')
pos = lista_entrenadores.busqueda(buscado,'nombre')
if (pos > -1 ):
    for i in range(lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio()):
        cont_nivel += lista_entrenadores.obtener_elemento(pos)['pokemons'].obtener_elemento(i)["nivel"] 
        cant_pokemons += 1


print("El promedio de nivel de los pokemons del entrenador", buscado, " es de ", cont_nivel/cant_pokemons,"%")
print()

#Punto H 
cont_pokemon = 0
buscado = input("Ingrese el nombre del pokemon ")
for i in range(lista_entrenadores.tamanio()):
    pos = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda(buscado,"nombre")
    if (pos > -1):
        cont_pokemon +=1

print("La cantidad de entrenadores que tienen al pokemon ",buscado," son ",cont_pokemon)
print()

#Punto I. 
entrenadores_aux = []
for i in range(lista_entrenadores.tamanio()):
    entrenador = lista_entrenadores.obtener_elemento(i)
    for j in range(lista_entrenadores.obtener_elemento(i)["pokemons"].tamanio()):
        pokemon = lista_entrenadores.obtener_elemento(i)["pokemons"].obtener_elemento(j)
        for k in range (j+1,lista_entrenadores.obtener_elemento(i)["pokemons"].tamanio()):
            pokemon_aux = lista_entrenadores.obtener_elemento(i)["pokemons"].obtener_elemento(k)
            if(pokemon_aux['nombre'] == pokemon['nombre']):
                if(entrenador['nombre'] not in entrenadores_aux):
                    entrenadores_aux.append(entrenador['nombre'])
                    break

print("Los entrenadores que tienen pokemon repetidos son : ", entrenadores_aux)
print()
#Punto J 
cont_tyrantrum = ""
cont_terrakion = ""
cont_wingull = ""
for i in range (lista_entrenadores.tamanio()):
    pos1 = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda("Tyrantrum","nombre")
    pos2 = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda("Te-rrakion","nombre")
    pos3 = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda("Wingull","nombre")
    if (pos1 > -1):
        cont_tyrantrum += (lista_entrenadores.obtener_elemento(i)["nombre"]+ "  ")
    if (pos2 > -1):
        cont_terrakion += (lista_entrenadores.obtener_elemento(i)["nombre"]+ "  ")
    if (pos3 > -1):
        cont_wingull += (lista_entrenadores.obtener_elemento(i)["nombre"]+ "  ")

print("Entrenadores que tienen el pokemon Tyrantrum: ", cont_tyrantrum)
print("Entrenadores que tienen el pokemon Terrakion: ", cont_terrakion)
print("Entrenadores que tienen el pokemon Wingull: ", cont_wingull)
print()
#Punto K 
buscado1 = input("Ingrese el nombre del entrenador ")
buscado2 = input("Ingrese el nombre del pokemon ")
pos1 = lista_entrenadores.busqueda(buscado1,"nombre")
pos2 = lista_entrenadores.obtener_elemento(pos1)["pokemons"].busqueda(buscado2,"nombre")

if (pos1 > -1 and pos2 > -1):
    print ("El entrenador ",buscado1," si tiene el pokemon ",buscado2)
else:
    print ("El entrenador ",buscado1," no tiene el pokemon ",buscado2)


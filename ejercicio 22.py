from lista import Lista

lista_jedi = Lista()

jedis = [
                {'nombre': 'Aayla Secura','maestros': "Qui-Gon Jin" ,'colores_sables_usados': ['rojo',"azul"],'especie':'humana'},
                {'nombre': 'Wolverine','maestros': "Yoda" ,'colores_sables_usados': ['amarillo'] ,'especie':'humana'},
                {'nombre': 'Ahsoka Tano','maestros': "Luke Skywalker" ,'colores_sables_usados': ['verde'] ,'especie':'twilek'},
                {'nombre': 'Dr Strange','maestros': "Luke Skywalker" ,'colores_sables_usados': ['violeta'] ,'especie':'otra'},
                {'nombre': 'Capitana Marvel','maestros': "Mace Windu" ,'colores_sables_usados': ['naranja',"gris"] ,'especie':'twilek'},
                {'nombre': 'Kit Fisto','maestros': "Yoda" ,'colores_sables_usados': ['rosa',"blanco" ],'especie':'humana'},
                {'nombre': 'Flash','maestros': "Mace Windu" ,'colores_sables_usados': ['violeta'] ,'especie':'otra'},
                {'nombre': 'Star-Lord','maestros': "Luke Skywalker",'colores_sables_usados': ['amarillo'] ,'especie':'humana'}
            ]

for jedi in jedis:
    lista_jedi.insertar(jedi, 'nombre')

#Punto A
lista_jedi.barrido_jedi()
print()

#Punto B
print("Informacion de Ahsoka Tano y Kit Fisto:")
for i in range(lista_jedi.tamanio()):
    pos = lista_jedi.obtener_elemento(i)
    if (pos["nombre"] == "Ahsoka Tano"):
        print(pos)
    if (pos["nombre"] == "Kit Fisto"):
        print(pos)
print()

#Punto C 
aprendiz_yoda = ""
aprendiz_luke = ""
for i in range (lista_jedi.tamanio()):
    pos = lista_jedi.obtener_elemento(i)
    if (pos["maestros"] == "Yoda"):
        aprendiz_yoda += (pos["nombre"]+ "  ")
    if (pos["maestros"] == "Luke Skywalker"):
        aprendiz_luke += (pos["nombre"]+ "  ")    

print("Los Padawan de Yoda son: ", aprendiz_yoda)
print("Los Padawan de Luke Skywalker son: ", aprendiz_luke)
print()

#Punto D 
especie_humana = ""
especie_twilek = ""
for i in range (lista_jedi.tamanio()):
    pos = lista_jedi.obtener_elemento(i)
    if (pos["especie"] == "humana"):
        especie_humana += (pos["nombre"]+ "  ")
    if (pos["especie"] == "twilek"):
        especie_twilek += (pos["nombre"]+ "  ")    

print("Los Jedi de especie humana son: ", especie_humana)
print("Los Jedi de especie twilek son: ", especie_twilek)
print()

#Punto E. 
cont_a = ""
for i in range (lista_jedi.tamanio()):
    pos = lista_jedi.obtener_elemento(i)
    if (pos['nombre'][0] == 'A'):
        cont_a += (pos['nombre']+'  ')

print("Los jedi que comienzan con A son : ", cont_a)
print()

#Punto F
cont_luz =""
for i in range (lista_jedi.tamanio()):
    pos = lista_jedi.obtener_elemento(i)
    if (len(pos["colores_sables_usados"]) > 1):
        cont_luz += (pos["nombre"]+ "  ") 
print("Los Jedi que utilizaron sable de luz de mas de un color: ",cont_luz)
print()

#Punto G
luz_amarilla = ""
luz_violeta = ""
for i in range (lista_jedi.tamanio()):
    pos = lista_jedi.obtener_elemento(i)
    if (pos["colores_sables_usados"] == ["amarillo"]):
        luz_amarilla += (pos["nombre"]+ "  ")
    if (pos["colores_sables_usados"] == ["violeta"]):
        luz_violeta += (pos["nombre"]+ "  ")    

print("Los Jedi que utilizaron sable de luz amarilla son: ",luz_amarilla)
print("Los Jedi que utilizaron sable de luz violeta son : ", luz_violeta) 

#Punto H
aprendiz_quigon = ""
aprendiz_mace = ""
for i in range (lista_jedi.tamanio()):
    pos = lista_jedi.obtener_elemento(i)
    if (pos["maestros"] == "Qui-Gon Jin"):
        aprendiz_quigon += (pos["nombre"]+ "  ")
    if (pos["maestros"] == "Mace Windu"):
        aprendiz_mace += (pos["nombre"]+ "  ")    

print("Los Padawan de Qui-Gon Jin son: ", aprendiz_quigon)
print("Los Padawan de Mace Windu son: ", aprendiz_mace)
print()
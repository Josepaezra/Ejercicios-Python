n = 9            # 
Binario=[]                 #Crea Lista con todas las posibles combinaciones de n partidas, con numeros binarios
for i in range(2**n): 
    b = bin(i)[2:]
    l = len(b)
    b = str(0) * (n - l) + b
    Binario.append(b) 
    
#print(Juegos)
Tres_Ganados=[]
for i in range(len(Binario)):
    if Binario[i].find("111") != -1:                #Verifica que 1 hayan ganado tres partidas
        buscar= Binario[i].find("111") +1
        if Binario[i].find("111", buscar) == -1:    #Verifica que no haya ganado tres partidas antes

            if Binario[i].find("000", buscar) == -1:        #Verifica que 0 no haya tenido tres partidas ganadas antes
                Tres_Ganados.append(Binario[i])
print(Tres_Ganados)


print(len(Tres_Ganados))



#Verifica que No sea una variación de una partida ya ganada (considerada)
# Itero sobre los elementos de la lista, tomo uno,  busco posicion de la victoria, tomo los digitos a la derecha de la ultima victoria en ese elemento, incluida esta, y la anexo a una lista si, 
# ninuno de los anteriores elementos de la lista tenian  el mismo patron en la misma posicion
Tres_Ganados_def = [Tres_Ganados[0]]
for i in range(1,len(Tres_Ganados)):
    posicion_victoria = Tres_Ganados[i].find("111")
    digitos = Tres_Ganados[i][posicion_victoria:]
    contador = 0
    for j in range(1,i):
        if Tres_Ganados[j][posicion_victoria:] != digitos :
            contador +=1
        if contador == (i-1):
            Tres_Ganados_def.append(Tres_Ganados[i])


            
print(Tres_Ganados_def)

print(len(Tres_Ganados_def))



"""
posicion_victoria = Tres_Ganados[3].find("111")
digitos = Tres_Ganados[3][posicion_victoria:]
print(posicion_victoria)
print(digitos)

"""

#print(len( range(1,1) ))
"""
for i in range(1,0):
    print(1543)

"""



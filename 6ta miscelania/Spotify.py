'''Lista tipo spotify
ACCIONES
-Anexar artista
-Anexar cancion
-La cancion debe tener genero y duracion

-Buscar artista
-Buscar cancion
-Eliminar artista
-Ordenar alfabeticamente
-El que tiene mas canciones
'El que tiene la cancion mas larga
'El que tiene la cancion mas corta'''

spotify={'artista':[],
          'cancion':[],
          'genero':[],
          'duracion':[],}
 
def artista(spotify):
    while True:
        artista=input('Ingresa tu artista o presiona 1 para ejecutar otra accion: ')
        if artista =='1':
            break
        if artista not in spotify['artista']:
            spotify['artista'].append(artista)
        if artista == spotify['artista']:
            print('El artista ya se encuentra en spotify',spotify['artista'])
            break
    return spotify
#print(artista(spotify))

def cancion(spotify):
    print(spotify['artista'])
    artista1=input('¿A cual artista desea anexarle una cancion? ')
    if artista1 in spotify['artista']:
        cancion1=input('Ingresa una cancion del anterior artista ')
        genero=input('Ingresa el genero de la cancion anterior ')
        duracion=float(input('Ingresa la duracion de la cancion ' ))
        spotify['cancion'].append(cancion1)
        spotify['genero'].append(genero)
        spotify['duracion'].append(duracion)
    elif artista1 not in spotify['artista']:
        print('El artista no se encuentra en spotify')
    return spotify
#print(cancion(spotify))

def buscar_artista(spotify):
    artista2=input('¿Cual artista deseas buscar? ')    
    for i in spotify['artista']:
        if i in artista2:
            print('El artista buscado se encuentra en spotify',spotify['artista'])
    return spotify
#print(buscar_artista(spotify))

def buscar_cancion(spotify):
    cancion2=input('¿Cual cancion deseas buscar? ')    
    for i in spotify['cancion']:
        if i in cancion2:
            print('La cancion buscada se encuentra en spotify',spotify['cancion'])
        else:
            print('La cancion buscada no se encuentra en Spotify')
    return spotify
#print(buscar_cancion(spotify))

def eliminar_artista(spotify):
    eliminar=int(input('¿Que artista deseas eliminar?, los artistas estan enumerados desde el numero 0 '))
    spotify['artista'].pop(eliminar)
    return spotify
#print(eliminar_artista(spotify))

def ordenar(spotify):
    ordenar=sorted(spotify['artista'])
    print('Los artistas ordenados son', ordenar)
    return spotify
#print(ordenar(spotify))

def cancion_mas_larga(spotify):
    larga=max(spotify['duracion'])
    print('La cancion con la duracion mas larga es de ',larga,'minutos')
    return spotify
#print(cancion_mas_larga(spotify))

def cancion_mas_corta(spotify):
    corta=min(spotify['duracion'])
    print('La cancion con la duracion mas corta es de ',corta,'minutos')
    return spotify
   
#print(cancion_mas_corta(spotify))

def listaMenu():
    print('1-Anexar Artista')
    print('2-Anexar Cancion')
    print('3-Buscar Artista')
    print('4-Buscar Cancion')
    print('5-Eliminar Artista')
    print('6-Ordenar Artistas')
    print('7-Cancion mas larga')
    print('8-Cancion mas corta')
    print('0-Salir')
    menu=int(input('Bienvenido a Spotify, ingresa un numero '))
    
while True:
    match menu:  
        case 1:
            artista(spotify)
                v=input('Desea agregar otro artista: si/no ')
                if v =='si':
                    continue
                else:
                    print('Gracias ',spotify)
                    listaMenu()
        case 2:
            cancion(spotify)
            v=input('Desea agregar otra cancion: si/no ')
            if v =='si':
                continue
            else:
                print('Gracias ',spotify)
                listaMenu()
        case 3:
                buscar_artista(spotify)
                v=('Desea buscar otro artista: si/no ')
                if v =='si':
                    continue
                else:
                    print('Gracias ',spotify)
                    listaMenu()
            case 4:
                buscar_cancion(spotify)
                v=('Desea buscar otra canción: si/no ')
                if v =='si':
                    continue
                else:
                    print('Gracias ',spotify)
                    listaMenu()
            case 5:
                eliminar_artista(spotify)
                v=('Desea eliminar otro artista: si/no ')
                if v =='si':
                    continue
                else:
                    print('Gracias ',spotify)
                    listaMenu()
            case 6:
                ordenar(spotify)
                v=input('Desea volver al menu si/no ')
                if v=='si':
                    listaMenu()
                else: 
                    break
            case 7:
                cancion_mas_larga(spotify)
                v=input('desea volver al menu si/no ')
                if v=='si':
                    listaMenu()
                else: 
                    break
            case 8:
                cancion_mas_corta(spotify)
                v=input('Desea volver al menu si/no ')
                if v=='si':
                    listaMenu()
                else: 
                    break
            case _:
                print('Gracias por usar Spotify')
                exit()

listaMenu()
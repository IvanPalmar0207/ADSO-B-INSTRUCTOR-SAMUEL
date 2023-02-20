'''-Determinar en que tiempo esta 
conjugado un verbo
'''
def pasado(strr):
    pasado=['é','aste','ó','amos','aron','í','iste','ió','imos','ieron','ió']
    for i in pasado:
        if strr.endswith(i):
            print('La palabra',strr,'esta congugada en pasado')
            break
def presente(strr):
    presente=['o','as','es','a','e','amos','emos','os','an','en']
    for i in presente:
        if strr.endswith(i):
            print('La palabra',strr,'esta congugada en presente')
            break
def futuro(strr):    
    futuro=['aré','arás','ará','aremos','aréis','arán','eré','erás','erá','eréis','erán','iré','irás','irá','remos','réis','ráis','iráis','iráis','irán']
    for i in futuro:
        if strr.endswith(i):
            print('La palabra',strr,'esta congugada en futuro')
            break
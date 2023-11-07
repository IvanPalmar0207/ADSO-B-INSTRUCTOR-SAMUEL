'''
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te 
devuelve Verdadero si el nombre de usuario es “Lionel Messi” y la contraseña es “Campeon”. Además
recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login 
incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente 
hacer login, solamente tenemos tres oportunidades para intentarlo.
'''

def login(usuario,contraseña,intentos):
    intentos = 0
    if usuario.upper() == 'LIONEL MESSI' and contraseña.upper() == 'CAMPEON':
        return True
    else:
        intentos+=1
        return False
    
print('-'*20,'INICIAR SESION','-'*20)    
print()

intentos = 0                    
while True:
    if intentos<3:
        usuario = input('Cual es el usuario?\n-')
        contraseña = input('Cual es la contraseña?\n-')
        intentos+=1
        if login(usuario,contraseña,intentos) == True:
            print('Bienvenido al sistema señor usuario')
            break
        else:
            continue
    else:
        print('Ya no tienes mas intentos')                        
        break
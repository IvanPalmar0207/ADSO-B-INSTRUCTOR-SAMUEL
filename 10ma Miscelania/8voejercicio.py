'''-Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula 
matemática para este fin.'''
def cesar(palabra,cifrado):
    cesar=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','A','B','C','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']
    cesar_vacio=[]
    for i in palabra:
        if i in cesar:
            index=cesar.index(i)
            total=cesar[index+cifrado]
            cesar_vacio.append(total)   
    print('Palabra cifrada:',cesar_vacio)
    print('Palabra no cifrada:',palabra)
#Esto es un ejemplo de ejecucion:)
palabra=input('¿Cual es tu palabra\n-')
cifrado=int(input('¿Cuanto desplazamiento deseas en las letras de tu palabra?\n-'))
cesar(palabra,cifrado)
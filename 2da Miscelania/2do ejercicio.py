'''Escribir un programa que pida tres numeros y que
escriban si son los tres iguales, si hay dos iguales 
o si son los 3 distintos''' 

n1=int(input("Digita el primer numero: "))
n2=int(input("Digita el segundo numero: "))
n3=int(input("Digita el tercer numero: "))
if n1!=n2==n3:
    print("Existen dos numeros iguales")
elif n2!=n3==n1:
    print("Existen dos numeros iguales")
elif n3!=n2==n1:
    print("Existen dos numeros iguales")    
elif n1==n3==n2:
    print("Los tres numeros son iguales")
elif n1!=n2!=n3:
    print("Ninguno de los numeros es igual")                
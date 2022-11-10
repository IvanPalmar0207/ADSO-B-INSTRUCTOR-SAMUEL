'''Solicitar al usuario un número de hasta 9 dígitos e
imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576'''
num=int(input("Ingrese un numero: "))
num2=num
r_num=0
while num>0:
    num3=num%10
    r_num=r_num*10+num3
    num=num//10
print(r_num)
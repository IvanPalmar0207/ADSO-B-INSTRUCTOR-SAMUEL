'''Pedir numeros e indicar cual de ellos es el valor del
medio'''

x=int(input("Digita el primer numero: "))
y=int(input("Digita el segundo numero: "))
z=int(input("Digita el tercer numero: "))

if x>y and y>z: 
    print(y)        
elif z > y and y > x: 
    print(y)   
elif z>x and x>y:
    print(x)
elif y>x and x>z:
    print(x)
elif x>z and z>y:
    print(z)    
elif y>z and z>x:
    print(z)      
from cgi import print_exception
from re import X
import string
from time import pthread_getcpuclockid
from tkinter import N


print('!HOLA, MUNDO!')
print()
print('IVAN DAVID PALMAR MARTINEZ')
print()
print('HOLA HIJUEPUTAS') 
print()
print('SAPOS GONORREAS') 
print()
print('MALPARIDOS')

print("La witsi witsi araña\nsubio a su telaraña.\n")
print()
print('Vino la lluvia y\nse la llevo.\n')

print('njnj\nlklklko')

print('\\')

print("la witsi witsi","araña","subio a su telaraña")
print("Mi nombre es, Python")
print("Monty Python")
print("Mi nombre es, python. ",end="")
print("Monty Python.")

print("MI","NOMBRE","ES","MONTY","PYTHON",sep="-")

print("MI","NOMBRE","ES", sep="_", end="*")
print("MONTY", "PYTHON.", sep="*", end="*\n")

print("Fundamentos","Programacion","en",sep="***",end="...")
print("Python")

print("    *\n")
print("   * *\n")
print("  *   *\n")
print(" *     *\n")
print("***   ***\n")
print("  *   *\n")
print("  *   *\n")
print("  *****\n")

print("    *"*2)
print("   * *"*2)
print("  *   *"*2)
print(" *     *"*2)
print("***   ***"*2)
print("  *   *"*2)
print("  *   *"*2)
print("  *****"*2)


#LITERALES EN SI MISMOS

#Argumento numerico
print("2")
#Numero entero
print(2)
#Numero entero negativo
print(-111111111)
#Numero octal
print(0o123 )
#Numero hexdecimal
print(0x123)
#Numero decimal
print(2.5,4.0,0.4)

print(3*10**8)
print(0.0000000000000000000001)

#Cadenas
print('Me gusta "Monty Python"')
print("I'm Monty Python.")
print('I\'m Monty Python.')

#boleanos
print(True>False)
print(True<False)

#LABORATORIO
print("\"Estoy\"\n","\"\"Aprendiendo\"\"\n","\"\"\"Python\"\"\"" )
print(2+2)
print(4*20)

#Potencia
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#Multiplicacion
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#division
print(6/3)
print(6/3.)
print(6./3)
print(6./3.)

#Division entera
print(6//3)
print(6//3.)
print(6.//3)
print(6.//3.)

print(6//4)
print(6.//4)

print(6/4)
print(-6//4)
print(6.//-4)
print(12 % 4.5)

#suma
print(-4+4)
print(-4.+8)

#resta
print(-4-4)
print(4.-8)
print(-1.1)

#operadores y sus prioridades
print(2+3*5)
#enlaces
print(9%6%2)

print(2**2**3)

print(2*3%5)

print((5*((25%13)+100)/(2*13))//2)
print((2**4),(2*4.),(2*4))
print((-2/4),(2/4),(2//4),(-2//4))
print((2%-4),(2%4),(2**3**2))

#variables
var=1
print(var)

#Variables utlizando
var=1
account_balance=1000.0
client_name='John Doe'
print(var,account_balance, client_name)
print(var)

var="3.8.5"
print("version de python: "+var)

var=1
print(var)
var=var+1
print(var)

var=100
var=200+300
print(var)

#matematica simple
a=3.0
b=4.0
c=(a**2+b**2)**0.5
print("c=", c)

#laboratorio
juan=3
maria=5
adan=6
print(juan, maria, adan)
total_manzanas=juan+maria+adan
print("Numero total de manzanas: ",total_manzanas)

x= 2 ** 2
print(x)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.6
kilometers_to_miles = kilometers /1.6

print(miles, "millas son", round(miles_to_kilometers, 2), "kilometros")
print(kilometers, "kilometros son", round(kilometers_to_miles, 2), "millas")

x=-1
x = float(x)
y=3*x**3-2*x**2+3*x-1
print("y =", y)

a='1'
b="1"
print(a+b)

a = 6
b = 3
a /= 2 * b
print(a)

# este programa calcula los segundos segun las horas digitadas
# este programa fue escrito hace dos días

hora = 3 # Horas
segundos = 3600 # número de segundos en una hora

print("Horas: ", hora) #imprime el numero de horas
print("Segundos en la hora: ", hora * segundos) # se imprime el numero de segundos en determinado numero de horas
print("¡ADIOS!")
#este el es fin del programa que calcula el numero de segundos en las horas que tu desees

print("Dime algo")
anything = input()
print("Mmmm...", anything, "....¿enserio?")

# Probando mensajes de error.

anything = input("Inserta un número: ")
something = anything ** 2.0
print(anything, "al cuadrado es", something)

print("Como se llama?")
nombre=input()
print("me alegro de conorcerte,{nombre}")
anything = float(input("Inserta un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)

leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + fnam + " " + lnam + ".")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))















#LAB INPUT

a=float(input("ingresa un valor aqui para la variable a "))
b=float(input("Ingresa un valor aqui para la variable b "))

print("Resultado de la suma:",a+b)
print("Resultado de la resta:", a-b)
print("Resultado de la multiplicacion:", a*b)
print("Resultado de la division:", a/b)

print("\n!Eso es todo amigos¡")

x=float(input("Ingresa el valor para x: "))
y=1/(x+1/(x+1/(x+1/x)))
print("y= ", y)

print(1//2*3)

x=input()
y=int(input())
print(x*y)

z=y=x=1
print(x,y,z,sep="*")

x=int(input(2))
y=int(input(4))

print(x+y)

x=int(input())
y=int(input())

x= x % y
x= x % y 
y= y % x
print(y)

x=1
y=2
z=x
x=y
y=z
print(x,y)

x= int(input())
y= int(input())

x=x//y
y=y//x
print(y)

print(1/1)

x=input()
y=input()
print(x+y)

x=1/2+3//3+4**2
print(x)
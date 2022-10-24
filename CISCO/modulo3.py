#Igualdad
a=5
b=4
print(a==b)

var = 0   # asignando 0 a var
print(var == 0)

var = 1  # asignando 1 a var
print(var == 0)

#Desigualdad
a=5
b=8
print(a!=b)

a=2
b=2
print(a!=b)

climafuera=2
climafuera > 0
print("El clima es perfecto", climafuera)

n=int(input("Escribe el numero: "))
n=n>=100
print(n)

#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir a la línea 02
    
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

x = "1"

if x == 1:
    print("uno")
elif x == "1":
    if int(x) > 1:
        print("dos")
    elif int(x) < 1:
        print("tres")
    else:
        print("cuatro")
if int(x) == 1:
    print("cinco")
else:
    print("seis")



# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande
print("El número más grande es:", largest_number)
for i in range(10):
    print("El valor de i es actualmente", i)


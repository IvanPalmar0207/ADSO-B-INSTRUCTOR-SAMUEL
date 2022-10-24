a=float(input("Ingresa un valor numerico a : "))
b=float(input("Ingresa un valor numerico b : "))
c=float(input("Ingresa un valor numerico c : "))

x1=-b-(b**2-4*a*c)*0.5/2*a
x2=-b+(b**2-4*a*c)*0.5/2*a

print("El primer valor de la formula cuadratica es: ", x1)
print("El segundo valor de la formula cuadratica es: ", x2)
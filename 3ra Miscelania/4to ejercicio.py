'''Determinar cuales y cuantos numeros perfectos hay entre 1 y 1000'''
for i in range(2, 1000+1):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        print("%s es perfecto" %i)
print("Son 3 numeros perfectos antes del numero 1000")
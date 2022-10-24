'''un obrero necesita calcular su salario semanal, el cual 
se obtiene de la siguienta manera: -Si trabaja 40 horas o menos se le pagara
$2600 por cada hora, -Si trabaja mas  de 40 horas se le paga $2600
por cada una de las primeras 40 horas y $5000 por hora extra'''


hora=float(input("Ingresa la cantidad de horas trabajadas: "))

salario=hora*2600

salario2=salario+5000-2600

salario3=salario+5000

salario4=salario+7600

if hora <= 80:
        print("Tu salario semanal es de: ", salario, "pesos")
elif hora==81:
        print("Tu salario semanal es de: ", salario2, "pesos") 
elif hora==82:
        print("Tu salario semanal es de: ", salario3, "pesos")   
elif hora==83:
        print("Tu salario semanal es de: ", salario4, "pesos")
elif hora==84:
        print("Tu salario semanal es de: ", salario4, "pesos")  
else:
    print("Una persona no puede trabajar tantas horas semanales")      


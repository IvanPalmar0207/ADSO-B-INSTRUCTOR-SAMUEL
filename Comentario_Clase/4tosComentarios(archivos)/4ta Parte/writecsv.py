import csv #Se usa la palabra reservada imposrt que sirve para importar un modulo propio de python o un modulo creado por el programador, y se importa el modulo csv que trae incorporado todas las funcionalidades que sirve para manipulas archivos csv.
header=['Fruit','Price'] #Se crea una variable local que se llama header y que contiene una lista con dos valores, el primero es fruit y el segundo es price.
rows=[['Apple',1200],
      ['Berry',2000],
      ['Lemon',1000],
      ['Melon',3000],
      ['Grapes',4000],
      ['Pear',2000]]

with open ('4ta Parte/example.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)

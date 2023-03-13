
import csv
diccio=[
    {'name':'Alice','age':18},
    {'name':'Bob','age':19},
    {'name':'John','age':17}
]
header=['name','age']

with open('4ta Parte/people.csv','w') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=header)
    writer.writeheader()
    writer.writerows(diccio)
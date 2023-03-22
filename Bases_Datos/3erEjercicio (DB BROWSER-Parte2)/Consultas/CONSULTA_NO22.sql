/*Listar todos los datos de los automotores cuya poliza expira en
septiembre de 2013, es reporte debe visualizar la placa, el modelo, la marca,
numero de pasajeros, cilindraje, nombre de automotor, el valor de la poliza
y el valor asegurado*/

SELECT aut.placa_aut,aut.modelo_aut,aut.marca_aut,aut.pasajeros_aut,
aut.cilindraje_aut, tpaut.nombre_aut, ase.valorAseguradora_ase,
ase.costo_ase FROM tb_automotores as aut INNER JOIN tb_tipoAutomotores as tpaut
on aut.tipo_aut=tpaut.tipo_aut INNER JOIN tb_aseguramientos as ase
on aut.placa_aut=ase.placa_aut;
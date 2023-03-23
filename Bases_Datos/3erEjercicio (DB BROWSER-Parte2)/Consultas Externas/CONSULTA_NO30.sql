/*Visualizar los datos de las polizas de los automotores tipo 1,
este reporte debe incluir placa, marca, modelo, cilindraje del vehiculo junto
con la fecha de inicio, de finalizacion y estado de la poliza*/

select aut.placa_aut, aut.marca_aut, aut.modelo_aut, aut.cilindraje_aut,
ase.fechaInicio_ase, ase.fechaExpiracion_ase, ase.estado_ase FROM
tb_automotores as aut LEFT JOIN tb_aseguramientos as ase
on aut.placa_aut=ase.placa_aut WHERE aut.tipo_aut=1;
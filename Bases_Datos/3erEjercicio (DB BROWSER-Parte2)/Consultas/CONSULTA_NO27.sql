/*Visualizar los incidentes del vehiculo con placas "FLL420", este reporte
debe visualizar la fecha, el lugar, la cantidad de heridos del incidente,
la fecha de inicio, la fecha de expiracion de la poliza y el valor aseguradora.*/

SELECT inc.fecha_inc,inc.lugar_inc,inc.heridos_inc, ase.fechaInicio_ase,
ase.fechaExpiracion_ase,ase.valorAseguradora_ase FROM tb_incidentes as inc
left JOIN tb_aseguramientos as ase on inc.placa_aut=ase.placa_aut 
WHERE inc.placa_aut ='FLL420';
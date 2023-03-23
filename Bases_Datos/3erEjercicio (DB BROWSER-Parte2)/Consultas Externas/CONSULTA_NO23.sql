/*Visualizar los datos de los incidentes ocurridos el 30 de septiembre de 
2012, con su respectivo numero de poliza, fecha de inicio de la poliza,
valor asegurado y valor de la poliza*/

SELECT inc.codigo_inc,inc.fecha_inc,inc.placa_aut,inc.lugar_inc,inc.heridos_inc
,inc.fatalidades_inc,inc.involucrados_inc, ase.codigo_ase,ase.fechaInicio_ase,
ase.valorAseguradora_ase, ase.costo_ase FROM tb_aseguramientos as ase 
LEFT JOIN tb_incidentes as inc on ase.placa_aut=inc.placa_aut WHERE 
inc.fecha_inc='2012-09-30';
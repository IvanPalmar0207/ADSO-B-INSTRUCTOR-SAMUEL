/*Vizsualizar los datos de los incidentes un (1) herido, este reporte
debe visualizar la placa del automotor, con los respectivos datos de la poliza
como son fecha de inicio, valor, estado y valor asegurado*/
 
SELECT inc.codigo_inc,inc.fecha_inc,inc.placa_aut,inc.lugar_inc,inc.heridos_inc
,inc.fatalidades_inc,inc.involucrados_inc, inc.placa_aut, ase.fechaInicio_ase,
ase.costo_ase, ase.estado_ase, ase.valorAseguradora_ase FROM tb_incidentes
as inc LEFT JOIN tb_aseguramientos as ase on inc.placa_aut=ase.placa_aut
WHERE inc.heridos_inc=1;
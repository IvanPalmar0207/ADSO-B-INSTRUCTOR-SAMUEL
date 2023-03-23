/*Visualizar los incidentes con el minimo numero de autos involucrados,
de este incidente visualizar el estado de la poliza y el valor
asegurado*/
select inc.codigo_inc, inc.fecha_inc, inc.placa_aut, inc.lugar_inc, inc.heridos_inc
, inc.fatalidades_inc, min(inc.involucrados_inc) as involucrados_inc, 
ase.estado_ase, ase.valorAseguradora_ase FROM tb_incidentes as inc 
left JOIN tb_aseguramientos as ase on inc.placa_aut=ase.placa_aut;
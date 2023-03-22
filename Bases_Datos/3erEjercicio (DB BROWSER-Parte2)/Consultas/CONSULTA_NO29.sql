/*Visualizar los datos de la poliza cuyo valor asegurado es el mas costoso
, este reporte ademas de visualizar todos los datos de la poliza, debe
presentar todos los datos del vehiculo que tien dicha poliza*/

SELECT ase.codigo_ase, ase.fechaInicio_ase, ase.fechaExpiracion_ase,
max(ase.valorAseguradora_ase) as valorAseguradora_ase, ase.estado_ase,
ase.costo_ase, aut.placa_aut, aut.marca_aut, aut.tipo_aut, aut.modelo_aut,
aut.pasajeros_aut, aut.cilindraje_aut, aut.chasis_aut FROM tb_aseguramientos
as ase LEFT JOIN tb_automotores as aut on ase.placa_aut=aut.placa_aut;
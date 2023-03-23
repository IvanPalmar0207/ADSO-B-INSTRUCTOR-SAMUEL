/*Visualizar todos los datos de la poliza mas costoza*/
SELECT codigo_ase,fechaInicio_ase,fechaExpiracion_ase,max(valorAseguradora_ase)
as valorAseguradora_ase,estado_ase,costo_ase,placa_aut
FROM tb_aseguramientos;
/*Visualizar el nombre, apellido y direccion de todos aquellos clientes que haya
realizado un pedido el dia 25/02/2012*/

SELECT cli.nom_cli,ape_cli,cli.dir_cli,ped.fec_ped 
FROM tb_pedido as ped INNER JOIN tb_cliente as cli
on ped.id_cli=cli.id_cli WHERE ped.fec_ped='25/02/2012';
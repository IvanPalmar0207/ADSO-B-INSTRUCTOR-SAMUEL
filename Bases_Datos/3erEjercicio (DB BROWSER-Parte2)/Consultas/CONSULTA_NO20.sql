/*Visualizar los pedidos que se han realizado para el articulo con id 2,
el listado debe mostrar el nombre y direccion del cliente, el 
 numero de pedido y cantidad solicitada*/
 
 SELECT cli.nom_cli,cli.ape_cli,cli.dir_cli,artped.id_ped, artped.cantidadArticulo_artp
 FROM tb_articuloPedido as artped INNER JOIN tb_pedido as ped
 on artped.id_ped=ped.id_ped INNER JOIN tb_cliente as cli
 on ped.id_cli=cli.id_cli WHERE artped.id_art=2;
/*Visualizar los datos del pedido 1, incluyendo el nombre del cliente, la direccion
del mismo, el nombre y el valor de los articulos que tiene dicho pedido*/

SELECT ped.id_ped,cli.nom_cli,cli.dir_cli,art.tit_art,pre_art,ped.val_ped
FROM tb_pedido as ped INNER JOIN tb_cliente as cli
on ped.id_cli=cli.id_cli INNER JOIN tb_articulo as art
on ped.id_ped=art.id_art WHERE ped.id_ped=1;
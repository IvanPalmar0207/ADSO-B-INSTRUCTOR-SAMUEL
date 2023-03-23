/*Listar todos los pedidos realizados incluyendo el nombre del articulo*/
SELECT ped.id_ped,ped.id_cli,art.tit_art,art.pre_art as valorUnidad,ped.fec_ped,ped.val_ped
FROM tb_pedido as ped LEFT JOIN tb_articulo as art
on ped.id_ped=art.id_art;
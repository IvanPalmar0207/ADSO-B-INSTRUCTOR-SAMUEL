/*Visualizar el nombre del cliente, la fecha y el valor del pedido mas costos*/
SELECT cli.nom_cli,ped.fec_ped,max(ped.val_ped) as val_ped
FROM tb_cliente as cli LEFT JOIN tb_pedido as ped
on cli.id_cli=ped.id_cli;
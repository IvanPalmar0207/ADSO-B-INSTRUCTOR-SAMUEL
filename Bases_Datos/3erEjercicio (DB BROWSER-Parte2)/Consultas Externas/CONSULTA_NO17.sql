/*Mostrar los pedidos con los respectivos articulos (codigo, nombre, valor
y cantidad pedida)*/

SELECT art.id_art,tit_art,pre_art,artped.cantidadArticulo_artp,
artped.valorVentaArticulo_artp FROM tb_articuloPedido as artped
INNER JOIN tb_articulo as art on artped.id_art=art.id_art GROUP by art.id_art;
/*Muestre el nombre del profesor con menor sueldo*/
SELECT nom_pro,ape_pro,min(sal_pro) as sal_pro FROM tb_profesor;
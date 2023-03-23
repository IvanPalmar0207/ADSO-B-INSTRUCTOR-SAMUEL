/*Muestre el nombre y la edad del estudiante mas joven*/
SELECT nom_estu, min(edad_estu) as edad_estu FROM tb_estudiante;
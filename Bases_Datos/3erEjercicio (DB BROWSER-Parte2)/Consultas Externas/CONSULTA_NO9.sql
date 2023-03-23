/*Visualizar todos los estudiantes (codigo y nombre) que iniciaron cursos el 
01/02/2011, del curso debe mostrarse el nombre, las horas y el valor
*/

SELECT estucur.fechaIncio_estcur,estu.doc_estu,
estu.nom_estu,cur.nom_cur,cur.hor_cur,cur.val_cur
FROM tb_estudianteExCurso as estucur INNER JOIN tb_estudiante as estu
on estucur.doc_est=estu.doc_estu INNER JOIN tb_curso as cur
on estucur.cod_cur=cur.cod_cur WHERE estucur.fechaIncio_estcur='01/02/2011';
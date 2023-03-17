CREATE TABLE Profesor(
pro_Id INTEGER PRIMARY KEY,
pro_Nombre VARCHAR(100),
pro_Documento INTEGER,
pro_Email VARCHAR (100),
pro_Telefono INTEGER,
pro_Genero VARCHAR (100)
);

INSERT INTO Profesor VALUES (1,'Bulma',3213123,'Bulma@gmail.com',13123123,'Masculino');
INSERT INTO Profesor VALUES (2,'Vegeta',3213123,'Vegeta@gmail.com',3443124,'Masculino');
INSERT INTO Profesor VALUES (3,'Milk',31231241,'Milk@gmail.com',3143241,'Femenino');
INSERT INTO Profesor VALUES (4,'Lunch',412312,'Lunch@gmail.com',3214314,'Femenino');
INSERT INTO Profesor VALUES (5,'Krillin',43123123,'Krillin@gmail.com',231324132,'Masculino');
INSERT INTO Profesor VALUES (6,'Freezer',21341231,'Frezzer@gmail.com',4366564443,'Masculino');
INSERT INTO Profesor VALUES (7,'Cell',3412312,'Cell@gmail.com',5435312,'Masculino');
INSERT INTO Profesor VALUES (8,'Boo',43241231,'Boo@gmail.com',10324234,'Masculino');
INSERT INTO Profesor VALUES (9,'Gohan',513425636,'Gohan@gmail.com',12242354,'Masculino');
INSERT INTO Profesor VALUES (10,'Yamcha',63535467,'Yamcha@gmail.com',32121231909,'Masculino');

SELECT * FROM Profesor;

DELETE FROM Profesor WHERE pro_Id = '4';
DELETE FROM Profesor Where pro_Nombre = 'Yamcha';

SELECT pro_Id,pro_Nombre FROM Profesor Where pro_Genero = 'Femenino';
SELECT pro_Id,pro_Nombre FROM Profesor Where pro_Genero = 'Masculino';

ALTER TABLE Profesor DROP COLUMN pro_Genero;

SELECT * FROM Profesor;

UPDATE Profesor SET pro_Nombre='Messi',pro_Email='Messi@gmail.com' WHERE pro_Id = 9;

SELECT * FROM Profesor;  


Create TABLE Estudiante(
estu_Id INTEGER PRIMARY KEY 
);

ALTER TABLE Estudiante ADD estu_Nombre VARCHAR(50);

ALTER TABLE Estudiante ADD estu_Documento INTEGER;

ALTER TABLE Estudiante ADD estu_Email VARCHAR (100);

ALTER TABLE Estudiante ADD estu_Edad INTEGER;

ALTER TABLE Estudiante ADD estu_Genero VARCHAR (30);

ALTER TABLE Estudiante ADD estu_Estrato INTEGER;

ALTER TABLE Estudiante ADD estu_Telefono INTEGER;

INSERT INTO Estudiante VALUES (1,'Miguel',3213123,'Miguel@gmail.com',12,'Masculino',1,321312312);
INSERT INTO Estudiante VALUES (2,'David',3213123,'David@gmail.com',34,'Masculino',2,4213123);
INSERT INTO Estudiante VALUES (3,'Andrea',31231241,'Andrea@gmail.com',54,'Femenino',1,4322131);
INSERT INTO Estudiante VALUES (4,'Elena',412312,'Elena@gmail.com',99,'Femenino',4,3213123);
INSERT INTO Estudiante VALUES (5,'Johana',43123123,'Johana@gmail.com',23,'Femenino',3,321312);
INSERT INTO Estudiante VALUES (6,'Messi',4341231,'Messielmejor@gmail.com',43,'Masculino',5,312431);
INSERT INTO Estudiante VALUES (7,'goku',3412312,'Goku@gmail.com',32,'Masculino',3,432123);
INSERT INTO Estudiante VALUES (8,'Drake',43241231,'Drake@gmail.com',100,'Masculino',2,341124);
INSERT INTO Estudiante VALUES (9,'Sullivan',513425636,'Sullivan@gmail.com',122,'Masculino',4,321432);
INSERT INTO Estudiante VALUES (10,'Sekiro',63535467,'Sekiro@gmail.com',321,'Masculino',5,1312321);

SELECT * FROM Estudiante;

UPDATE Estudiante SET estu_Nombre='Chloe',estu_Email='Chloe@gmail.com' WHERE estu_Id = 1;
UPDATE Estudiante SET estu_Nombre='Nathan',estu_Estrato=6 WHERE estu_Id = 8;

SELECT * FROM Estudiante;
SELECT * FROM Estudiante WHERE estu_Estrato BETWEEN 3 And 5;
SELECT estu_Id,estu_Nombre, estu_Edad FROM Estudiante WHERE estu_edad BETWEEN 30 AND 50;
SELECT estu_Id, estu_Nombre, estu_Documento FROM Estudiante ORDER BY estu_Documento;
SELECT * FROM Estudiante WHERE estu_Nombre LIKE 'D%';
SELECT * FROM Estudiante;

DELETE FROM Estudiante WHERE estu_Id = 9;

SELECT * FROM Estudiante; 


CREATE TABLE Curso(
cur_Id INTEGER PRIMARY KEY,
cur_Nombre VARCHAR (50),
cur_Tipo VARCHAR (70),
cur_Metodologia VARCHAR (60),
cur_IntensidadSemanal INTEGER,
cur_IdAprendiz INTEGER,
cur_IdProfesor INTEGER,
cur_IdRegional INTEGER,
FOREIGN KEY (cur_IdAprendiz) REFERENCES Estudiante(estu_Id),
FOREIGN KEY (cur_IdProfesor) REFERENCES Profesor(pro_Id)
);

ALTER TABLE Curso DROP COLUMN cur_IdRegional;

INSERT INTO Curso VALUES (1,'Psicologia','Profesional','Virtual',48,1,3);
INSERT INTO Curso Values (2,'Recreacion y Deportes','Tecnico','Presencial',30,4,2);
INSERT INTO Curso Values (3,'Leyes','Profesional','Mixto','50 horas',5,7);
INSERT INTO Curso Values (4,'Ingenieria Industrial','Profesional','Presencial',48,6,8);
INSERT INTO Curso Values (5,'Ingenieria Civil','Profesional','Virtual',50,9,1);
INSERT INTO Curso Values (6,'Ciencias Aplicadas','Maestria','Mixto',30,10,2);
INSERT INTO Curso Values (7,'Artes','Maestria','Presencial',35,1,9);
INSERT INTO Curso Values (9,'Ingenieria de Sistemas','Tecnologo','Virtual',45,2,10);
INSERT INTO Curso Values (10,'Recursos Humanos','Tecnologo','Mixto',30,5,9);

UPDATE Curso SET cur_Tipo='Profesional' Where cur_Id = 1; 
UPDATE Curso SET cur_Metodologia='Presencial',cur_Tipo='Profesional' WHERE cur_Id=9;

SELECT * FROM Curso;
SELECT cur_Nombre FROM Curso;
SELECT cur_Id,cur_Nombre,cur_Tipo FROM Curso WHERE cur_Tipo = 'Profesional';
SELECT * FROM Curso WHERE cur_Metodologia = 'Virtual';
SELECT cur_Nombre,cur_IntensidadSemanal FROM Curso ORDER BY cur_Nombre;
SELECT * FROM Curso WHERE cur_Nombre LIKE '%s';
SELECT * FROM Curso;

DELETE FROM Curso WHERE cur_Nombre ='Artes';
DELETE FROM Curso Where cur_Id = 10;

SELECT * FROM Curso;

DROP TABLE Curso;
DROP TABLE Estudiante;
DROP TABLE Profesor;
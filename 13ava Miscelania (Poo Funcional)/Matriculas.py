class registrar:
    def __init__(self,id,nombre,edad,contacto,nombreuse,contraseña):
        self.__id=id
        self.__nombre=nombre
        self.__edad=edad
        self.__contacto=contacto
        self.__nombreuse=nombreuse
        self.__contraseña=contraseña
    def gid(self):
        return self.__id
    def sid(self,id):
        self.__id=id
    def gnombre(self):
        return self.__nombre
    def snombre(self,nombre):
        self.__nombre=nombre
    def gedad(self):
        return self.__edad
    def sedad(self,edad):
        self.__edad=edad
    def gcontacto(self):
        return self.__contacto
    def scontacto(self,contacto):
        self.__contacto=contacto
    def gnombreuse(self):
        return self.__nombreuse
    def snombreuse(self,nombreuse):
        self.__nombreuse=nombreuse
    def gcontraseña(self):
        return self.__contraseña
    def scontraseña(self,contra):
        self.__contraseña=contra
class materia:
    c=0
    def __init__ (self,id,nombre,descripcion,instructor,horario):
        self.__id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.instructor=instructor
        self.horario=horario
        self.__class__.c+=1
    def getidm(self):
        return self.__id
    def getNombrem(self):
        return self.nombre
    def getdescripcionm(self):
        return self.descripcion
    def getinstructorm(self):
        return self.instructor
    def gethorariom(self):
        return self.horario
class instructor(registrar):
    c=0
    def __init__(self,id,nombre,edad,contacto,nombreuse,contraseña,credenciales):
        super().__init__(id,nombre,edad,contacto,nombreuse,contraseña)
        self.__credenciales=credenciales
        self.materia=[]
        self.geteliminar=[]
        self.consulta=[]
        self.__class__.c+=1
    def gcredenciales(self):
        return self.__credenciales
    def scredenciales(self,creden):
        self.__credenciales=creden
    def delmateria(self,materia1):
        self.geteliminar.append(materia1)
        del self.geteliminar
    def geliminar(self):
        return self.geteliminar
    def agregarmateria(self,ma):
        self.materia.append(ma)
    def gmateria(self):
        return self.materia
    def consultarmate(self,ma1):
        self.consulta.append(ma1)
    def getconsulta(self):
        return self.consulta
    def newacta(self,ins):
        self.acta.append(ins)
    def getacta(self):
        return self.acta
'Ejemplo de ejecucion'
#ob=instructor('yo',18,32,1232312,'43423qd','dwdad','yosoyprofe')
#ma1=materia(1,'ciencia','hola','samuel','6horas')
#ob.consultarmate(ma1)
#for i in ob.getconsulta():
#print(i.getidm())
class inscripcion:
    def __init__(self,id,detalles,requisitos,finicio,ffin):
        self.id=id
        self.detalles=detalles
        self.requisitos=requisitos
        self.finicio=finicio
        self.ffin=ffin
    def gid(self):
        return self.id
    def gdetalles(self):
        return self.detalles
    def grequisitos(self):
        return self.requisitos
    def gfinicio(self):
        return self.finicio
    def gffinal(self):
        return self.finicio
    def sid(self,id):
        self.id=id
    def sdetalles(self,detalles):
        self.detalles=detalles
    def srequisitos(self,requisitos):
        self.requisitos=requisitos
    def sfinicio(self,inicio):
        self.finicio=inicio
    def sffin(self,fin):
        self.ffin=fin

class estudiante(registrar):
    c=0
    def __init__(self,id,nombre,edad,contacto,nombreuse,contraseña,curso):
        super().__init__(id,nombre,edad,contacto,nombreuse,contraseña)
        self.__curso=curso
        self.inscripcion=[]
        self.acta1=[]
        self.__class__.c+=1
    def gcurso(self):
        return self.__curso
    def scurso(self,curso):
        self.__curso=curso
    def realizarincripcion(self,inscripcion):
        self.inscripcion.append(inscripcion)
    def ginscripcion(self):
        return self.inscripcion
    def acta(self,ins1):
        self.acta1.append(ins1)
    def gacta(self):
        return self.acta1
        
'Ejemplo de ejecucion No1'
#est=estudiante(1,'ivan',18,3214344449,'Ivan_Palmar','Teresa0205.','Adso')
#ins=inscripcion(23,'admitido','Bachillerato','hoy','mañana')
#est.realizarincripcion(ins)
#for i in est.ginscripcion():
#    print(i.gid())
'Ejemplo de ejecucion No2'
#print(est.gcurso())
#print(ob.delmateria(est))
#print(est.gcurso())

class curso:
    c=0
    def __init__(self,id,descripcion,fechainicio,nivelacademico,nombre):
        self.id =id
        self.descripcion = descripcion
        self.fechainicio = fechainicio
        self.nivelacademico = nivelacademico        
        self.nombre = nombre
        self.curso = []
        self.inscripcion=[]
        self.tecnico=[]
        self.tecnologo=[]
        self.profesional=[]
        self.maestria=[]
        self.__class__.c+=1

    def getidc(self):
        return self.id
    def getDescripcionc(self):
        return self.descripcion
    def getFechainicioc(self):
        return self.fechainicio
    def getNivelacademicoc(self):
        return self.nivelacademico
    def getNombrec(self):
        return self.nombre
    def agregarmateria(self,id,nombre,descripcion,instructor,horario):
        ma=materia(id,nombre,descripcion,instructor,horario)
        self.curso.append(ma)
    def getmateria(self):
        return self.curso
    def cinscripcion(self,id,detalles,requisitos,finicio,ffin):
        ins=inscripcion(id,detalles,requisitos,finicio,ffin)
        self.inscripcion.append(ins)
    def ginscripcion(self):
        return self.inscripcion
    def agruparc(self):
        if curso.getNivelacademicoc()=='Tecnico' or curso.getNivelacademicoc()=='tecnico':
            self.tecnico.append(self.id)
            return self.tecnico
        elif curso.getNivelacademicoc()=='Tecnologo' or curso.getNivelacademicoc()=='tecnologo':
            self.tecnologo.append(self.id)
            return self.tecnologo
        elif curso.getNivelacademicoc()=='Profesional' or curso.getNivelacademicoc()=='tecnologo':
            self.profesional.append(self.id)
            return self.profesional
        elif curso.getNivelacademicoc()=='Maestria' or curso.getNivelacademicoc()=='maestria':
            self.maestria.append(self.id)
            return self.maestria

'Ejemplo de ejecucion'
#curso=curso(1,'Desarrollaremos una solucion para un sistema hotelero','10/30/1002','tecnico','adsito')
#curso.cinscripcion(2, 'hola', 'Terminar el bachillerato', 'hoy', 'mañana')
#print(curso.agruparc())
#curso.agregarmateria(1,'arquitectura','Diseñaremos la arquitectura del proyecto','Miguel Gomez','12horas')
#curso.agregarmateria(2,'programacion','Diseñaremos el backen del proyecto','Samuel Padilla','18horas')
#for i in curso.ginscripcion():
#    print(i.gid(),i.gdetalles(),i.grequisitos(),i.gfinicio(),i.gffinal())

class acta:
    c=0
    def __init__(self, id, detalles, fechacreacion):
        self.id = id
        self.detalles = detalles
        self.fechacreacion = fechacreacion
        self.curso=[]
        self.__class__.c+=1
    def getid(self):
        return self.id
    def getdetalles(self):
        return self.detalles
    def getfechacreacion(self):
        return self.fechacreacion
    def getprecio(self):
        return self.precio
    def pagos(self,cursito):
        if cursito.getNivelacademicoc()=='Tecnico' or cursito.getNivelacademicoc() == 'tecnico':
            print('El curso que cursaras es de nivel tecnico y en nuestra institucion es completamento gratuito')
        elif cursito.getNivelacademicoc()=='Tecnologo' or cursito.getNivelacademicoc() == 'tecnologo':
            print('El curso que cursaras es de nivel tecnologo y en nuestra institucion es completamente gratuito')
        elif cursito.getNivelacademicoc()=='Profesional' or cursito.getNivelacademicoc() == 'profesional':
            print('El curso tiene un precio de 5millones el semestre, contado que son 10 semestres, el precio final seria de 50millones')
        elif cursito.getNivelacademicoc()=='Mestria' or cursito.getNivelacademicoc() == 'mestria':
            print('La maestria en nuestra institucion tiene unvalor de 40 millones de pesos.')

'Ejemplo de ejecucion No1'
#es=estudiante(1 ,'ivan', 18, 3214344449, 'Ivan_Palmar07', 'Teresa0205.', 'ADSO')
#ac=acta(1, 'hola','hoy')
#es.acta(ac)
#for i in es.gacta():
#    print(i.getid())

'Ejemplo de Ejecucion No2'
#curso=curso(1,'Desarrollaremos una solucion para un sistema hotelero','10/30/1002','Tecnologo','adsito')
#acta=acta(1,'Esta es la acta del curso No1','9/1/1002')
#acta.pagos(curso)
#curso1=curso(1,'Desarrollaremos una solucion para un sistema hotelero','10/30/1002','maestria','adsito')
#acta=acta(1,'Esta es la acta del curso No1','9/1/1002')
#acta.pagos(curso1)

def menuclases():
    print('\nBienvenido al menu del Sena')
    print('1-Registrar profesor')
    print('2-Registrar alumno')
    print('3-Agregar materias')
    print('0-Salir')
    menu=int(input(''))
print('Bienvenido al menu del Sena')
print('1-Registrar profesor')
print('2-Registrar alumno')
print('3-Agregar materias')
print('0-Salir')
menu=int(input(''))
while True:
    match menu:
        case 1:
            id=int(input('¿Cual es el id del instructor?\n-'))
            nombre1=input('¿Cual es el nombre del instructor?\n-')
            edad=int(input('¿Cual es la edad del instrcutor?\n-'))
            contacto=int(input('¿Cual es el numero de contacto del instructor?\n-'))
            nombreuse=input('¿Cual es el nombre de usuario del instructor?\n-')
            contraseña=input('¿Cual es la contraseña del instructor?\n-')
            credenciales=input('¿Cuales son las credenciales del instructor?\n-')
            instructor1=instructor(id,nombre1,edad,contacto,nombreuse,contraseña,credenciales)
            print('\nDatos del instructor: ',instructor1.gid(),instructor1.gnombre(),instructor1.gedad(),instructor1.gcontacto(),instructor1.gnombreuse(),instructor1.gcontraseña(),instructor1.gcredenciales())
            pregunta=input('\n¿Quieres agregar materias al?\n-')
            if pregunta == 'Si' or pregunta=='si':
                continue
            else:
                menuclases()
        case 2:
            id=int(input('¿Cual es el id del aprendiz?\n-'))
            nombre1=input('¿Cual es el nombre del aprendiz?\n-')
            edad=int(input('¿Cual es la edad del aprendiz?\n-'))
            contacto=int(input('¿Cual es el numero de contacto del aprendiz?\n-'))
            nombreuse=input('¿Cual es el nombre de usuario del aprendiz?\n-')
            contraseña=input('¿Cual es la contraseña del aprendiz?\n-')
            curso1=input('¿Cuales es el curso del aprendiz?\n-')
            estudiante1=estudiante(id,nombre1,edad,contacto,nombreuse,contraseña,curso1)
            print('\nDatos del aprendiz: ',estudiante1.gid(),estudiante1.gnombre(),estudiante1.gedad(),estudiante1.gcontacto(),estudiante1.gnombreuse(),estudiante1.gcontraseña(),estudiante1.gcurso())
            pregunta=input('\n¿Quieres agregar otro aprendiz?\n-')
            if pregunta == 'Si' or pregunta=='si':
                continue
            else:
               menuclases()
        case 3:
            print('Como instructor puedes agregar nuevas materias')      
            id=int(input('¿Cual es el id de la materia?\n-'))
            nmateria=input('¿Cual es el nombre de la materia\n-')
            descripcion=input('¿Cual es la descripcion de la materia?\n-')
            nombre=instructor1.gnombre()
            horario=input('¿Cuantas horas a la semana es esta materia?\n-')
            ma=materia(id,nmateria,descripcion,nombre,horario)
            instructor1.agregarmateria(ma)
            print(ma.getidm(),ma.getNombrem(),ma.getdescripcionm(),ma.getinstructorm(),ma.gethorariom())
            if pregunta == 'Si' or pregunta=='si':
                    continue
            else:
                menuclases()
            
        case 0:
            print('Gracias por usar la pagina del sena')
            quit()
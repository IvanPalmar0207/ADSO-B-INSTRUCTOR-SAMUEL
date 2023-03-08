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
        self.requisitos=requistos
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
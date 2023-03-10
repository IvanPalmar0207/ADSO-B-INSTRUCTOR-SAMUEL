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
    def sid(self,id):
        self.__id=id
    def snombre(self,nombre):
        self.nombre=nombre
    def sdescripcion(self,descripcion):
        self.descripcion=descripcion
    def sinstructor(self,instructor):
        self.instructor=instructor
    def shorario(self,horario):
        self.horario=horario
class instructor(registrar):
    c=0
    def __init__(self,id,nombre,edad,contacto,nombreuse,contraseña,credenciales):
        super().__init__(id,nombre,edad,contacto,nombreuse,contraseña)
        self.__credenciales=credenciales
        self.materia=[]
        self.geteliminar=[]
        self.consulta=[]
        self.acta=[]
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

class acta:
    c=0
    def __init__(self, id, detalles, fechacreacion):
        self.id = id
        self.detalles = detalles
        self.fechacreacion = fechacreacion
        self.__class__.c+=1
    def getid(self):
        return self.id
    def getdetalles(self):
        return self.detalles
    def getfechacreacion(self):
        return self.fechacreacion
    def pagos(self,cursito):
        if cursito.getNivelacademicoc()=='Tecnico' or cursito.getNivelacademicoc() == 'tecnico':
            print('El curso que cursaras es de nivel tecnico y en nuestra institucion es completamento gratuito.')
        elif cursito.getNivelacademicoc()=='Tecnologo' or cursito.getNivelacademicoc() == 'tecnologo':
            print('El curso que cursaras es de nivel tecnologo y en nuestra institucion es completamente gratuito.')
        elif cursito.getNivelacademicoc()=='Profesional' or cursito.getNivelacademicoc() == 'profesional':
            print('El curso tiene un precio de 5millones el semestre, contando que son 10 semestres, el precio final seria de 50millones.')
        elif cursito.getNivelacademicoc()=='Mestria' or cursito.getNivelacademicoc() == 'mestria':
            print('La maestria en nuestra institucion tiene unvalor de 40 millones de pesos.')

print('Bienvenido al menu del Sena'.title())
print('1-Agregar materia/as a un curso (Instructor)')
print('2-Realizar inscripción a un curso (Aprendiz)')
print('3-Consultar acta (Instructor)')
print('4-Eliminar materia (Instructor)')
print('5-Constultar acta (Aprendiz)')
print('6-Precio del curso a traves del acta')
print('7-Actualizar materia (Instructor)')
print('8-Actualizar inscripción (Aprendiz)')
print('9-Registrar (Instructor)')
print('10-Registrar (Aprendiz)')
print('0-Salir')
menu=int(input('\n¿Que accion deseas realizar?- '))
while True:
    match menu:
        case 1:
            print('\nDetalles del curso')
            id=int(input('¿Cual es el id del curso?\n-'))
            descripcion=input('¿Cual es la descripcion del curso?\n-')
            fechainicio=input('¿Cual es la fecha en la que inicia el curso?\n-')
            nivelacademico=input('¿Cual es el grado academico del curso?\n-')
            nombre=input('¿Cual es el nombre del curso?\n-')
            curso=curso(id, descripcion, fechainicio, nivelacademico, nombre)
            print('\nDatos del instructor del curso')
            id1=int(input('¿Cual es el id del instructor?\n-'))
            nombre1=input('¿Cual es el nombre del instructor?\n-')
            edad1=int(input('¿Cual es la edad del instructor?\n-'))
            contacto1=int(input('¿Cual es el numero de contacto del instructor?\n-'))
            nombreuse1=input('¿Cual es el nombre de usuario del instructor?\n-')
            contraseña1=input('¿Cual es la contraseña del instructor?\n-')
            credenciales1=input('¿Cuales son las credenciales del instructor?\n-')
            inst=instructor(id1, nombre1, edad1, contacto1, nombreuse1, contraseña1, credenciales1)
            print('\nDatos de la materia o asignatura')
            idm=int(input('¿Cual es el id de la materia?\n-'))
            nombrem=input('¿Cual es el nombre de la materia?\n-')
            descripcionm=input('¿Cual es la descripcion de la materia?\n-')
            horariom=input('¿Cual es el horario de la materia?\n-')
            curso.agregarmateria(idm, nombrem, descripcionm, inst.gnombre(),horariom)
            print('Datos del curso:',curso.getidc(),curso.getDescripcionc(),curso.getFechainicioc(),curso.getNivelacademicoc(),curso.getNombrec())
            print('Datos de instructor:',inst.gid(),inst.gnombre(),inst.gedad(),inst.gcontacto(),inst.gnombreuse(),inst.gcontraseña(),inst.gcredenciales())
            for i in curso.getmateria():
                print('Datos de la asignatura:',i.getidm(),i.getNombrem(),i.getdescripcionm(),inst.gnombre(),i.gethorariom())
            pregunta=input('\n¿Deseas agregar otra materia? -')
            if pregunta=='Si' or pregunta=='si':
                id2=int(input('¿Cual es el id de la materia?\n-'))
                nombre2=input('¿Cual es el nombre de la materia?\n-')
                descripcion2=input('¿Cual es la descripcion de la materia?\n-')
                horario2=input('¿Cual es el horario de la materia?\n-')
                ma=materia(id2, nombre2, descripcion2, inst.gnombre(), horario2)
                inst.agregarmateria(ma)
                for i in curso.getmateria():
                    print('\nDatos de la primera asignatura:',i.getidm(),i.getNombrem(),i.getdescripcionm(),inst.gnombre(),i.gethorariom())
                for j in inst.gmateria():
                    print('Datos de la segunda asignatura:',i.getidm(),i.getNombrem(),i.getdescripcionm(),inst.gnombre(),i.gethorariom())
                print('Has agregado materias al curso satisfactoriamente')
                break
            else:
                print('Has decidido no agregar mas materias')
        case 2:
            print('\nIngresa los detalles del curso al cual deseas realizar tu inscripcion')
            id=int(input('¿Cual es el id del curso?\n-'))
            descripcion=input('¿Cual es la descripcion del curso?\n-')
            fechainicio=input('¿Cual es la fecha en la que inicia el curso?\n-')
            nivelacademico=input('¿Cual es el grado academico del curso?\n-')
            nombre=input('¿Cual es el nombre del curso?\n-')
            curso1=curso(id, descripcion, fechainicio, nivelacademico, nombre)            
            print('\nIngresa tus datos para realizar el proceso de inscripcion')
            id1=int(input('¿Cual es el id del aprendiz?\n-'))
            nombre1=input('¿Cual es el nombre del aprendiz?\n-')
            edad1=int(input('¿Cual es la edad del aprendiz?\n-'))
            contacto1=int(input('¿Cual es el numero de contacto del aprendiz?\n-')) 
            nombreuse1=input('¿Cual es el nombre de usuario del aprendiz?\n-')
            contraseña1=input('¿Cual es la contraseña del aprendiz?\n-')
            aprendiz=estudiante(id1, nombre1, edad1, contacto1, nombreuse1, contraseña1, curso1)
            print('\nDetalles de la inscripcion')
            id2=int(input('¿Cual es el id de la inscripcion?\n-'))
            detalles2=input('¿Cuales son los detalles de la inscripcion?\n-')
            requisitos2=input('¿Cuales son los requisitos de la inscripcion?\n-')
            finicio2=input('¿Cual es la fecha de inicio del programa por el cual ser realizo la inscripcion?\n-')
            ffin2=input('¿Cual es la fecha de finalizacion del programa?\n-')
            curso1.cinscripcion(id2,detalles2,requisitos2,finicio2,ffin2)
            print('Datos del curso:',curso1.getidc(),curso1.getDescripcionc(),curso1.getFechainicioc(),curso1.getNivelacademicoc(),curso1.getNombrec())
            print('Datos del aprendiz',aprendiz.gid(),aprendiz.gnombre(),aprendiz.gedad(),aprendiz.gcontacto(),aprendiz.gnombreuse(),aprendiz.gcontraseña(),curso1.getNombrec())
            for i in curso1.ginscripcion():
                print('Datos de la inscripcion: ',i.gid(),i.gdetalles(),i.grequisitos(),i.gfinicio(),i.gffinal())
            print('Haz realizado tu inscripcion satisfactoriamente ')
            break
        case 3:
            print('\nIngresa los datos del instructor para procesar el acta')
            id1=int(input('¿Cual es el id del instructor?\n-')) 
            nombre1=input('¿Cual es el nombre del instructor?\n-')
            edad1=int(input('¿Cual es la edad del instructor?\n-'))
            contacto1=int(input('¿Cual es el numero de contacto del instructor?\n-'))
            nombreuse1=input('¿Cual es el nombre de usuario del instructor?\n-')
            contraseña1=input('¿Cual es la contraseña del instructor?\n-')
            credenciales1=input('¿Cuales son las credenciales del instructor?\n-')
            instruc=instructor(id1, nombre1, edad1, contacto1, nombreuse1, contraseña1, credenciales1)
            print('\nIngresa los datos generales de el acta')
            ida=int(input('¿Cual es el id de el acta?\n-'))
            detallesa=input('¿Cuales son los detalles princiapales de el acta?\n-')
            fechac=input('¿Cual fue la fecha de creacion de el acta?\n-')
            acta1=acta(ida, detallesa, fechac)
            instruc.newacta(acta1)
            for i in instruc.getacta():
                print('Tu acta ya fue procesada y contiene los siguientes datos: ',i.getid(),i.getdetalles(),i.getfechacreacion())
            break
        case 4:
            print('\nIngresa los datos de la materia o asignatura que deseas eliminar como instructor')
            idm1=int(input('¿Cual es el id de la materia?\n-'))
            nombrem1=input('¿Cual es el nombre de la materia?\n-')
            descripcionm1=input('¿Cual es la descripcion de la materia?\n-')
            instructorm1=input('¿Cual es tu nombre?\n-')
            horariom1=input('¿Cual es el horario de la materia?\n-')
            mat=materia(idm1, nombrem1, descripcionm1, instructorm1, horariom1)
            del mat
            print('Tu materia ha sido eliminada satisfactoriamente\n')
            break
        case 5:
            print('\nIngresa los datos del aprendiz para poder crear el acta')
            id1=int(input('¿Cual es el id del aprendiz?\n-')) 
            nombre1=input('¿Cual es el nombre del aprendiz?\n-')
            edad1=int(input('¿Cual es la edad del aprendiz?\n-'))
            contacto1=int(input('¿Cual es el numero de contacto del aprendiz?\n-'))
            nombreuse1=input('¿Cual es el nombre de usuario del aprendiz?\n-')
            contraseña1=input('¿Cual es la contraseña del aprendiz?\n-')
            curso1=input('¿Cuales es el curso que identifica a el aprendiz?\n-')
            aprendiz=estudiante(id1, nombre1, edad1, contacto1, nombreuse1, contraseña1, curso1)
            print('\nIngresa los datos generales de tu acta para poder crearla')
            ida1=int(input('¿Cual es el id de el acta?\n-'))
            detallesa1=input('¿Cuales son los detalles princiapales de el acta?\n-')
            fechac1=input('¿Cual fue la fecha de creacion de el acta?\n-')
            acta11=acta(ida1, detallesa1, fechac1)
            aprendiz.acta(acta11)
            for i in aprendiz.gacta():
                print('Tu acta ya fue procesada y contiene los siguientes datos: ',i.getid(),i.getdetalles(),i.getfechacreacion())
            break
        case 6:
            print('\nIngresa los detalles del curso al que le deseas hallar precio')
            id2=int(input('¿Cual es el id del curso?\n-'))
            descripcion2=input('¿Cual es la descripcion del curso?\n-')
            fechainicio2=input('¿Cual es la fecha en la que inicia el curso?\n-')
            nivelacademico2=input('¿Cual es el grado academico del curso?\n-')
            nombre2=input('¿Cual es el nombre del curso?\n-')
            curso2=curso(id2, descripcion2, fechainicio2, nivelacademico2, nombre2)
            print('\nIngresa los detalles del acta para hallar el precio del curso')
            ida12=int(input('¿Cual es el id de el acta?\n-'))
            detallesa12=input('¿Cuales son los detalles princiapales de el acta?\n-')
            fechac12=input('¿Cual fue la fecha de creacion de el acta?\n-')
            acta112=acta(ida12,detallesa12,fechac12)
            acta112.pagos(curso2)
            break
        case 7:
            print('\nIngresa los detalles de la materia que deseas actualizar')
            idm12=int(input('¿Cual es el id de la materia?\n-'))
            nombrem12=input('¿Cual es el nombre de la materia?\n-')
            descripcionm12=input('¿Cual es la descripcion de la materia?\n-')
            instructornm12=input('¿Cual es el instructor de la materia?\n-')
            horariom12=input('¿Cual es el horario de la materia?\n-')
            materia1=materia(idm12,nombrem12,descripcionm12,instructornm12,horariom12)
            print('\nMomento de Actualizar la Materia')
            p1=input('¿Quieres actualizar la Materia?\n-')
            if p1=='Si' or p1=='si':
                pregunta=input('¿Que parte deseas cambiar o actualizar de la materia?\n-')
                if pregunta=='Id' or pregunta=='id':
                    cambioid=input('¿Cual es el id nuevo para la materia?\n-')
                    materia1.sid(cambioid)
                    print('La materia con el id nuevo es:',materia1.getidm(),materia1.getNombrem(),materia1.getdescripcionm(),materia1.getinstructorm(),materia1.gethorariom())
                    break
                elif pregunta=='Nombre' or pregunta=='nombre':
                    cambionombre=input('¿Cual es el nombre nuevo para la materia?\n-')
                    materia1.snombre(cambionombre)
                    print('La materia con un nombre nuevo es:',materia1.getidm(),materia1.getNombrem(),materia1.getdescripcionm(),materia1.getinstructorm(),materia1.gethorariom())
                    break
                elif pregunta=='Descripcion' or pregunta=='descripcion':
                    cambiodescripcion=input('¿Cual es la nueva descripcion para la materia?\n-')
                    materia1.sdescripcion(cambiodescripcion)
                    print('La materia con una descripcion nueva es:',materia1.getidm(),materia1.getNombrem(),materia1.getdescripcionm(),materia1.getinstructorm(),materia1.gethorariom())
                    break
                elif pregunta=='Instructor' or pregunta=='instructor':
                    cambioinstructor=input('¿Cual sera el nuevo instructor para la materia?\n-')
                    materia1.sinstructor(cambioinstructor)
                    print('La materia con un nuevo instructor es:',materia1.getidm(),materia1.getNombrem(),materia1.getdescripcionm(),materia1.getinstructorm(),materia1.gethorariom())
                    break
                elif pregunta=='Horario' or pregunta=='horario':
                    camiohorario=input('¿Cual es el nuevo horario para la materia?\n-')
                    materia1.shorario(camiohorario)
                    print('La materia con el horario nuevo es:',materia1.getidm(),materia1.getNombrem(),materia1.getdescripcionm(),materia1.getinstructorm(),materia1.gethorariom())
                    break
            else:
                print('Has decidido continuar y dejar los datos anteriores')
        case 8:
            print('\nIngresa los datos del estudiante, para poder realizar la actualizacion de datos')
            id12=int(input('¿Cual es el id del aprendiz?\n-')) 
            nombre12=input('¿Cual es el nombre del aprendiz?\n-')
            edad12=int(input('¿Cual es la edad del aprendiz?\n-'))
            contacto12=int(input('¿Cual es el numero de contacto del aprendiz?\n-'))
            nombreuse12=input('¿Cual es el nombre de usuario del aprendiz?\n-')
            contraseña12=input('¿Cual es la contraseña del aprendiz?\n-')
            curso12=input('¿Cuales es el curso que identifica a el aprendiz?\n-')
            aprendiz12=estudiante(id12, nombre12, edad12, contacto12, nombreuse12, contraseña12, curso12)
            print('\nAhora ingresar los datos de tu inscripcion para poder hacer los cambios')
            id112=int(input('¿Cual es el id de la inscripcion?\n-'))
            detalles112=input('¿Cuals son los detalles de la inscripcion?\n-')
            requisitos112=input('¿Cuales son los requisitos de la inscripcion?\n-')
            finicio112=input('¿Cual es la fecha de inicio del curso a la cual realizo la inscripcion?\n-')
            ffin112=input('¿Cual es la fecha final del curso al que realizo la inscripcion?\n-')
            ins112=inscripcion(id112, detalles112, requisitos112, finicio112, ffin112)
            pr=input('\n¿Que deseas actualizar de la inscripcion?\n-')
            if pr=='Id' or pr=='id':
                cambio1=int(input('¿Cual es el nuevo id?\n-'))
                ins112.sid(cambio1)
                print('Los datos actualizados son:',ins112.gid(),ins112.gdetalles(),ins112.grequisitos(),ins112.gfinicio(),ins112.gffinal())
                break
            elif pr=='Detalles' or pr=='detalles':
                cambio2=input('¿Cuales son los nuevos detalles para tu matricula?\n-')
                ins112.sdetalles(cambio2)
                print('Los datos actualizados son:',ins112.gid(),ins112.gdetalles(),ins112.grequisitos(),ins112.gfinicio(),ins112.gffinal())
                break
            elif pr=='Requisitos' or pr=='requisitos':
                cambio3=input('¿Cuales son los nuevos requisitos de la iscripcion?\n-')
                ins112.srequisitos(cambio3)
                print('Los datos actualizados son:',ins112.gid(),ins112.gdetalles(),ins112.grequisitos(),ins112.gfinicio(),ins112.gffinal())
                break
            elif pr=='Fecha de inicio' or pr=='fecha de inicio' or pr=='Fecha inicio' or pr=='fecha inicio':
                cambio4=input('¿Cual es la nueva fecha del inicio del curso al cual se realizo la inscripcion?\n-')
                ins112.sfinicio(cambio4)
                print('Los datos actualizados son:',ins112.gid(),ins112.gdetalles(),ins112.grequisitos(),ins112.gfinicio(),ins112.gffinal())
                break
            elif pr=='Fecha de fin' or pr=='fecha de fin' or pr=='Fecha fin' or pr=='fecha fin':
                cambio5=input('¿Cual sera la nuevo fecha de finalizacion del curso al que se hizo la inscripcion?\n-')
                ins112.sffin(cambio5)
                print('Los datos actualizados son:',ins112.gid(),ins112.gdetalles(),ins112.grequisitos(),ins112.gfinicio(),ins112.gffinal())
                break    
        case 9:
            print('\nIngresa tus datos principales')
            id11=int(input('¿Cual es el id del instructor?\n-'))
            nombre11=input('¿Cual es el nombre del instructor?\n-')
            edad11=int(input('¿Cual es la edad del instructor?\n-'))
            contacto11=int(input('¿Cual es el numero de contacto del instructor?\n-'))
            nombreuse11=input('¿Cual es el nombre de usuario del instructor?\n-')
            contraseña11=input('¿Cual es la contraseña del instructor?\n-')
            credenciales11=input('¿Cuales son las credenciales del instructor?\n-')
            inst1=instructor(id11, nombre11, edad11, contacto11, nombreuse11, contraseña11, credenciales11)
            print('Datos ingresados:',inst1.gid(),inst1.gnombre(),inst1.gedad(),inst1.gcontacto(),inst1.gnombreuse(),inst1.gcontraseña(),inst1.gcredenciales())
            print('Has sido satisfactoriamente registrado en un rol de instructor')
            break
        case 10:
            print('\n-Ingresa tus datos principales')
            id12=int(input('¿Cual es el id del aprendiz?\n-'))
            nombre12=input('¿Cual es el nombre del aprendiz?\n-')
            edad12=int(input('¿Cual es la edad del aprendiz?\n-'))
            contacto12=int(input('¿Cual es el numero de contacto del aprendiz?\n-')) 
            nombreuse12=input('¿Cual es el nombre de usuario del aprendiz?\n-')
            contraseña12=input('¿Cual es la contraseña del aprendiz?\n-')
            curso12=input('¿Con cual curso se te puede identificar?\n-')
            aprendiz12=estudiante(id12, nombre12, edad12, contacto12, nombreuse12, contraseña12, curso12)
            print('Datos ingresados',aprendiz12.gid(),aprendiz12.gnombre(),aprendiz12.gedad(),aprendiz12.gcontacto(),aprendiz12.gnombreuse(),aprendiz12.gcontraseña(),aprendiz12.gcurso())
            print('El proceso de registro ha sido satisfactoriamente completado (Aprendiz)')
            break
        case 0:
                print('Gracias por usar la pagina del SENA, espero haya sido de mucho provecho')
                break
class Registrar:
    def __init__(self,Id,Nombre,Edad,Contacto,Nombre_Usuario,Contraseña):
        self.id=Id
        self.nombre=Nombre
        self.edad=Edad
        self.contacto=Contacto
        self.__nombreusuario=Nombre_Usuario
        self.__contraseña=Contraseña
    
    def setId(self,id):
        self.id=id
    
    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setEdad(self,edad):
        self.edad=edad
    
    def setContacto(self,contacto):
        self.contacto=contacto
        
    def setNombreUsuario(self,nombreusuario):
        self.__nombreusuario=nombreusuario
        
    def setContraseña(self,contraseña):
        self.__contraseña=contraseña
        
class materias:
    def __init__(self,id,nombre,descripcion,instructor,horario):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.instructor=instructor
        self.horario=horario
        self.nombre1=[]
    def nombre12(self,n):
        self.nombre1.append(n)
    def getNombre(self,nombre):
        if nombre == self.nombre:
            print('El id del curso es',self.id,'y el nombre del curso es', nombre)
        for i in self.nombre1 :
            if i in nombre:
                print('El id del curso es',self.id,'y el nombre del curso es', nombre)
            else:
                print('El nombre no coincide con ninguna materia del curso')

ma2=materias(1,'ciencia','descripcion','intrcutor','horario')
ma2.getNombre('cienca')
    
class curso:
    def __init__(self,id,nombre,descripcion,fechainicio,nivelacademico):
        self.id=id
        self.descripcion=descripcion
        self.fechainicio=fechainicio
        self.nivelacademico=nivelacademico
        self.nombre=nombre
        self.idnombre=id + nombre
        self.tecnico=[]
        self.tecnologo=[]
        self.profesional=[]
        self.maestria=[]
    def getId(self):
        return self.id
    def getDescripcion(self):
        return self.descripcion
    def getFechaInicio(self):
        return self.fechainicio
    def getNivel(self):
        return self.nivelacademico
    def getNombre(self):
        return self.nombre
    def agrupar(self):
        if self.nivelacademico == 'Tecnico':
            self.tecnico.append(self.idnombre)
            return self.tecnico
        elif self.nivelacademico == 'Tecnologo':
            self.tecnologo.append(self.idnombre)
            
class acta:
    def __init__(self,id,detalles,fechacreacion,precio):
        self.id=id
        self.detalles=detalles
        self.fechacreacion=fechacreacion
        self.precio=precio
    def getId(self):
        return self.id
    def getDetalles(self):
        return self.detalles
    def getFechaCreacion(self):
        return self.fechacreacion
    def getPrecio(self):
        return self.precio
   # def PrecesoPago(self,metodopago):
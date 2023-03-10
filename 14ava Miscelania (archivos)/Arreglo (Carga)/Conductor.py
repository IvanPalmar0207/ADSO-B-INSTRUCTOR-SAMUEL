class Conductor: #Se hace uso de la palabra reservada class que sirve
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
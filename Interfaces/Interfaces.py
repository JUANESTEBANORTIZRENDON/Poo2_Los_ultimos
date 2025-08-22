from abc import ABC,abstractmethod #el abstrap,metod le indica a todas las clases que si usa la interfaz debe usar todas sus propiedad

class auto:
    def _init_(self, marca, matricula, dueño):
        self.marca  = marca
        self.__matricula  = matricula
        self.__dueño = dueño

    def get_matricula(self):
        # getter para poder verlo desde afuera
        return self.__matricula
    
    def set_matricula(self, nueva_matricula):
        if len(nueva_matricula) == 6:
            self.__matricula = nueva_matricula
        else:
            print("No cumple con los requisitos de la nueva matricula")

    def __get_dueño(self):
        return self.__dueño

    def get_informacion(self):
        print(f"El auto con matricula {self.get_matricula()} y marca {self.marca} es propiedad de {self.__get_dueño()}")

mi_carrito = auto("Mercho", "123XYZ", "JCDD")
print(mi_carrito.get_matricula())

# mi_carrito.set_matricula("ZYX321")

mi_carrito.get_informacion()



# mi_carrito.marca = "Lexus"
# print(mi_carrito.marca)

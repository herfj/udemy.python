#OBJETO

class User:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido=apellido
    def saludo(self):
        print("Hola mi nombre es",self.nombre,self.apellido)
u1 = User(apellido="jose", nombre="baute")
# u1.saludo()

#HERENCIA

class Admin(User):
    def superSaludo(self):
        print("soy el admin paaa : ", self.nombre)


admin = Admin("asdf", "qwerty")
# admin.saludo()
# admin.superSaludo()

#EJEMPLOS 

class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

class Gato(Animal):
    def __init__(self, nombre, sonido):
        Animal.__init__(self,nombre,sonido)
    tipo="GATO"
    def saludo(self):
        print("hola soy un",self.tipo," con nombre", self.nombre, "y sonido ", self.sonido)

        
class Perro(Animal):
    def __init__(self, nombre, sonido):
        super().__init__(nombre,sonido)
        self.tipo="PERRO"
    def saludo(self):
        print("hola soy un ",self.tipo," con nombre", self.nombre, "y sonido ", self.sonido)

gato = Gato("firulais", "miiiiauuuuu cuidado que te araño papi")
perro = Perro("zues", "perro macho alfa peludito y kariniosito")
gato.saludo()
perro.saludo()


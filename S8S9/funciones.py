# def miFuncion():
#     print("que anda");

# miFuncion();

# def func(a1, a2):
#     print(a1, a2)
#     return "pepeGaurdiola"

# print(func("haofsd", 3))


# def lista(*nomBre):
#     print(nomBre)

# lista("afds", 4, "sadf")

# def funSinOrden(apellido, nombre):
#     print(nombre, apellido)

# funSinOrden(nombre="hernan", apellido="fabrica")

# def funcionesKwargs(**k):
#     print(k["nombre"], k["apellido"])

# funcionesKwargs(nombre="hernan", apellido="fabrica")

# SETEA POR DEFAULT EL VALOR DEL ARGUMENTO SI ES QUE NO LO RECIBE
# def miFuncion(arg="tomas"):
#     print(arg)

# miFuncion("hola")
# miFuncion()

def listaFuncion(lista):
    for el in lista:
        print(el)

listaFuncion(["tomas", "hernan"])
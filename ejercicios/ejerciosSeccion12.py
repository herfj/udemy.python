# Ejercicio 1

n1 = 5
n2 = 6
res =0
for i in range(n1):
		res+=n2

print(res)

# Ejercicio 2

n = input('ingresa tu name: ')
a = input('ingresa tu ape: ')

alRevez=n+' '+a

print(alRevez[::-1])

# Ejercicio 3

lista = [2,234,23,3,2,45,2,-12,0]
menor = 'init'
for i in lista:
	if menor == 'init':
		menor = i
	else:
		if menor>i:
			menor=i
print(menor)

# Ejercicio 4

def calculo(radio):
	return 4/3 * 3.14 * radio**3

print(calculo(6))

# Ejercicio 5

def esMayor(edad):
	return edad >= 18

print(esMayor(21))
print(esMayor(18))
print(esMayor(1))

# Ejercicio 6

# Ejercicio 7

palabra = 'ChAnchitoFeliz'
vocales = 0
for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
print(vocales)

# Ejercicio 8

lista = []
print('Ingrese números y para salir escriba "basta"')
while True:
    valor = input('Ingrese valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato inválido')
            exit()

resultado = 0
for x in lista:
    resultado += x

print(resultado)

# Ejercicio 9

def agregaNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombreAArchivo('Chanchito', 'Feliz')
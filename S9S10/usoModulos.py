from modulos import saludo
from camelcase import CamelCase

saludo()
c = CamelCase()
s = "esto es una es sentencia necesita camel caseeee"
s = c.hump(s)
print(s);

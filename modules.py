# python modules (desde el python)

import datetime #* para importar un modulo de python con su nombre respectivo (se pueden buscar sus modulos en la biblioteca de python)

# print(datetime.date.today())

# print(datetime.timedelta(minutes=70))

from datetime import timedelta, date
print(timedelta(minutes=80))
print(date.today())

# own modules (propias)

import fmath
fmath.add(1, 2)
fmath.substract(1, 2)

from fmath import add, substract
substract(1, 2)
add(1, 2)

# thirdy party modules (descargar de inter)
    #* el comando pip en la consola sirve para instalar modulos de internet (pip --version) y poner el comando que mencionan en el navegador en la consola

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "Hello world")

# Coleccion desordenada y sin indice
colors ={'red', 'green', 'blue'}

print(type(colors))
print('red' in colors)
colors.add('violet') #*lo agrega al inicio debido a que no tiene indice
print(colors)
colors.remove('red')
print(colors)

colors.clear() #*para limpiar el ser
del colors #* para eliminar el set
print(colors)

# Sirve para cuando tienes datos que no tienen indice
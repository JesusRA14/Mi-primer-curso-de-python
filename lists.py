demo_list = [1, 'Hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))
print(type(numbers_list))
# sale error porque la .list solo soporta un argumento
#* por lo tanto le colocare una tupla ()

# Listas a partir de un rango
r = list(range(1, 10))
print(r)
#* En este caso el rango solo llega hasta un numero antes del numero final
print(len(demo_list))
# no olvidar que el dir sirve para ver que se puede hacer con algo, en este caso  las listas
print(colors[1]) #* para que me devuelva el string en la posicion mencionada
print('orange' in colors)

print(colors)
colors[1]='yellow'
print(colors)

# print(dir(colors))

#colors.append('violet') #*agregar elemmento
#colors.append(('violet', 'yellow')) #*//append solo acepta un elemento por lo que tendremos que convertirlo a tupla

#colors.extend(('violet', 'yellow')) #*permite agregar los elementos, que estan como un solo elemento, pero sin los parentesis o los corchetes cual sea el caso

colors.insert(1, 'pink') #* para insertar un elemento en una posicion determinada
colors.insert(len(colors), 'red')

print(colors)

#colors.pop() #* sirve para quitar el ultimo valor o un elemento basado en un indice

#colors.remove('red') #* para quitar un elemento en especifico

#colors.clear() #* dejar la lista vacia

#colors.sort() #*para ordenarlos alfabeticamente

#colors.sort(reverse=True) #* para ordenarlos de manera inversa

print(colors.index('red')) #* para obtener los indices de un elemento
print(colors.count('red')) #* contar el valor dado

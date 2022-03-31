myStr = "Hello World"

    # print(dir(myStr))
    # dir sirve para ver que se puede hacer con myStr

print(myStr.upper()) # poner en mayusculas el texto
print(myStr.lower()) # poner en minusculas el texto
print(myStr.swapcase()) # cambiar minusculas por mayusculas y viceversa
print(myStr.capitalize()) # mantiene la primera letra en mayuscula en caso no este asi
print(myStr.replace('Hello', 'Bye')) # Cambia del texto aquello que especificas por otra palabra
print(myStr.replace('Hello', 'Bye').upper()) # metodos encadenados
print(myStr.count(' ')) # contar duh

print(myStr.startswith('Hello')) # ¿el texto escrito empieza con la palabra ...? (true or false)
print(myStr.endswith('World')) #¿el texto termina con ...? (true or false)

print(myStr.split()) # por defecto separa las palabras a partir de un caracter en blanco o tambien decirle que separe el texto a partir de una ',' o un 'o' (los cuales van an el parentesis de .split())
print(myStr.find('o')) #devuelve la posicion del caracter proporcionado.

print(len(myStr)) # cuenta la longitud de los caracteres pero empieza a contar desde 0, 1, 2,...
print(myStr.index('e')) # da el indice del caracter (empezando desde 0)

print(myStr.isnumeric()) #¿es mystr numerico?
print(myStr.isalpha()) # ¿es mystr alfanumerico?

print(myStr[4]) # quiero el caracter de la posicion 4
print(myStr[-1]) # me devolvera el caracter inverso, osea el ultimo y asi.

print("My name is " + myStr) #concatenar
print(f"My name is {myStr}") # la f es para decirle que myStr entre llaves es una variable y no solo hay caracteres
print("My name is {0}".format(myStr)) # en el valor cero se pondra la variable myStr
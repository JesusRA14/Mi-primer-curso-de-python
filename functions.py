# Porcion de codigo que lo procesa internamente y que nos devuelve un resultado

# Para crear mis propias funciones
def hello(name="Person"):
    print("hello " + name)
    #* se puede colocar mas o una coma

hello("fazt")
hello()

def add(n1, n2):
    return n1 + n2

print(add(10, 30))

print(len("hello"))


#funciones lambda son funciones que no tienen nombre se pueden colocar en una sola linea sin necesidad de escribir return
add = lambda nu1, nu2: nu1 + nu2

print(add(10, 14))
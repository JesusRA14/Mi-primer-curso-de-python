
x = 40

if x < 30:
    print("x is less than 30")
    #* en este caso si es falso no se muestra el print a menos que le agreguemos un else.
else:
    print("x is greater than 30")

color = "blue"

if color == "red":
    print("The color is red")
elif color == "blue":
    print("the color is blue")
else:
    print("any color")


name = "John"
lastname = "Laseter"

if name == "John":
    if lastname == "Carter":
        print("You are John Carter")
    else:
        print("You are not John Carter")
else:
    print("You are not Jhon")


if x > 2 and x < 10:
    print("x is greater than 2 and less than or equal to ten")
if x > 2 or x <= 20:
    print("x is greater than two or less or equal to twenty")
if (not(x == y)):
    print("x is not equal y") 

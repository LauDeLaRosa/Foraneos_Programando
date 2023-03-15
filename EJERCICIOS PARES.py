a:float
a=float(input("ingrese el primer número real:"))
b:float
b=float(input("ingrese el segundo número real:"))
c:float
c=float(input("ingrese el tercer número real:"))
if a>b and a>c:
   print ("El número " + str(a) + " es mayor que " + str(b) + " y " + str(c))
elif b>a and b>c:
      print ("El número " + str(b) + " es mayor que " + str(a) + " y " + str(c))
elif c>a and c>b:
        print ("El número " + str(c) + " es mayor que " + str(b) + " y " + str(a))


a: float
a=float(input("Ingrese un número real:"))
b: float
b= float(input("Ingrese otro número real:"))
if a%b==0:
    print(str(a)+" es múltiplo de " + str(b))
else:
     print(str(a)+" no es múltiplo de " + str(b))


letra=(input("Ingrese una letra:"))
consonantes= ["b","B","C","c","d","D","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","ñ","Ñ","p","P","q","Q","r","R","s","S","t","T","v","V","w","W","x","X","y","Y","z","Z"]
vocales=["a","A","e","E","i","I","o","O","u","U"]
if letra in consonantes:
    print("La letra "+str(letra)+" es una consonante")
elif letra in vocales:
 print("La letra "+str(letra)+" es una vocal")


x : float
x = float(input("Ingresar frecuencia de onda en Hz: "))
if x<=300 and x>=0:
    print("frecuencias extremadamente bajas ")
elif x > 300 and x <= 3e+6:
    print("frecuencias bajas ")
elif x > 3e+6  and x <= 3e+8:
    print("Radiofrecuencias ")
elif x > 3e+8 and x <= 3e+10:
    print("Micro-ondas ")
elif x > 3e+10 and x <= 3e+11:
    print("Micro-ondas de muy alta frecuencia")
elif x > 3e+11 and x <= 4.3e+14:
    print("Ondas infrarrojas")
elif x > 4.3e+14 and x <= 7.7e+14:
    print("Luz visible")
elif x > 7.7e+14 and x <= 3e+16:
    print("Radiación ultravioleta")
elif x > 3e+16 and x <= 1e+19:
    print("Radiación ultravioleta")
elif x > 1e+19 and x <= 3e+22:
    print("Radiación ultravioleta")
elif x > 1e+22 and x <= 1e+25:
    print("Rayos cósmicos")
elif x > 1e+25:
    print("Rayos cósmicos muy energeticos ")
else:
    print("como tienes frecuencia negativa???")


Vluz : float
Vsonido : float
Vauto : float
Vbolt : float
Vluz : float = 2.998e+8
Vsonido : float = 343
Vauto : float = 141.11
Vbolt : float = 12.4
x : float
x=float(input("introduzca una dsitancia en metros: " ))
tiempo:float
a = x/Vluz
b = x/Vsonido
c = x/Vauto
d = x/Vbolt
print("tarda la luz " + str(a) + " segundos")
print("tarda el sonido " + str(b) + " segundos")
print("tarda el auto " + str(c) + " segundos")
print("tarda bolt " + str(d) + " segundos")
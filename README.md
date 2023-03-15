# Foráneos Programando - Taller #1
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/124603892/225188078-0b83ef61-9a17-458d-aa7e-608587b3886c.png">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/124603892/225188078-0b83ef61-9a17-458d-aa7e-608587b3886c.png">
   <img alt="Logo del equipo Foraneos.py" src="https://user-images.githubusercontent.com/124603892/225188078-0b83ef61-9a17-458d-aa7e-608587b3886c.png">
</picture>

## Quiz Python
A continuación evidencia del puntaje de más del 90% en el Python Beginner Quiz:

Quiz de Laura De La Rosa:
![image](https://user-images.githubusercontent.com/124603892/225186814-31bf9893-43d8-4243-97ea-5da22a8d3630.png)

Quiz de Brayan Ortiz:
![image](https://user-images.githubusercontent.com/124603892/225204130-4540f0a1-ddb8-4149-a4ea-277965826a03.png)

## Ejercicio #2
En este ejercicio se tenía que realizar un programa que leyera tres números reales y determinara cuál es el mayor. Para esto, se declararon tres variables (_a_, _b_, y _c_) las cuales son flotantes; de igual forma, se le permite al usuario ingresar cualquier número real esto tres veces por medio de _input_. Luego haciendo uso del condicional _if_ se determina que si _a_ es mayor a _b_ y a _c_ el programa debe de retornar un mensaje que diga que el número ingresado _a_ es mayor que los números ingresados _b_ y _c_. Sino, haciendo uso de _elif_ si _b_ es mayor que _a_ y _c_ el programa debe de retornar un mensaje que diga que el número ingresado _b_ es mayor que los números ingresados _a_ y _c_. Finalmente, también haciendo uso de _elif_ se definió que si _c_ es mayor que _a_ y _b_ el programa debe de retornar un mensaje que diga que el número ingresado _c_ es mayor que los números ingresados _b_ y _c_.
```pseudocode
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
 ```
[![](https://mermaid.ink/img/pako:eNp9kk1ugzAQRq8y8iqRwgVYtIpCfkgCSdTuoIvBuI3VYLcOqIpQLtZtL1Zjg0OQWjbAmzfzjcA1oTJnxCevJ_lFj6hKeA5SAc01HYWCUy7H9n0KnvcAs0T8fBdMScAXy2eGBwn6iuGphRAYOnd21hbmhi-S7M6GhcFLp9O2sjR8ldC-vvI0DGsEdoYCL1LBZ8Uge7zacuh5cOZN43ro0M5Za0fIxon-deycTTLMgotbcaOF7WjBxfgW343O7tuwGw2Rmx0PJZcPEDtrlwxH9TYA2DU79Ebb_H1N_8iPjdMobdPeJR2GTe67wsFJ216bzeqIEx22hdsdgEyI_skF8lwfvLohKSmPrGAp8fVjjuo9Jam4ag-rUj5dBCV-qSo2IdVHjiULOL4pLDrIcl5KFdmDbM7z9RcNvdIm?type=png)](https://mermaid.live/edit#pako:eNp9kk1ugzAQRq8y8iqRwgVYtIpCfkgCSdTuoIvBuI3VYLcOqIpQLtZtL1Zjg0OQWjbAmzfzjcA1oTJnxCevJ_lFj6hKeA5SAc01HYWCUy7H9n0KnvcAs0T8fBdMScAXy2eGBwn6iuGphRAYOnd21hbmhi-S7M6GhcFLp9O2sjR8ldC-vvI0DGsEdoYCL1LBZ8Uge7zacuh5cOZN43ro0M5Za0fIxon-deycTTLMgotbcaOF7WjBxfgW343O7tuwGw2Rmx0PJZcPEDtrlwxH9TYA2DU79Ebb_H1N_8iPjdMobdPeJR2GTe67wsFJ216bzeqIEx22hdsdgEyI_skF8lwfvLohKSmPrGAp8fVjjuo9Jam4ag-rUj5dBCV-qSo2IdVHjiULOL4pLDrIcl5KFdmDbM7z9RcNvdIm)

## Ejercicio #3
En este ejercicio había que crear un programa que leyera un número entero y determine si es par o impar. Dándole solución, se declaró una variable _n_ donde tendrá que ser un número entero. El usuario podrá ingresar cualquier número. Se usó el condicional _if_ para determinar que si el residuo entre el número entero y 2 era cero, el programa va a determinar que el número es par. Sino, usando _else_, es decir, si no pasa lo anterior, el número no es par.

```pseudocode
n:int
n=int(input("Ingrese un número entero:"))
if n%2==0:
    print("El número es par")
else:
    print("El número no es par")
```

## Ejercicio #4
Realizar un programa que lea dos números reales y determine si el primero es múltiplo del segundo. Se declararon dos variables (_a_, _b_) las cuales son flotantes para que el usuario pueda ingresar un número real en cada una de estas. Se hizo uso del condicional _if_ para determinar que si el residuo entre el primer número y el segundo es cero, el programa retornará que _a_ es múltiplo de _b_. Si no se cumple lo anterior (_else_), _a_ no es múltiplo de _b_.
```pseudocode
a: float
a=float(input("Ingrese un número real:"))
b: float
b= float(input("Ingrese otro número real:"))
if a%b==0:
    print(str(a)+" es múltiplo de " + str(b))
else:
     print(str(a)+" no es múltiplo de " + str(b))
```

## Ejercicio #5
Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número. Se crearon tres variables flotantes, donde el usuario tendrá que ingresar tres números reales. Luego, haciendo uso del condicional _if_ se dterminó que si la sumatoria del primer y segundo número es mayor que c, el programa arrojará una respuesta diciendo que el tercer número ingresado es menor que la suma de los dos primeros. Sino (_elif_), si la sumatoria de los dos primeros números es menor que el tercer número, la respuesta será que el tercer número es mayor que la suma de los primeros números. Sino, si la sumatoria de _a_ y _b_ es igual que c, el programa retornará que la sumatoria de los dos primeros números es igual al tercer número.
```pseudocode
a: float
a=float(input("Ingrese un número real:"))
b: float
b= float(input("Ingrese otro número real:"))
c:float
c=float(input("Ingrese un último número real:"))
if a+b>c:
    print(str(c)+ " es menor que la suma de " + str(a)+ " y " + str(b))
elif a+b<c:
   print(str(c)+ " es mayor que la suma de " + str(a)+ " y " + str(b))
elif a+b==c:
   print(str(c)+ " es igual que la suma de " + str(a)+ " y " + str(b))
```
[![](https://mermaid.ink/img/pako:eNqNkk1uwjAQha8y8gpUcoEsWiHCrwCB2l3SxWAbsJrY1HZUIcTFuu3F6sT5AzZEshS_eTPvkzUXQhXjJCT7VP3QI2oLH1EiofiGvbkUVKi-vw8hCF5hFMu_34xrBfjp9VGpRzGGmmNaiRCV6rhx76rCuNQn8e7GDZNSnjZ2WlWmpT6Ladc-C5w4v-DLDriBDM9Kw3fOgb5dvWEeBGBE0bqIlwgmzxAYh1QZYO6ctChCDFRp5nYMT8FyTV2hylu4QcveRMh-jesjpCoiVg0Il_cgsGpI1s-TNHMeSGBdoNQUnQyPsqlRxCHH9A5l06Bsn0Zp5zygdKb68GX7OADbrlw3tI1kQFxGhoK51bsUSkLskWc8IaH7Zai_EpLIq_NhbtX7WVISWp3zAclPDC2PBB40ZiTcY2qcypmwSq_8Lpcrff0HhhffdA?type=png)](https://mermaid.live/edit#pako:eNqNkk1uwjAQha8y8gpUcoEsWiHCrwCB2l3SxWAbsJrY1HZUIcTFuu3F6sT5AzZEshS_eTPvkzUXQhXjJCT7VP3QI2oLH1EiofiGvbkUVKi-vw8hCF5hFMu_34xrBfjp9VGpRzGGmmNaiRCV6rhx76rCuNQn8e7GDZNSnjZ2WlWmpT6Ladc-C5w4v-DLDriBDM9Kw3fOgb5dvWEeBGBE0bqIlwgmzxAYh1QZYO6ctChCDFRp5nYMT8FyTV2hylu4QcveRMh-jesjpCoiVg0Il_cgsGpI1s-TNHMeSGBdoNQUnQyPsqlRxCHH9A5l06Bsn0Zp5zygdKb68GX7OADbrlw3tI1kQFxGhoK51bsUSkLskWc8IaH7Zai_EpLIq_NhbtX7WVISWp3zAclPDC2PBB40ZiTcY2qcypmwSq_8Lpcrff0HhhffdA)

## Ejercicio #6
Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante. Para este programa se declaró una variable llamada _letra_ en la cual el usuario podrá ingresar cualquier letra. Luego se definieron dos variables llamadas _consonantes_ y _vocales_, donde en cada una de estas se hizo un listado de las consonantes y vocales. Haciendo uso del condicional _if_ se determinó que si la variable _letra_ está dentro del listado de _consonantes_, el programa dará una respuesta diciendo que la letra ingresada por el usuario es una consonante. Sino (_elif_), si _letra_ está dentro del listado _vocales_, el programa dará una respuesta de que la letra ingresada por el usuario es una vocal.
```pseudocode
letra=(input("Ingrese una letra:"))
consonantes= ["b","B","C","c","d","D","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","ñ","Ñ","p","P","q","Q","r","R","s","S","t","T","v","V","w","W","x","X","y","Y","z","Z"]
vocales=["a","A","e","E","i","I","o","O","u","U"]
if letra in consonantes:
    print("La letra "+str(letra)+" es una consonante")
elif letra in vocales:
 print("La letra "+str(letra)+" es una vocal")
```

## Ejercicio #7
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

 + El promedio
 + La mediana
 + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
 + Ordenar los números de forma ascendente
 + Ordenar los números de forma descendente
 + La potencia del mayor número elevado al menor número
 + La raíz cúbica del menor número

Se piden 5 variables, que posteriormente se ponen en un conjunto donde puedo pedir el número máximo y mínimo, también se puede ordenar de manera de ascendente y descendente, las otras operaciones se hacen a través de su fórmula numérica. Los resultados los asigno, y al final unicamente imprimo las variables asignadas previamente.
```pseudocode
n1 = float(input("Ingresar número 1: "))
n2 = float(input("Ingresar número 2: "))
n3 = float(input("Ingresar número 3: "))
n4 = float(input("Ingresar número 4: "))
n5 = float(input("Ingresar número 5: "))
numeros = [n1, n2, n3 , n4 , n5]
menorMayor = sorted(numeros)
mayorMenor = sorted(numeros, reverse=True)
promedio = (n1+n2+n3+n4+n5)/5
if len(numeros) % 2 == 0:
    mediana = (numeros[len(numeros)//2] + numeros[len(numeros)//2 - 1]) / 2
else:
    mediana = numeros[len(numeros)//2]
pmultiplicativo = (n1 * n2* n3 * n4 * n5)**0.2
peque = min(numeros)
grande = max(numeros)
raiz = peque**1/3
potencia = grande**peque
print("el promedio aritmetico es  " + str(promedio))
print("el promedio multiplicativo es " + str(pmultiplicativo))
print("la mediana es " + str(mediana))
print("de menor a mayor son " + str(menorMayor))
print("de menor a mayor son " + str(mayorMenor))
print("el mayor elevado al menor es " + str(potencia))
print("la raiz cubica del menor es " + str(raiz))
```

## Ejercicio #8
Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra. Asigno el nombre del área al que pertenece en _Hz_, y los intervalos a los que pertenece cierta frecuencia, desde frecuencia baja hasta rayos cósmicos, se pide un valor en _Hz_ y con el _if_ se establece a dónde va  a pertenecer con su respectivo _print_.
```pseudocode
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
```

## Ejercicio #9
Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado. Este proceso es más sencillo debido a que por el _lang_ establezco que para cada caso haya una respuesta, y en caso de ser una distinta, imprimir el mensaje _"país no identificado"_, entonces se pedirá un país en minúscula y se imprimirá el resultado.
```pseudocode
lang = input("ingrese país de america en minuscula ")
match lang:
  case "argentina":
    print("buenos aires")
  case "antigua y barbuda":
    print("saint john")
  case "bahamas":
    print("Nasáu")
  case "barbados":
    print(" Bridgetown")
  case "belice":
    print("Belmopán")
  case "bolivia":
    print(" Sucre")
  case "brasil":
    print("Brasilia")
  case "canada":
    print("Ottawa")
  case "chile":
    print("Santiago")
  case "colombia":
    print("bogotá")
  case "costa rica":
    print("San José")
  case "cuba":
    print("La Habana")
  case "dominica":
    print("Roseau")
  case "ecuador":
    print("Quito")
  case "el salvador":
    print("San Salvador")
  case "estados unidos":
    print("Washington D. C.")
  case "granada":
    print("Saint George")
  case "guatemala":
    print("Ciudad de Guatemala")
  case "guyana":
    print("Georgetown")
  case "haiti":
    print("Puerto Príncipe")
  case "honduras":
    print("Tegucigalpa")
  case "jamaica":
    print("Kingston")
  case "mexico":
    print("Ciudad de México")
  case "nicaragua":
    print("Managua")
  case "panama":
    print("Ciudad de Panamá")
  case "paraguay":
    print("Asunción")
  case "peru":
    print("lima")
  case "republica dominicana":
    print("Santo Domingo")
  case "san cristobal y nieves":
    print("Basseterre")
  case "san vicente y las granadinas":
    print("Kingstown")
  case "santa lucia":
    print("Castries")
  case "surinam":
    print("Paramaribo")
  case "trinidad y tobago":
    print("Puerto España")
  case "uruguay":
    print("montevideo")
  case "venezuela":
    print("caracas")
  case _:
    print("país no identificado")
```

## Ejercicio #10
Escriba un programa que dada una distancia calcule:

 + El tiempo que le tomaría a la luz recorrer la distancia.
 + El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
 + El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
 + El tiempo que le tomaría a Bolt recorrer la distancia.
 
 Se establecen las velocidades de dichas cosas que se evalúan, se pide una una distancia y se hace con cada velocidad el cálculo, posteriormente, se da el resultado con cada una de las velocidades.
 ```pseudocode
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
 ```

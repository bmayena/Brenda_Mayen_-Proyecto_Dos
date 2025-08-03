#PRIMERA PARTE DEL PROYECTO LONGITUD DE UNA FRASE: Crear un programa para identificar la longitud de una palabra ingresada. La palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las siguientes consideraciones:
#Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe imprimir un mensaje que indique que la palabra es correcta.
#Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: “Hacen falta letras. Solo tiene N letras” (siendo N el número de letras de la palabra).
#Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: “Sobran letras. Tiene N letras” (siendo N el número de letras de la palabra).

print("""PARTE I.
      
Hola, te doy la bienvenida. Este programa te ayudará a condicionar una palabra mediante la comprobación de la cantidad de caracteres alfabeticos.
Se considerará que la palabra es correcta cuando esta tenga de 4 a 8 letras. 
Para ello deberás de introducir la palabra que desees verificar y el programa te indicara si es correcta o te señalara alguna corrección. 

Vamos a ello.
       """)
user_word=(input("Introduce una palabra: "))
l_word_u = len(user_word)
if l_word_u >= 4 and l_word_u <= 8:
    pass
#hasta aqui funciona bien con distintas palabras 
#Se debe usar un while para seguir solicitando palabras hasta que se cumpla 
while l_word_u < 4:
    print (f"Hacen falta letras. Solo tiene {l_word_u} letras")
    user_word=(input("Introduce otra palabra: "))
    l_word_u = len(user_word)

while l_word_u > 8:
    print (f"Sobran letras. Tiene {l_word_u} letras")
    user_word=(input("Introduce otra palabra: "))
    l_word_u = len(user_word)
    
    while l_word_u < 4:
        print (f"Faltan letras. Tiene {l_word_u} letras")
        user_word=(input("Introduce otra palabra: "))
        l_word_u = len(user_word)
print("¡Bien! La palabra es correcta.")

#*********************************PARTE DOS DEL PROYECTO***************************
# Crear un programa que en base a 2 números de entrada, coordenadas, identifique en cuál de los 4 cuadrantes se encuentra el punto. El programa debe verificar que ninguna coordenada sea 0. Por ejemplo
print ("""
       ****Parte II****
        """)
print("""Hola, te doy la bienvenida. 
Este programa te indicará el cuadrante en el que se ubica un punto dentro de un plano cartesiano. El plano cartesiano se divide en cuatro cuadrantes, se enumera el cuadrante comenzando desde el superior derecho como punto de partida y la continuidad se asigna en sentido antihorario.
Un punto en el plano cartesiano tiene siempre 2 componentes, un valor en el eje "x" (horizontal) y otro en el eje "y" (vertical) que se indican con la siguiente estructura: (x,y). Sin embargo, para que un punto se sitúe en un cuadrante la condición es que "x" y "y" sean ambos números enteros pero exceptuando el cero.
      
       II   |   I
      (-,+) | (+,+)
      ------------
        III |   IV
      (-,-) |  (+,-) 

Por ejemplo, un punto con coordenadas (1,4) se sitúa en el cuadrante I.  

Con base en estas definiciones deberás de indicar un valor entero distinto de cero para (x,y) y el programa indicará el cuadrante en donde se ubica. 
      """)
x= int(input ("Ingresa el valor de x: "))
y= int(input ("Ingresa el valor de y: "))

# if x>0 and y>0:
#     print("El punto se ubica en el cuadrante: I")
# if x<0 and y>0:
#     print("El punto se ubica en el cuadrante: II")
# if x<0 and y<0:
#     print("El punto se ubica en el cuadrante: III")
# if x>0 and y<0:
#     print("El punto se ubica en el cuadrante: IV")

while x==0 and y == 0:
    print("Erroneo. No existe cuadrante, el punto se encuentra en el origen. Introduce dos enteros positivos o negativos: ")
    x= int(input ("Ingresa el valor de x: "))
    y= int(input ("Ingresa el valor de y: "))
comprobacion = x*y
#comprobacion para evitar que x o y queden como 0
while comprobacion == 0:
    print("Erroneo. No existe cuadrante. Introduce dos números enteros distintos de cero: ")
    x= int(input ("Ingresa el valor de x: "))
    y= int(input ("Ingresa el valor de y: "))
    comprobacion = x*y
if x>0 and y>0:
    print("El punto se ubica en el cuadrante: I")
if x<0 and y>0:
    print("El punto se ubica en el cuadrante: II")
if x<0 and y<0:
    print("El punto se ubica en el cuadrante: III")
if x>0 and y<0:
    print("El punto se ubica en el cuadrante: IV")
print("""
***Fin del programa***""")
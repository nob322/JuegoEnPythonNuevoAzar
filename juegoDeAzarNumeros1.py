#Juego basado en:
#ingresar un número, dividirlo x 4 y restarlo por un número al azar. Luego 
#adivinar cuál es el resultado, osea ese número producto de esa operación y tiene sólo 10 intentos, mostrar los intentos fallidos
#y si acierta entonces mostrarlo en pantalla.
from random import randint
import time
import msvcrt
import os
nombreJuego = "NUEVO AZAR"
restanIntentos = 10 #defino la cantidad de intentos que tendrá el jugador en ésta variable.
contadorIntentos = 0 #arrancamos el contador de vueltitas que va metiendo el bucle en 0
adivinar = 0;#con esta variable guardamos el número que el user cree que será el ganador, osea el resultado de la operación aritmética 
num = 0 #número ingresado por el usuario
numAzar = randint(1,5) #variable dónde guardamos la función azar y aclaramos que lanzará un n al azar de 0 a 5
numCuatro = 4 #guardo el número que será el multiplicable, podría haber puesto el 4 directamente en la condición booleana en restarNumeros <- (num * 4) - numAzar; 
#restarNumeros <- (num * numCuatro) - numAzar; //creamos la operación matemática que nos llevará al número que buscamos cómo jugadores he inicializamos la variable.
time.sleep(1)
nombre = input("Cómo se llama? " )
time.sleep(2)
print(f"Hola {nombre} bienvenido a {nombreJuego}, buena suerte porque realmente la va a necesitar.") #damos bienvenida al jugar
print("Tendrá que ingresar un número y luego ese número será multiplicado por x4, ese resultado será restado") # explicamos al jugador en qué consiste el juego
print("por otro número aleatorio que la computadora arrojará, usted tiene solo 10 intentos para adivinar ese resultado.")# ----
time.sleep(1)
print("Si esta listo para arrancar el juego presione una tecla...")
msvcrt.getch()
time.sleep(1)
num = int(input("Ingrese un número: "))
time.sleep(1)
print(f"ok, usted ingresó el {num}, vamos...")
restarNumeros = (num * numCuatro) - numAzar
time.sleep(1.5)
while (restarNumeros != adivinar) and (contadorIntentos < restanIntentos):
    time.sleep(1.5)
    adivinar = int(input("Cuál cree usted que será el resultado de la operación?:")) 
    #print("Le restan", (contadorIntentos - 10)," intentos.")  
    contadorIntentos = contadorIntentos + 1;   
    time.sleep(2)
    os.system ("cls") 
    if restarNumeros == adivinar:
       print("Usted acaba de pegar en el palo y ganó.") 
    else:
        print(f"Intento fallado, intente de nuevo {nombre}")
        if  (restanIntentos - contadorIntentos) >= 1:
            print("Le quedan ", (restanIntentos - contadorIntentos), " oportunidades.")
        else:
            print("Lo siento, a llorar pa la casa rosada.")    
        if (restanIntentos - contadorIntentos) <= 3 and (restanIntentos - contadorIntentos) >= 2:
            time.sleep(0.15)
            print("00000000000000000000000000000000000000000000000000000000000000000000000000000")
            time.sleep(0.15)
            print("00000000000000000000000000000000000000000000000000000000000000000000000000000")
            time.sleep(0.15)
            print("0000000   ESTÁS AL BORDE DE QUEDAR ELIMINADO DEL JUEGO                0000000")
            time.sleep(0.15)
            print("00000000000000000000000000000000000000000000000000000000000000000000000000000")
            time.sleep(0.15)
            print("00000000000000000000000000000000000000000000000000000000000000000000000000000")  
        if 	(restanIntentos - contadorIntentos) <= 1:
            time.sleep(0.15)
            print("00000000000000000000000000000000000000000000000000000000000000000000000000000")
            time.sleep(0.15)
            print("00000000000000000000000000000000000000000000000000000000000000000000000000000")
            time.sleep(0.15)
            print("0000000   HASTA LA VISTA BABY                                         0000000")
            time.sleep(0.15)
            print("00000000000000000000000000000000000000000000000000000000000000000000000000000")
            time.sleep(0.15)
            print("00000000000000000000000000000000000000000000000000000000000000000000000000000")
            time.sleep(0.15)
            print(" ")
if restarNumeros == adivinar:
    print(" ")
    time.sleep(0.6)
    print("-*-*-*-*-*-*-*-*-*-*-*-*")    
    print("Lo hizo muy bien!!! (Y)")   
    print("-*-*-*-*-*-*-*-*-*-*-*-*")  
else: 
    print(" ")
    time.sleep(0.3)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    time.sleep(0.4)
    print("Usted liquidó todos sus intentos y ha perdido el juego, definitivamente hoy no es su día de suerte.")
    time.sleep(0.4)
    print(f"El número correcto era: {restarNumeros}, otro día será.")       
    time.sleep(0.4)     
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

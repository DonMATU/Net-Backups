# Librerias a importar
from colorama import init,Fore,Back,Style
import os


init(autoreset=True)









# Variables principales
mName = "Matu's Network Backup Manager"
tName = "Gestor de copias en red."

version = 1.0





"""
La libreria de los colores funciona de la siguiente forma:
print(Fore.BLUE + "Hola Mundo")
"""

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()






def cabecera():
    print(Fore.BLUE + "===================================")
    print(mName, version)
    print(Fore.BLUE + "===================================")
    
    



# Arranca por la dercha el genio del fútbol mundial.

cabecera()
while True:
    x = int(input("Ingrese un número: "))
    if x == 1:
        break
    
    
    
print(Fore.YELLOW + "Fin del programa")
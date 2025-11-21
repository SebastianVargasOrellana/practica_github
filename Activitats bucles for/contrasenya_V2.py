import string #Introduzco la librería string para saber si hay caracteres especiales
estadísticas_correctas=0
estadísticas_incorrectas=0
#Hago un bucle para que te pida la contraseña 3 veces y la analice
for i in range (3): 
    print("""
    Versión 2 del programa de contraseñas seguras.
    Se comprueba que:
    - Haya al menos 3 números (0-9)
    - Haya al menos 3 letras (mayúsculas y minúsculas separadas)
    - Haya al menos 2 símbolos especiales (*, #, %, /, _, etc.)
    - Longitud entre 6 y 12 caracteres (criterio opcional adicional)
    - Permite introducir 3 contraseñas por ejecución
    - Muestra estadísticas de correctas e incorrectas
    """)
    contraseña=input("Introduce una contraseña: ")
    #Analiza cada carácter de la contraseña y dependiendo del tipo de caracter suma 1 a una variable
    for c in contraseña:
        numer0_4_=0
        numer5_9_=0
        mayus=0
        minus=0
        car_esp=0
        letras=mayus+minus
        numer=numer0_4_+numer5_9_
        car_espe=string.punctuation
        if c.isdigit() and 0<=int(c)<=4:
            numer0_4_+=1
        elif c.isdigit() and int(c)>=5:
            numer5_9_+=1
        elif c.isupper():
            mayus+=1
        elif c.islower():
            minus+=1
        elif car_espe:
            car_esp+=1
    #Comprueba que la contraseña tenga los caracteres de las instrucciones
    if numer>=3 and letras>=3 and car_esp>=2:
        estadísticas_correctas+=1
    #En caso de que no añade 1 a la variable de contraseñas incorrectas
    elif 6<= len(contraseña)<=12 or not (numer>=3 and letras>=3 and car_esp>=2):
        estadísticas_incorrectas+=1
#Escribe la estadística de contraseñas correctas e incorrectas
print(f"Número de contraseñas correctas: {estadísticas_correctas}")
print(f"Número de contraseñas incorrectas: {estadísticas_incorrectas}")
import string #Introduzco la librería string para saber si hay caracteres especiales
correcta_incorrecta=""
pregunta="s"
while pregunta=="s":
    print("""
    Versión 2 del programa de contraseñas seguras.
    Se comprueba que:
    - Haya al menos 3 números (0-9)
    - Haya al menos 3 letras (mayúsculas y minúsculas separadas)
    - Haya al menos 2 símbolos especiales (*, #, %, /, _, etc.)
    - Longitud entre 6 y 8 caracteres (criterio opcional adicional)
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
    if numer>=3 and letras>=3 and car_esp>=2 and 8>=len(contraseña)>=6:
        correcta_incorrecta+="correcta"
    #En caso de que no añade incorrecto a la variable de contraseñas incorrectas
    elif not 6<= len(contraseña)<=8 or not (numer>=3 and letras>=3 and car_esp>=2):
        correcta_incorrecta+="incorrecta"
    #Escribe si la contraseña es correcta o incorrecta
    print(f"Contraseña {correcta_incorrecta}")
    pregunta=input("¿Quieres introducir otra contraseña? (s/n): ")
estadísticas_correctas=0
estadísticas_incorrectas=0
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
    numer=0
    mayus=0
    minus=0
    car_esp=0
    letras=mayus+minus
    for c in contraseña:
        if c.isdigit():
            numer+=1
        elif c.isupper():
            mayus+=1
        elif c.islower():
            minus+=1
        else:
            car_esp+=1
    if numer>=3 and letras>=3 and car_esp>=2:
        estadísticas_correctas+=1
    if 6<= len(contraseña)<=12 or not (numer>=3 and letras>=3 and car_esp>=2):
        estadísticas_incorrectas+=1
print(f"Número de contraseñas correctas: {estadísticas_correctas}")
print(f"Número de contraseñas incorrectas: {estadísticas_incorrectas}")
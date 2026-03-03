import random
import time
import datetime
import sqlite3
import os
import json
def conexion_db():
    conn=sqlite3.connect("registro_ahorcado.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS partidas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha_hora TEXT,
                        tiempo_total TEXT
                    )''')
    conn.commit()
    return conn, cursor
def categoría_palabras():
    categorias={
        "Animales": {"perro", "gato", "elefante", "leon", "tigre"},
        "Frutas": {"manzana", "banana", "naranja", "uva", "fresa"},
        "Países": {"mexico", "argentina", "brasil", "españa", "francia"},
        "Random": {"python","programacion","ahorcado","juego","palabra","adivinar","letras","intentos","divertido","desafio"}
    }
    return categorias
categorias=categoría_palabras()
def guardar_partida_db(fecha_hora, tiempo_total):
    conn, cursor=conexion_db()
    cursor.execute("INSERT INTO partidas (fecha_hora, tiempo_total) VALUES (?, ?)", (fecha_hora, tiempo_total))
    conn.commit()
    conn.close()
def guardar_partida_json(fecha_hora, tiempo_total):
    partida={"fecha_hora": fecha_hora, "tiempo_total": tiempo_total}
    if os.path.exists("registro_ahorcado.json"):
        with open("registro_ahorcado.json", "r") as archivo:
            datos=json.load(archivo)
    else:
        datos=[]
    datos.append(partida)
    with open("registro_ahorcado.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
def mostrar_registro():
    conn, cursor=conexion_db()
    cursor.execute("SELECT * FROM partidas")
    partidas=cursor.fetchall()
    print("Registro de partidas:")
    for partida in partidas:
        print(f"ID: {partida[0]}, Fecha y hora: {partida[1]}, Tiempo total: {partida[2]}")
    conn.close()
def mostrar_registro_json():
    if os.path.exists("registro_ahorcado.json"):
        with open("registro_ahorcado.json", "r") as archivo:
            datos=json.load(archivo)
            print("Registro de partidas (JSON):")
            for partida in datos:
                print(f"Fecha y hora: {partida['fecha_hora']}, Tiempo total: {partida['tiempo_total']}")
    else:
        print("No hay registros en JSON.")
def eliminar_registro_db():
    conn, cursor=conexion_db()
    cursor.execute("DELETE FROM partidas")
    conn.commit()
    conn.close()
def eliminar_registro_json():
    if os.path.exists("registro_ahorcado.json"):
        os.remove("registro_ahorcado.json")
        print("Registro JSON eliminado.")
    else:
        print("No hay registros en JSON para eliminar.")
def menu():
    while True:
        print("\nMenú:")
        print("1. Jugar al Ahorcado")
        print("2. Mostrar registro de partidas (DB)")
        print("3. Mostrar registro de partidas (JSON)")
        print("4. Eliminar registro de partidas (DB)")
        print("5. Eliminar registro de partidas (JSON)")
        print("6. Salir")
        opcion=input("Selecciona una opción: ")
        if opcion=="1":
            jugar_ahorcado()
        elif opcion=="2":
            mostrar_registro()
        elif opcion=="3":
            mostrar_registro_json()
        elif opcion=="4":
            eliminar_registro_db()
        elif opcion=="5":
            eliminar_registro_json()
        elif opcion=="6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
def jugar_ahorcado():
    inicio=time.time()
    lista_fallo=['_',"_","_","_","_","_","_","_"]
    ahorcado=["A","H","O","R","C","A","D","O"]
    lista_palabras=[]
    print("Categorías disponibles:")
    for categoria in categorias:
        print(f"- {categoria}")
    contador_fallo=0
    categoria_seleccionada=input("Elige una categoría: ")
    if categoria_seleccionada in categorias:
        lista_palabras.extend(categorias[categoria_seleccionada])
    else:
        print("Categoría no válida.")
    lista_palabra=list(random.choice(lista_palabras))
    lista_letra_adivinada=["_"]*len(lista_palabra)
    print(lista_letra_adivinada)
    print("".join(lista_fallo))
    while ahorcado!=lista_fallo:
        letra=input("Adivina una letra: ").lower()
        if letra in lista_letra_adivinada:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif letra in lista_palabra:
            for i in range(len(lista_palabra)):
                if letra==lista_palabra[i]:
                    lista_letra_adivinada[i]=letra
            print(lista_letra_adivinada)        
        elif letra not in lista_palabra:
            contador_fallo+=1
            for i in range(contador_fallo):
                lista_fallo[i]=ahorcado[i]
            print(lista_letra_adivinada)
            print("".join(lista_fallo))
        elif lista_letra_adivinada==lista_palabra:
            print(f"¡Felicidades! Has adivinado la palabra: {lista_palabra}")
            break
        if contador_fallo==len(ahorcado):
            print(f"¡Has perdido! La palabra era: {lista_palabra}")
    final=time.time()
    tiempo_total=final-inicio
    fecha_hora=datetime.strftime("%Y-%m-%d %H:%M:%S", datetime.localtime())
    minutos=int(tiempo_total//60)
    segundos=int(tiempo_total%60)
    with open("registro_ahorcado.txt", "a") as archivo:
        archivo.write(f"Fecha y hora: {fecha_hora}, Tiempo total: {minutos} minutos y {segundos} segundos\n")
    guardar_partida_db(fecha_hora, f"{minutos} minutos y {segundos} segundos")
    guardar_partida_json(fecha_hora, f"{minutos} minutos y {segundos} segundos")
if __name__=="__main__":
    menu()  
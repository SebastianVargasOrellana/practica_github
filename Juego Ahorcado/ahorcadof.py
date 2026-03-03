import random
import time
lista_palabras=["python","programacion","ahorcado","juego","palabra","adivinar","letras","intentos","divertido","desafio"]
def menu_tkinter():
    import tkinter as tk
    from tkinter import messagebox
    def iniciar_juego():
        root2=tk.Tk()
        root2.withdraw()
        messagebox.showinfo("Iniciar Juego", "¡El juego del Ahorcado comenzará ahora!")
        root.destroy()
    root=tk.Tk()
    root.title("Menú del Ahorcado")
    root.geometry("300x200")
    label=tk.Label(root, text="¡Bienvenido al Ahorcado!", font=("Arial", 16))
    label.pack(pady=20)
    boton_iniciar=tk.Button(root, text="Iniciar Juego", command=iniciar_juego)
    boton_iniciar.pack(pady=10)
    root.mainloop()
def obtener_palabra():
    Palabra=random.choice(lista_palabras)
    Lista_palabras.remove(Palabra)
    return list(Palabra)
def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ["_" for i in range(len(palabra_secreta))]
    for i, letra in enumerate(palabra_secreta):
        if letra in letras_adivinadas:
            tablero[i]=letra
    return tablero
def tablero_fallos(intentos):
    Lista_ahorcado=["_", "_", "_", "_", "_", "_", "_", "_"]
    ahorcado=[" A ", "H", "O", "R", "C", "A", "D", "O"]
    for i in range(intentos):
        Lista_ahorcado[i]=ahorcado[i]
    return Lista_ahorcado
def jugar_ahorcado():
    print("¡Bienvenido al juego del Ahorcado!")
    Lista_partida=[]
    intentos=0
    Lista_palabrasecreta=obtener_palabra()
    while intentos<8 and Lista_palabrasecreta!=Lista_partida:
        tablero=mostrar_tablero(Lista_palabrasecreta, Lista_partida)
        fallos=tablero_fallos(intentos)
        print(tablero)
        print(fallos)
        letra=input("Adivina una letra: ").lower()
        if letra in Lista_partida:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue
        Lista_partida.append(letra)
        if letra in Lista_palabrasecreta:
            tablero=mostrar_tablero(Lista_palabrasecreta, Lista_partida)
            Lista_Aciertos.append(letra)
            contador_aciertos+=1
            if " ".join(tablero) == " ".join(Lista_palabrasecreta):
                partidas_ganadas+=1
                print(f"¡Felicidades! Has adivinado la palabra: {Lista_palabrasecreta}")
                break
        elif letra not in Lista_palabrasecreta:
            Lista_Errores.append(letra)
            contador_errores+=1
            fallos=tablero_fallos(contador_errores)
        else:
            partidas_perdidas+=1
            print(f"¡Has perdido! La palabra era: {Lista_palabrasecreta}")
def main():
    inicio=time.time()
    menu_tkinter()
    pregunta="s"
    while pregunta=="s":
        jugar_ahorcado()
        print(f"Número de aciertos: {contador_aciertos}")
        print(f"Número de errores: {contador_errores}")
        print(f"Porcentaje de aciertos: {(contador_aciertos/(contador_aciertos+contador_errores))*100:.2f}%")
        while pregunta!="s" or pregunta!="n":
             pregunta=input("¿Quieres jugar otra vez? (s/n): ").lower()
        Lista_palabrasecreta.append(input("Introduce una palabra para agregar a la lista de palabras: ").lower())
    print(f"Media de aciertos por partida: {contador_aciertos/(partidas_ganadas+partidas_perdidas):.2f}")
    print(f"Número de partidas ganadas: {partidas_ganadas}")
    print(f"Número de partidas perdidas: {partidas_perdidas}")
    print(f"Total de partidas jugadas: {partidas_ganadas+partidas_perdidas}")
    print(f"Porcentaje de partidas ganadas: {(partidas_ganadas/(partidas_ganadas+partidas_perdidas))*100:.2f}%")
    
    fin=time.time()
    tiempo_total=fin-inicio
    fecha_hora=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    minutos=int(tiempo_total//60)
    segundos=int(tiempo_total%60)
    with open("registro_ahorcado.txt", "a") as archivo:
        archivo.write(f"Fecha y hora: {fecha_hora}, Tiempo total: {minutos} minutos y {segundos} segundos\n")
if __name__ == "__main__":
        main()  
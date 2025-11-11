### Ejercicio 5 
nota=float(input("Introduce la nota del alumno: "))
if nota<0 or nota>10:
    print("La nota no es valida")
elif nota>=5 and nota<6.5:
    print("El alumno ha aprobado con un satisfactorio")
elif nota>=6.5 and nota<=8.5:
    print("El alumno ha aprobado con un notable")
elif nota>8.5 and nota<=10:
    print("El alumno ha aprobado con un excelente")
elif nota<5:
        print("El alumno ha suspendido")
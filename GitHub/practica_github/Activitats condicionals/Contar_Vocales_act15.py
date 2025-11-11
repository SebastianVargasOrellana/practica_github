## Contar_Vocales_act15.py
import string
frase="No hay mal que dure cien años"
#cuento las vocales
vocala=frase.count("a")
vocele=frase.count("e")
vocali=frase.count("i") 
vocalo=frase.count("o")
vocalu=frase.count("u")
vocales=vocala+vocele+vocali+vocalo+vocalu
print(frase)
print("La frase tiene ",vocales," vocales")
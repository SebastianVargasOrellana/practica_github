valor = input()
if valor.count('.') == 1 and valor.replace('.', '').isdigit():
    print("Es un número con decimales")
else:
    print("No es un número con decimales")
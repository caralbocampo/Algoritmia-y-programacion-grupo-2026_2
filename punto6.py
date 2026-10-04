letra = input("ingrese una letra:")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("es vocal")
else:
    print("no es vocal")
    if len(letra) != 1:
        print("no se puede procesar dato")


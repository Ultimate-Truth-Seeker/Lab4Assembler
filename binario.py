def intToBinary(n):
    sign = "0"
    if ("-" == n[0]):
        n = n.partition("-")[2]
        sign = "1"
    if not n.isdigit():
        return "No es un entero"
    if (int(n) > 255 or int(n) < -255):
        return "No se puede representar con 8 bits"
    n = str(format(int(n), "b"))
    for x in range(7-len(n)):
        n = "0" + n
    return sign + n

def binaryToC2(n):
    for i in n:
        if (i != "0" and i != "1"):
            return "No es un número binario"
        
    if len(n) > 8:
        return "No es un binario representable con 8 bits"
    else:
        for i in range(8-len(n)):
            n = "0"+n
    
    if (n[0] == "0"):
        return n
    else:
        c2 = ""
        for i in range(1, 8):
            c2 += "1" if n[i] == "0" else "0"
        c2 = str(format(int(c2, base = 2) + 1 + 128, "b"))
        if len(c2) > 8:
             c2 = "00000000"
        return c2

    

def hexOrDecimal(n):
    if (n.isdigit()):
        if (int(n) > 4095):
            return "No es un entero representable con 3 dígitos hexadecimales"
        return hex(int(n))
    elif ("0" == n[0] and "x" == n[1]):
        if (len(n) > 5):
            return "No es un hexadecimal representable en 3 dígitos"
        try:
            return format(int(n, base = 16), "d")
        except:
            return "No es un hexadecimal"
    return "No es un número positivo entero o hexadécimal"

def menu():
    while True:
        print("""Bienvenido, ingrese una opción
            1. Convertir Entero a binario de 8 bits (M&S)
            2. Convertir binario a Complemento 2 (asumiendo primer dígito es el signo)
            3. Convertir entre hexadecimal y decimal (tres dígitos hexadecimales)
            4. Salir""")
        while True:
            s = input()
            if s.isdigit():
                if int(s) == 1 or int(s) == 2 or int(s) == 3 or int(s) == 4:
                    s = int(s)
                    break
        
        if (s == 1):
            print(intToBinary(input("Ingrese un número entero: \n")))
        elif (s == 2):
            print(binaryToC2(input("Ingrese un número binario de 8 bits: \n")))
        elif (s == 3):
            print(hexOrDecimal(input("Ingrese un número decimal hexadecimal de tres dígitos con prefijo 0x, o un número decimal menor a 4095:\n")))
        elif (s == 4):
            return


menu()
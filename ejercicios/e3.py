try:
    p = input("primer dato: ")
    pint = int(p)
    s = input("segundo dato: ")
    sint = int(s)
    simbolo = input("Ingrese la operacion: ")

    if simbolo == "+":
        res = pint+sint
        print("resultado =", res)
    elif simbolo == "*":
        res = pint*sint
        print("resultado =", res)
    elif simbolo == "/":
        res = pint/sint
        print("resultado =" , res)
    elif simbolo == "-":
        res = pint-sint
        print("resultado =" , res)
    else:
        print("sos pelotudo!")
except:
    print("acaso sos pelotudo!")
   




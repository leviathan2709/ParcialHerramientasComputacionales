#### Julian David Riaño Tamara
#### 8963747
#### BRAYAN ESTEBAN SOLANO
#### ID:8963801
#### Parcial1

##########  BONUS  ####################################################

def cafeteriaspagobonus():
    x = int(input("Ingrese su numero de cédula: "))
    y = input("Ingrese su rol (profesor / estudiante): ")
    i = "si"
    cod = ""
    num = 0
    precioapagar = 0

    if ((y == "estudiante") or (y == "profesor")) and (x > 0):
        while i == "si":
            z = input("Ingrese código del producto a comprar: ")
            m = int(input("Ingrese cantidad de unidades a comprar: "))
            n = int(input("Ingrese precio del producto a comprar: "))

            cod += z + ". "
            total = m * n
            if (y == "estudiante") and (m > 0) and (n > 0):
                precioapagar += total * 0.5

            elif (y == "profesor") and (m > 0) and (n > 0):
                precioapagar += total * 0.8

            num += 1
            i = input("Desea comprar otro producto? (si / no): ")

        if num > 1:
            print("El " + str(y) + " con cédula " + str(x) + ", debe pagar " + str(precioapagar) + " por los productos " + cod)

        elif num == 1:
            print("El " + str(y) + " con cédula " + str(x) + ", debe pagar " + str(precioapagar) + " por el producto " + z)

        else:
            print("la información no es valida")

    else:
        print("la información no es valida")
        
cafeteriaspagobonus()

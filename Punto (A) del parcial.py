#### Julian David Riaño Tamara
#### 8963747
#### BRAYAN ESTEBAN SOLANO
#### ID:8963801
#### Parcial1

################################################################################

def cafeteriaspago():
    x = int(input("Ingrese su numero de cédula: "))
    y = input("Ingrese su rol (profesor / estudiante): ")
    z = input("Ingrese código del producto a comprar: ")
    m = int(input("Ingrese cantidad de unidades a comprar: "))
    n = int(input("Ingrese precio del producto a comprar: "))

    total = m * n

    if (y == "estudiante") and (x > 0) and (m > 0) and (n > 0):
        precioapagar = total * 0.5
        print("El " + str(y) + " con cédula " + str(x) + ", debe pagar " + str(precioapagar) + " por el producto " + z)

    elif (y == "profesor") and (x > 0) and (m > 0) and (n > 0):
        precioapagar = total * 0.8
        print("El " + str(y) + " con cédula " + str(x) + ", debe pagar " + str(precioapagar) + " por el producto " + z)

    else:
        print("la información no es valida")
        
cafeteriaspago()














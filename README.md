# *ParcialHerramientasComputacionales*
## Punto (a)
- Para recuperarse un poco del tiempo en cuarentena, las cafeterias de la universidad se encuentran dando descuentos a la comunidad estudiantil y dependiendo si es estudiante o profesor, tienen descuentos diferentes. Se desea saber entonces por cada compra cuánto debe pagar el usuario en caja.
## Entrada: 
- Número de cédula 
- Rol (profesor o estudiante)
- Código del producto
- Cantidad de unidades
- Precio del producto
### Entrada de algoritmo:
- x : Número de cédula -> Entero
- y : Rol (profesor o estudiante) -> String
- z : Código del producto -> String
- m : Cantidad de unidades -> entero
- n : Precio del producto -> entero
## Salida:
- El **Rol** con cedula **Numero**. debe pagar **Valor** por el producto **Codigo**
### Salida de algoritmo:
- print ("El" + **y** + "con cedula" + **x** + "debe pagar" + **precioapagar** + "por el producto" + **z**)
## Algoritmo:
- El usuario ingresa el número de cedula, rol, código del producto, cantidad de unidades, precio del producto, si el usuario es estudiante entonces hacer un descuento de 50% al total a pagar, si es profesor hacer un descuento de 20% al total a pagar.
### Calculo de algoritmo:
- El usuario ingresa el número de cedula que se guarda en la variable **x**, el rol se guarda en la variable **y**, el código del producto se guarda en la variable **z**, la cantidad de unidades se guarda en la variable **m**, el precio del producto se guarda en la variable **n**. se crea una variable con nombre **total** para obtener el resultado de *multiplicar* la cantidad de unidades con el precio del producto. Utilizamos condicionales para saber si el **rol** es *igual* a "**estudiante**", si la condición se cumple entonces creamos una variable con el nombre **precioapagar** para hacer la operación de 50% descuento al estudiante y luego impirmir la salida del algoritmo, si no se cumple entonces revisamos otra condición que nos permita comparar si el **rol** ingresado por el usuario es *igual* a "**profesor**", si esta condición se cumple entonces la variable **precioapagar** le damos la operación para que descuente un 20% al total, de lo contrario utilizaremos **else** para imprimir que la información no es valida.   
## La implementación de python puede verse en el archivo: "Punto (A) del parcial"

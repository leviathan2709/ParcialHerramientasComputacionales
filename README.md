# *ParcialHerramientasComputacionales*
## *Punto (a)*
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
## *Punto Bonus*
- Para recuperarse un poco del tiempo en cuarentena, las cafeterias de la universidad se encuentran dando descuentos a la comunidad estudiantil y dependiendo si es estudiante o profesor, tienen descuentos diferentes. Se desea saber entonces por cada compra cuánto debe pagar el usuario en caja.
## Entrada: 
- Número de cédula 
- Rol (profesor o estudiante)
- Código del producto
- Cantidad de unidades
- Precio del producto
- comprar más productos
### Entrada de algoritmo:
- x : Número de cédula -> Entero
- y : Rol (profesor o estudiante) -> String
- z : Código del producto -> String
- m : Cantidad de unidades -> entero
- n : Precio del producto -> entero
- i : Comprar más productos -> String
## Salida:
- El **Rol** con cedula **Numero**. debe pagar **Valor** por el producto **Codigo**, o El **Rol** con cedula **Numero**. debe pagar **Valor** por los productos **Codigo**,**Codigo**,etc.
### Salida de algoritmo:
- print ("El" + **y** + "con cedula" + **x** + "debe pagar" + **precioapagar** + "por el producto" + **z**) o print ("El" + **y** + "con cedula" + **x** + "debe pagar" + **precioapagar** + "por los productos" + **cod**)
## Algoritmo:
- El usuario ingresa el número de cedula, rol, código del producto, cantidad de unidades, precio del producto, si desea comprar otro producto, si el usuario es estudiante entonces hacer un descuento de 50% al total a pagar, si es profesor hacer un descuento de 20% al total a pagar. El usuario puede llevar más de un item (puede comprar varios productos, varias unidades)
### Calculo de algoritmo:
- El usuario ingresa el número de cedula que se guarda en la variable **x**, el rol se guarda en la variable **y**, creamos un variable **i** con una cadena "si", creamos una variable **cod** que tiene una cadena vacia, creamos una variable **num** que nos servirá de contador, creamos una variable **precioapagar** con valor de 0, procedemos a utilizar un condicional para para saber si el **rol** es *igual* a "**estudiante**" o "**profesor**" y si la cédula ingresada es mayor a cero, con el fin de poner restricciones, si la condición se cumple entonces agregamos un ciclo While con el parametro de la variable **i** sea *igual* a "si", que tendra las siguientes variables que reciben datos del usuario, el código del producto se guarda en la variable **z**, la cantidad de unidades se guarda en la variable **m**, el precio del producto se guarda en la variable **n**, tambien tiene la variable **cod** concatenando cadenas del codigo del producto, se crea una variable con nombre **total** para obtener el resultado de *multiplicar* la cantidad de unidades con el precio del producto. Utilizamos condicionales dentro del ciclo para saber si el **rol** es *igual* a "**estudiante**", si la condición se cumple entonces creamos una variable con el nombre **precioapagar** para hacer la operación de 50% descuento al estudiante, si no se cumple entonces revisamos otra condición que nos permita comparar si el **rol** ingresado por el usuario es *igual* a "**profesor**", si esta condición se cumple entonces la variable **precioapagar** le damos la operación para que descuente un 20% al total, sumamos uno a la variable **num** que funciona como contador de codigos de productos, la variable **i** le ponemos a que el usuario digite si desea comprar otro producto, dado por terminado el ciclo, agregamos unos condicionales para impimir la salida del algoritmo.  
## La implementación de python puede verse en el archivo: "Bonus del parcial"

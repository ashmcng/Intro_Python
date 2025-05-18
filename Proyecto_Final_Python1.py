
# Arreglo único para los datos de la empresa 

datos_empresa =  "Empresa: TecnoStore", "Correo: TecnoStore@gmail.com", "Teléfono: 2222-9856", "Ubicación: Heredia"
datos_usuario = []

# Función para capturar los datos del usuario

def captura_datos_usuario():
     
      nombre = input("Ingrese su nombre: ")
      correo = input("Ingrese su correo Gmail: ")
      ciudad = input("Ingrese su ciudad de residencia: ")

      datos_usuario.append(nombre)
      datos_usuario.append(correo)
      datos_usuario.append(ciudad)

      print(datos_usuario)

# FIN DEF USUARIO 


def modulo_paquetes():
    ## Definimos listas vacías en lugar de variables simples

    print("modulo_paquetes")
    opcion_producto = []
    total_factura = []
    suma_total = 0
    cambio_cliente = []
    pago_cliente = []
    opcion_paquete = 0

    while opcion_paquete != 4:
        ## Preguntamos qué paquete desea
        opcion_paquete = int(input("Hoy tenemos 3 paquetes disponibles, digite \
1 para el paquete de refrigeradora más estufa, 2 para el paquete de lavadora y secadora, \
3 para el paquete de microondas más coffee maker, o bien digite 4 para finalizar su compra: "))

        ## PAQUETE 1
        if opcion_paquete == 1:
            print("HA SELECCIONADO EL PAQUETE 1")

            producto = int(input("Digite 1 para la refrigeradora Samsung su valor es de ₡400,000 \
Digite 2 para la refrigeradora LG su valor es de ₡300,000. \
La estufa tiene un precio estándar de ₡100,000: "))
            opcion_producto.append(producto)

            if producto == 1:
                total_factura.append(500000)
                suma_total = suma_total + 500000
                print("Usted ha seleccionado la refrigeradora Samsung más la estufa. \
Su compra ha sido registrada al carrito.")

            elif producto == 2:
                total_factura.append(400000)
                suma_total = suma_total + 400000
                print("Usted ha seleccionado la refrigeradora LG más la estufa. \
Su compra ha sido registrada al carrito.")
            else:
                print("Opción no válida, intente de nuevo.")

        ## PAQUETE 2
        elif opcion_paquete == 2:
            print("HA SELECCIONADO EL PAQUETE 2")

            producto = int(input("Digite 1 para la lavadora Samsung su valor es de ₡350,000 \
Digite 2 para la lavadora LG su valor es de ₡200,000. \
La secadora tiene un precio estándar de ₡100,000: "))
            opcion_producto.append(producto)

            if producto == 1:
                total_factura.append(450000)
                suma_total = suma_total +450000
                print("Usted ha seleccionado la lavadora Samsung más la secadora. \
Su compra ha sido registrada al carrito.")

            elif producto == 2:
                total_factura.append(300000)
                suma_total = suma_total + 300000
                print("Usted ha seleccionado la lavadora LG más la secadora. \
Su compra ha sido registrada al carrito.")
            else:
                print("Opción no válida, intente de nuevo.")

        ## PAQUETE 3
        elif opcion_paquete == 3:
            print("HA SELECCIONADO EL PAQUETE 3")
            print("El microondas tiene un precio estándar de ₡35,000 y el coffee maker de ₡15,000. \
Su compra ha sido registrada a su carrito.")
            total_factura.append(50000)
            suma_total = suma_total + 50000
            opcion_producto.append(0)  # Código 0 para este paquete sin opciones

        elif opcion_paquete != 4:  # Solo mostrar mensaje si la opción es inválida
            print("Opción no válida, intenta de nuevo.")

    ## Sistema de facturación
    for contador in range(2):
        if suma_total > 0:
            print("Su pago mínimo a debitar es de", suma_total)
            pago = int(input("Digite su pago: "))
            pago_cliente.append(pago)

            if pago >= suma_total:
                cambio = pago - suma_total
                cambio_cliente.append(cambio)
                print(datos_empresa)
                print(datos_usuario)
                print("Su compra ha sido exitosa. Su pago fue de", pago,
                      ". Por ende, su vuelto es de", cambio)
                break
            elif pago < suma_total:
                print("El pago es inferior a la suma mínima de", suma_total,
                      "intente de nuevo. Tiene únicamente un intento más.")


##FIN MODULO PAQUETES
      
def modulo_productos():
    ## Definimos variables
    print("modulo_productos")
    print("BIENVENIDO AL MODULO DE VENTA DE PRODUCTOS")
    print("Tenemos 4 productos, digite 1 para agregar\
    audifonos del ₡10,000 al carrito, 2 para mouse de ₡12,000, 3 para tableta grafica de ₡16,000, \
    4 para extension de ports usb de ₡13,000, o 5  para salir")
    
    productos = 0
    vuelto = 0
    pago = 0
    suma = 0
    total = 0
    can = 0
    
    # Usamos listas para almacenar las cantidades de productos
    cantidad_productos = [0, 0, 0, 0]  # audifonos, mouse, tableta, portsusb
    precios = [10000, 12000, 16000, 13000]  # Precios de los productos
    
    while productos != 5:
        productos = int(input("Digite que opcion desea: "))  ##Preguntamos que producto desea 

        if productos == 1:
            total = precios[0]
            suma = total + suma
            cantidad_productos[0] = cantidad_productos[0] + 1
            can = can + 1
        elif productos == 2:
            total = precios[1]
            suma = total + suma
            cantidad_productos[1] = cantidad_productos[1] + 1
            can = can + 1
        elif productos == 3:
            total = precios[2]
            suma = total + suma
            cantidad_productos[2] = cantidad_productos[2] + 1
            can = can + 1
        elif productos == 4:
            total = precios[3]
            suma = total + suma
            cantidad_productos[3] = cantidad_productos[3] + 1
            can = can + 1
        elif productos != 5:  # Solo mostrar mensaje si la opción es inválida
            print("Opción no válida, intenta de nuevo.")
    
    ## Sistema de factorización
    for contador in range(2):
        if suma > 0:
            print("La cantidad total de productos comprados es de", can, "la cual se divide en:")
            print("Cantidad de audífonos:", cantidad_productos[0])
            print("Cantidad de mouse:", cantidad_productos[1])
            print("Cantidad de tabletas gráficas:", cantidad_productos[2])
            print("Cantidad de extensión de puertos USB:", cantidad_productos[3])
            print("El total a pagar por todos los productos es de", suma)
            pago = int(input("Digite su pago: "))

        if pago >= suma:
            vuelto = pago - suma
            print(datos_empresa)
            print(datos_usuario)
            print("Su compra ha sido exitosa. Su pago fue de", pago, "Por ende su vuelto es de", vuelto)
            break
        elif pago < suma:
            print("El pago es inferior a la suma mínima de", suma, "Intente de nuevo, tiene únicamente un intento más.")

## FIN MODULO PRODUCTOS 
                         
def devoluciones():
    print("BIENVENIDO AL SISTEMA DE DEVOLUCIONES")
    producto = " "
    motivo = " "
    audifonos = []
    mouse = []
    tableta = []
    portsusb = []
    can2 = 0

    while producto != "s":
        producto = input("Digite el nombre del producto que desea devolver puede devolver audifonos, \
mouse, tableta, portusb o bien digite 's' para salir del programa: ")
        
        if producto == "s":
            print("El total de devoluciones ha sido de", can2, "HAZ SALIDO DEL PROGRAMA")
            break
      
        can = int(input("Digite cuál cantidad de ese producto desea devolver: "))
        motivo = input("Cual es el motivo de la devolución: ")
        can2 = can2 + 1
        
        if producto == "audifonos":
            audifonos.append(can)
            print("El producto devuelto son audífonos. Su motivo de la devolución es:", motivo)
            print("El inventario de los audífonos devueltos es de", audifonos)
            
        elif producto == "mouse":
            mouse.append(can)
            print("El producto devuelto son mouses. Su motivo de la devolución es:", motivo)
            print("El inventario de los mouses devueltos es de", mouse)
        elif producto == "tableta":
            tableta.append(can)
            print("El producto devuelto son tabletas gráficas. Su motivo de la devolución es:", motivo)
            print("El inventario de las tabletas gráficas devueltas es de", tableta)
        elif producto == "portsusb":
            portsusb.append(can)
            print("El producto devuelto son portsusb. Su motivo de la devolución es:", motivo)
            print("El inventario de los portsusb devueltos  es de", portsusb)
        else: 
            print("El producto no es válido")



##FIN PROGRAMA DE DEVOLUCIONES

def mantenimiento_productos():
    print("BIENVENIDO AL SISTEMA DE MANTENIMIENTO DE PRODUCTOS")
    motores = "no hay actualizacion"
    valvulas = "no hay actualizacion"
    maquinas_escritorio = "no hay actualizacion"
    producto = 0

    while producto!=4:
        producto = int(input("Digite 1 para actualizar el mantenimiento de los motores, 2 para las válvulas, "
                             "3 para las máquinas de escritorio, o bien 4 para salir del programa: "))
        if producto == 1:
            motores = input("¿Cuál es el nuevo estado de los motores? ")
        elif producto == 2:
            valvulas = input("¿Cuál es el nuevo estado de las válvulas? ")
        elif producto == 3:
            maquinas_escritorio = input("¿Cuál es el nuevo estado de las máquinas de escritorio? ")
        else:
            print("El producto no es válido")
    if producto == 4:
            print("La cantidad de productos con el mantenimiento actualizado es de:", motores,  valvulas, maquinas_escritorio)
            print("El estado de los motores es de", motores)
            print("El estado de las válvulas es de", valvulas)
            print("El estado de las máquinas de escritorio es de", maquinas_escritorio)
            
##     FIN MODULO DE MANTEIMIENTO

def modulo_reportes():
    num_facturas = int(input("Digite el número de facturas que desea calcular: "))
    
    menor_200 = []
    mayor_400 = []
    suma1 = 0
    suma2 = 0
    suma_total = 0
    can_menor_200 = 0
    can_mayor_400 = 0

    for contador in range(num_facturas):
        valor = float(input("Digite el valor de la factura a clasificar:..."))
        
        if valor <= 200000:
            menor_200.append(valor)
            suma1 = suma1 + valor
            can_menor_200 = can_menor_200 + 1
        elif valor >= 400000:
            mayor_400.append(valor)
            suma2 = suma2 + valor
            can_mayor_400 = can_mayor_400 + 1
    
        suma_total = suma_total + valor
    
    print(datos_empresa)
    print("Resumen de reportes, Facturas de 200,000 o menos:", can_menor_200, "Sumatoria de facturas menores a 200,000:", suma1,
          "Facturas de 400,000 o más:", can_mayor_400, "Sumatoria de facturas mayores a 400,000:", suma2,
          "Sumatoria total de todas las facturas:", suma_total)

##FIN MODULO DE REPORTES

def menu():
    menu = 0
    while menu != 6:
        menu = int(input("Digite 1=captura_datos_usuario  2=modulo_paquetes  3=modulo_productos  4=devoluciones 5=mantenimiento_productos 6=reportes 7=SALIR"))
        if menu == 1:
           captura_datos_usuario()
        elif menu == 2:
            modulo_paquetes()
        elif menu == 3:
            modulo_productos()
        elif menu == 4:
            devoluciones()
        elif menu == 5:
            mantenimiento_productos()
        elif menu == 6:
            modulo_reportes()
        elif menu == 7:
            print("Haz salido del programa")
            break
        else:
            print("La opcion no es valida")
            break
 

# FIN MENU 

## SISTEMA LOGIN

usu = " "
contra = 0

for contador in range(3):  # Permitir hasta 3 intentos
    while usu != "admin" or usu != "secretaria" or contra != 123 or contra != 1233: 
        usu = input("Digite su usuario...: ") 
        contra = int(input("Digite su contraseña...: "))
        if usu == "admin" and contra == 123 or usu == "secretaria" and contra == 1233:  # Declaramos que ambas opciones de usuario con su respectiva contrasena
            print("Bienvenido a nuestro programa TecnoStore")
            menu()  # Llama al menú cuando los datos son correctos 
        else:
            print("Error, intente de nuevo")
            break
            
    if contador == 2:  # Cuando llega a 2 ya sería el tercer intento 
        print("Su usuario ha sido bloqueado")
        break

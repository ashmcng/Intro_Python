#SISTEMA PARQUE DE DIVERSIONES




def regalias():
      print("Bienvenido al sistema de regalias")
      mayor_n=0 
      entradas=20 
      edad=[]
      
      for i in range(20):
           print("La cantidad de entradas son de", entradas)
           
           edad=int(input("Digite su edad"))
           entradas = entradas -1
           
           if edad>=18:
               mayor_n = mayor_n +1
      print("La cantidad de personas mayores de edad que ganaron una entrada es de", mayor_n)
       
      print("YA SE AGOTO LA PROMOCION")

      
def ventas():
      print("Bienvenido al sistema de ventas")

      #a controlar los montos de las
# personas que utilizan las atracciones VIP. El parque cuenta con 4 atracciones VIP y en cada
# atracción pueden ingresar 5 personas 


      vip=[]
      #llenamos de 0
      
      for f in range(4):
           vip.append([0]*5)
      print(vip)

      #llenamos el arreglo

      print("Usted esta llenando las ventas del grupo vip 1")

      n=0

      for f in range(4):
          for c in range(5):
              n=int(input("Digite el valor monetario de la venta"))
              vip[f][c]=n
          if f == 0:
              print("Usted esta llenando las ventas del grupo vip 2")
              
          elif f == 1:
              print("Usted esta llenando las ventas del grupo vip 3")

          elif f == 2:
              print("Usted esta llenando las ventas del grupo vip 4")
              
          print(vip)

     #El programa será capaz de preguntar si desea hacer un cambio de uno de los montos, en caso
     ##afirmativo, el programa debe solicitar los índices correspondientes y el nuevo monto y realizar
     #los pasos necesarios para que el monto se vea modificado en el arreglo.
      opcion=0
      fil=0
      col=0
      n=0

      while opcion!=2:
          opcion=int(input("Digite 1 si desea cambiar un valor ingresado o bien 2 de no ser asi"))
          fil=("Digite el horacio que desea corregir del 1-4") -1
          col=("Digite el espacio que desea corregir del 1-5") -1

          for f in range(fil):
              for c in range(col):
                  n=int(input("Digite el valor monetario de la venta"))
                  vip[f][c].pos=n

      #El programadebe ser capaz de calcular el monto promedio por cada una de las atracciones VIP.

      for f in range(4):
          promedio=0
          suma=0
          for c in range(5):
               suma=suma+vip[f][c]
          promedio= suma // 5
          print("El promedio de ventas de la atraccion", str(f+1), "es de", promedio)

        
      
def atraciones():
      print("Bienvenido al sistema de atraciones")

      #El programa debe permitir la entrada de datos de 3 arreglos unidimensionales (vectores) de 10:

      #Un arreglo para nombre atracción (Caballitos, Chocones, Pacuare, Conchas)

      atraccion=[]

      # el programa debe validar a la hora de ingresar el nombre de la atracción que sean 
##   estos nombres, en caso contrario debe enviar un mensaje de inténtelo de nuevo y el programa no
##      dejara avanzar a la siguiente variable hasta que ingrese un nombre
# válido.


      opcion=" "

      while opcion!="caballitos" or opcion!="chocones" or opcion!="pacuare" or opcion!="conchas":

          for f in range(1):
               opcion=input("Digite el nombre de la atracion a la que se desea montar, las opciones son caballitos, chocones, pacuare, conchas")
            
          if opcion == "caballitos":
             print("La opcion es correcta")
             atraccion.append(opcion)
             print(atraccion)
             break
             
          elif opcion == "chocones":
             print("La opcion es correcta")
             atraccion.append(opcion)
             print(atraccion)
             break

          if opcion == "pacuare":
             print("La opcion es correcta")
             atraccion.append(opcion)
             print(atraccion)
             break
             
          if opcion == "conchas":
             print("La opcion es correcta")
             atraccion.append(opcion)
             print(atraccion)
             break
              
          else:
               print("la ocpion no es valida intentelo de nuevo")

    

      #Sistema de precio
               
      precio=[]
      fil=0
      col=0
      opcion=0

          
      fil=int(input("Digite 1 para pagar caballitos, 2 para pagar chocones, 2 para pagar pacuare y 4 para pagar concha"))
            
      for f in range(fil):
          
            int(input("Digite el precio de su atraccion seleccionada Caballitos=500, Chocones=1000, pacuare=1500, Conchas=500"))
            precio.append(opcion)
            print(precio)
            break

      # El programadebe ser capaz posterior a la capturade datos de calcular/imprimirla cantidad
#de personas que se subieron a cada atracción.

      caballitos=0
      chocones=0
      pacuare=0
      conchas=0
      
      if fil == 1:
          caballitos = caballitos + 1
      elif fil == 2:          
            chocones = chocones + 1          
      elif fil == 3:          
            pacuare = pacuare + 1     
      elif fil == 4:          
            conchas = conchas + 1
          
            print("La cantidad de personas que se subieron a los caballitos es de", caballitos, "la cantidad de personas que se subiern a los chocones es de", chocones, "La cantidad de personas\
 que se subieron al pacuare es de", pacuare, "la cantidad de personas que se subieron a las conchas es de", conchas)

      #El programa debe ser capaz de calcular/imprimir cuantas personas en cada atracción son mayores de edad

      edad=[]
      mayor_e=0
      
      edad=int(input("Digite su edad"))
      print(edad)

      


def menu():
      print("BIEVENIDO AL MENU DEL SISTEMA DEL PARQUE DIVERSIONES")

      opcion=0
      while opcion!=4:
          opcion=int(input("Digite 1 para ingresar a sistema de atracciones, digite 2 para ingresar al sistema ventas, y digite 3 para el sistema de regalias"))

          if opcion == 1:
              atraciones()
          elif opcion == 2:
                ventas()
          elif opcion == 3:
                regalias()
          elif opcion == 4:
                print("Haz salido del programa")
                break
          else:
              print("la opcion no es valida")

# SISTEMA LOGIN      
usu=" "
contra=0

for i in range(3):
    while usu!="admin" or contra!=123:
        usu=input("Digite su nombre de usuario")
        contra=int(input("Digite su contraseña"))
        if usu=="admin" and contra==123:
           menu()
        else:
            print("incorrecto")
            break
    if i == 3:
        print("Su usuario ha sido bloqueado")
        break 

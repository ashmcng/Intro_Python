# PRACTICA EVALUADA 2 ASHLEY M 

def  sistema_matematico():
       print("BIENVENIDO AL SISTEMA MATEMATICO")

       #Llenamos el arreglo de ceros 

       operaciones=[]

       for i in range(1):
             operaciones.append([0]*10)
             
       print(operaciones)

       #El usuario digita los numeros que vamos a usar para las operaciones 

       for f in range(1):
          for c in range (10):     
                n=int(input("Digite un numero.."))
                operaciones[f][c]=n
       print(operaciones)

       
       # Vamos a realizar las operaciones: calcular la suma del número en posición 1,
       ##       5 y 10.La resta entre número en posición 2 y 8. La multiplicación entre el 
       ## numero posición 9 y 3. Y la división entre el numero en posición 4 y 7.

       suma=0
       resta=0
       multi=0
       divi=0

       suma=operaciones[0][0]+operaciones[0][4]+operaciones[0][9]
       resta=operaciones[0][1]-operaciones[0][7]
       multi=operaciones[0][8]*operaciones[0][2]
       divi=operaciones[0][3]/operaciones[0][6]

       print("La suma entre la posicion 1, 5 y 10 es de.:", suma)
       print("La resta entre la posicion 2 y 8 es de..:", resta)
       print("La multiplicaion entre la posicion 9 y 3 es de..:", multi)
       print("La division entre la posicion 4 y 7 es de..:", divi)
       
             
def reserva_bus():
      print("BIENVENIDO AL LA RESERVA DE BUS")

      #Declaramos todos los asientos vacios 

      reservas=[]

      for i in range(4):
            reservas.append([0]*10)
            
      print(reservas)

       #El usuario reserva asiento
      fil=0
      col=0
      opcion=0
      
      while opcion!=2:               
          fil=int(input("Digite en que horario desea reservar su asiento, del 1-4")) -1
          
          col=int(input("Digite en que asiento se desea sentar, del 1-10")) -1 

          reservas[fil][col]=1
          
          print("Su asiento ha sido reservado con exito, este es su lugar")
          print(reservas)
          
          opcion=int(input("Digite 1 para reserva o 2 para salir del programa"))
          
      print("Haz salido del prgrama de reservas")
      
def control_notas():
      print("BIENVENIDO AL CONTROL DE NOTAS DE LA U FIDELITAS")

            #3 cursos de Programación Básica, cada curso cuenta con 5 estudiantes
      notas=[] 

      #Llenar los arreglos de 0

      for i in range(3):
           notas.append([0]*5)
           
      print(notas)

      for f in range(3):
          for c in range(5):
               print(notas[f][c],end="   ")
          print() #realiza salto de linea

      # El usuario introduce la nota final de los estudiantes 
      print("Usted esta llenando las notas del grupo 1")

      for f in range(3):
          for c in range (5):     
               n=int(input("Digite la nota.."))
               notas[f][c]=n
          if f==0:
              print("Usted esta llenando las notas del grupo 2")
              
          elif f==1:
              print("Usted esta llenando las notas del grupo 3")
          
      print(notas)
          
      for f in range(3):
          for c in range(5):
              print(notas[f][c],end="   ")
          print() #realiza salto de linea
    
      # debe calcular la nota promedio de todos los estudiantes y mostrarla al usuario.

      suma = 0
      prom = 0
      
      for f  in range (3):
          for c in range(5):
                  suma = suma + notas[f][c]
                  prom = suma // 15
      print("El promedio de las notas es de todos los estudiantes.:", prom)

      #debe calcular la nota promedio por cada uno de los grupos

      for f in range(3):
          suma = 0
          promedio = 0
          for c in range(5):
                suma= suma + notas[f][c]
          promedio=suma/5
          print("El promedio del grupo", str(f+1), "es..:", promedio)
      
     
      #debe mostrar al usuario por cada grupo cuál es el porcentaje de estudiantes aprobados.

      for f  in range (3):
          aprobado=0
          porcentaje=0
          for c in range(5):
            if notas[f][c] >= 70:
                aprobado = aprobado +1
          porcentaje = (aprobado *100) // 5
          print("El porcentaje de aprobados grupo", str(f+1), "es..:", porcentaje, "%")
      
      #cuál ha sido la nota mayor y la menor por cada uno de los grupos
      mayor=0
      menor=notas[f][c]

      for f  in range (3):
          mayor=0
          for c in range(5):
            if notas[f][c] > mayor:
               mayor = notas[f][c]
          print("El numero mayor del grupo", str(f+1), "es..:", mayor)
          
      for f  in range (3):
          menor=notas[f][c]
          for c in range(5):
            if notas[f][c] < menor:
               menor = notas[f][c]        
          print("El numero menor del grupo", str(f+1), "es..:", menor)
      
def menu():
    print("BIENVENIDO AL MENU DEL SISTEMA")
    opcion=0
    while opcion!=4:
        opcion=int(input("Digite 1 para entrar al sistema de control de notas, 2 para el sistema de \
reservar asientos en el bus, digite 3 para operaciones matematicas")) #Preguntamos al usuario que deasea hacer
    
        if opcion==1:
            control_notas()
        
        elif opcion==2:
               reserva_bus()
          
        elif opcion==3:
              sistema_matematico()
              
        elif opcion==4:
              print("Haz salido del menu")
              break
            
    
#LOGIN

usu=" "
contra=0

while usu!="admin" or contra!=123:
    usu=input("Digite su usuario...")
    contra=int(input("Digite su contraseña..."))
    
    if usu=="admin" and contra==123:
        menu()
        
print("Error, intente de nuevo")

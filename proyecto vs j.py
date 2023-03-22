#Variables y librerias
pts = 0
import random, os
from re import A
#Funcion asignar lista numeros random
def num_rand():
    '''
    Funcion para crear lista: Crea lista con orden random de numeros

    return:
    int(lista): regresa una lista de numeros
    '''

    #Creo lista con todos los numeros de juego
    numeros = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
    #Lista con los numeros ordenados aleatoriamente 
    lista = random.sample(numeros, 30)
    
    return lista
    
#Funcion llena tablero de cartas iguales     
def llena_tablero():
  '''
  Funcion para crea matriz: hace matriz con elementos iguales

  return:
  str(matriz): Regresa la matriz de 5x6 creada
  '''

  matriz=[]
  for r in range(5):
      renglon=[]
      for c in range(6):
          
          renglon.append('\U0001F0CF')
      matriz.append(renglon)
  return matriz   

#Variable global
tablero = llena_tablero()

#Funcion que despliega el formato del tablero en pantalla
def despliega_tablero(tablero):
  '''
  Funcion para desplegar tablero: despliega con formato en pantalla
  
  return:

  parametros:
  str(tablero); Lista de listas con los elementos del tablero
  
  '''  
    
  ff = 1
  print("   1     2      3     4      5      6")
  print("--------"*len(tablero))
  for renglon in tablero:
    print(ff, end="")
    ff = ff + 1
    for elemento in renglon:
        
        print(f'{elemento}'.center(5), end="")
        print("|", end="")
        
    print('\n'+"-------"*len(renglon))
    
#Funcion para hacer matriz con los numero random     
def llena_escondida():
  '''
  Funcion para crear matriz: Crea matriz con los numeros random
  
  return: 
  str(matriz): regresa la matriz creada 

  '''
  xd = num_rand()
  matriz=[]
  matriz.append(xd[0:6])
  matriz.append(xd[6:12])
  matriz.append(xd[12:18])
  matriz.append(xd[18:24])
  matriz.append(xd[24:30])
  return matriz

#Varible global
escondidas =llena_escondida()

#Funcion para limpiar pantalla
def limpia():
    if os.name == 'nt': 
        os.system('cls') 
    else:  
        os.system('clear') 

#Funcion que despliega el menu principal
def menu_principal():
    print("\na. Jugar")
    print("b. Instrucciones")
    print("c. ¿Que es un memorama?")
    print("d. salir")
    select1 = str(input("Ingresa la opción deseada: "))
    selc_menu(select1)

#Funcion para seleccionar opcion del menu
def selc_menu(op):
    '''
    Funcion que selecciona menu: Dirige a la funcion correspondiente
    
    return:

    parametros:
    str(op): Letra que el usuario ingresa para seleccionar opcion
    
    '''
    if op.lower() == "a":
        init_juego()
    elif op.lower() == "b":
        instrucciones()
        input('Enter para continuar')
        limpia()
        mensaje_inicial()
    elif op.lower() == "c":
        qes()
        input('Enter para continuar')
        limpia()
        mensaje_inicial()
    elif op.lower() == "d":
        salir()
    else:
        error()
        input('Enter para continuar')
        limpia() 
        mensaje_inicial()
        
#Funcion donde se selecciona el modo de juego
def init_juego():
    limpia()
    print("¡Modo de juego!".center(25))
    print("\nSelecciona un modo de juego")
    print("\na. 1 jugador")
    print("b. 2 juadores")
    print("c. Volver al menu\n")
    selec2 = str(input("Selecciona la opcion deseada: "))
    
    if selec2.lower() == "a":
        
        empezar_1jugador()
    elif selec2.lower() == "b":

        empezar_2jugador()
    elif selec2.lower() == "c":
        mensaje_inicial()
    else:
     
        error()
        input('Enter para continuar')
        limpia()
        init_juego()
              
 #Funcion que verifica que las coorenadas esten entre los rangos y cambia la casilla       
def verifica_cambia(c,r, tablero, escondida):
  '''
  funcion que cambia la ficha: Cambia el valor de una posicion en la matriz
  
  Return:

  parametros: 
  int(c): valor ingresado por el usuario para la columna
  int(r): valor ingresado por el usuatio para la fila
  str(tablero): Matriz que contiene las fichas del tablero
  str(escondida): Matriz con los valores de las fichas
 
  '''
  if 1<=r<=5 and 1<=c<=6:
    r = r - 1
    c = c - 1
    caso = escondida[r][c]
    
    tablero[r][c] = caso
      
  elif (r>4 or r<0):
      print('\nRenglon inválido')
  elif (c>5 or c<0):
      print('\nColumna inválida')
  else:
      error()
  
      
#Funcion que vuelve a esconder las casillas 
def cambia2(c,r, tablero):
  '''
  funcion que cambia ficha: Cambia el valor de la ficha a la carta escondida

  return:

  parametros:
  int(c): valor ingresado por el usuario para la columna
  int(r): valor ingresado por el usuatio para la fila
  srt(tablero): Matriz que contiene las fichas donde se va a cambiar

  
  '''  
  if 1<=r<=5 and 1<=c<=6:
    r = r - 1
    c = c - 1
    
    tablero[r][c] = '\U0001F0CF'
      
#Funcion pricipal para el modo de un jugador
def empezar_1jugador():
    global escondidas
    global pts
    global tablero

    #Ciclo del juego que acaba cuando el usuario llegue a 15 puntos
    while pts < 15:
        limpia()
        despliega_tablero(tablero)
        print(f"Tus puntos: {pts}")
        print("Selecciona la posicion de la carta que deseas levantar :)")
        try: 
            columna=int(input('Columna de la carta 1: '))
        except ValueError:
            limpia()
            error()
            input('Enter para continuar')
            empezar_1jugador()
        try:
            renglon=int(input('Renglón de la carta 1: '))
        except ValueError:
            limpia()
            error()
            input('Enter para continuar')
            try:
                cambia2(columna,renglon, tablero)
            except UnboundLocalError:
                limpia()
                
                
              
            empezar_1jugador()

        try: 
            x1 = tablero[renglon-1][columna-1]
        except IndexError:
            limpia()
            error()
            input('Enter para continuar')
            empezar_1jugador()
            
        if (x1 != '\U0001F0CF'):
            limpia()
            print("Esa carta ya esta seleccionada, intenta otra vez")
            input('Enter para continuar')
            empezar_1jugador()
        else:

            verifica_cambia(columna,renglon, tablero, escondidas)
            try:
                y1 = escondidas[renglon-1][columna-1]
            except IndexError:
                limpia()
                input('Enter para continuar')
                cambia2(columna,renglon, tablero)
                empezar_1jugador()
               
            limpia()
            despliega_tablero(tablero)
            try:
                columna2=int(input('Columna de la carta 2: '))
            except ValueError:
                limpia()
                print("Error Vuelve a intentarlo")
                cambia2(columna,renglon, tablero)
                input('Enter para continuar')
                empezar_1jugador()
            try: 
                renglon2=int(input('Renglón de la carta 2: '))
            except ValueError:
                limpia()
                print("Error Vuelve a intentarlo")
                input('Enter para continuar')
                cambia2(columna,renglon, tablero)
                empezar_1jugador()
            
           
            if (columna == columna2 and renglon == renglon2):
                limpia()
                print("La carta es la misma, vuelve a intentalo")
                input('Enter para continuar')
                cambia2(columna,renglon, tablero)
                cambia2(columna2,renglon2, tablero)
    
            
            else:
                try:
                    x2 = tablero[renglon2-1][columna2-1]
                except IndexError:
                    limpia()
                    error()
                    input('Enter para continuar')
                    cambia2(columna,renglon, tablero)
                    empezar_1jugador()
                    
                    
                if (x2 != '\U0001F0CF'):
                    limpia()
                    print("Esa carta ya esta seleccionada, intenta otra vez")
                    input('Enter para continuar')
                    cambia2(columna,renglon, tablero)
                    empezar_1jugador()
                else: 
                    
                    
                    verifica_cambia(columna2,renglon2, tablero, escondidas)
                    try: 
                        y2 = escondidas[renglon2-1][columna2-1]
                    except IndexError:
                        limpia()
                        input('Enter para continuar')
                        cambia2(columna,renglon, tablero)
                        empezar_1jugador()
            
            
                    limpia()
                    despliega_tablero(tablero)
                    if (y1 == y2):
            
                        print("Muy bien!! Par encontrado")
                        pts = pts + 1
                        input('Enter para continuar')
            
                    else:
                        print("Las cartas no son pares")
                        cambia2(columna,renglon, tablero)
                        cambia2(columna2,renglon2, tablero)
                        input('Enter para continuar')
    limpia()
    despliega_tablero(tablero)
    print("Ganaste!! Fin del juego")
    pts = 0
    input('Enter para continuar')
    tablero = llena_tablero()
    escondidas =llena_escondida()
    menu_principal()
    
#Funcion principal para el modo de dos jugadores
def empezar_2jugador():
    limpia()
    print("En proceso...")
    input('Enter para continuar')
    limpia()
    mensaje_inicial()
    
#Funcion que despliega las instrucciones     
def instrucciones():
    limpia()
    print("Instrucciones".center(60))
    print("\nPara un judador:\n")
    
    #Llama a archivo y lo lee
    inst1 = open("instrucciones1.txt","r")
    conten = inst1.read()
    print(conten)
    inst1.close()
    
    #Llama a archivo y lo lee
    print("\nPara dos judadores:\n")
    inst2 = open("instrucciones2.txt","r")
    conten2 = inst2.read()
    print(conten2)
    inst2.close()

#Funcion que despliega que es un memorama
def qes():
     limpia()
     print("¿Que es un memorama?\n".center(60))
     
     #Llama a archivo y lo lee
     whatis = open("qes.txt","r")
     conten3 = whatis.read()
     print(conten3)
     whatis.close()
    
    
#Funcion que termina el programa
def salir():
    limpia()
    print("Fin del juego. Ten un buen dia")
  

#Funcion para marca un error en el programa
def error():
    limpia()
    print("Error".center(15))
    print("\nOpcion no valida!!\n")
    

#Funcion que despliega el mensaje inicial   
def mensaje_inicial():
    limpia()
    print("¡Memorama!".center(40))
    print('''\nEl memorama es un juego divertido que te
ayudara a mantener tus capacidades congitivas''')
    print("\nMenu principal")
    
    menu_principal()

#Main
def main():
    
    mensaje_inicial()

#Llama a funcion
main()

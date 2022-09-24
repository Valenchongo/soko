from shutil import move
import string

def crear_grilla(grilla):
    f = len(grilla)
    for i in range(0,f):
        grilla [i] =list(grilla[i])
    return grilla

def dimensiones(grilla):
    filas = int(len(grilla))
    columnas = int(len(grilla[0]))
    return columnas,filas

def hay_pared(grilla,c,f):
   if grilla[f][c] == "#":
        return True
   
def hay_objetivo(grilla,c,f):
    if grilla[f][c] == "." or grilla[f][c] =="+" or grilla[f][c] =="*":
        return True
    
def hay_jugador(grilla,c,f):
    if grilla[f][c] =="@" or grilla[f][c] =="+":
        return True
  
def hay_caja(grilla,c,f):
    if grilla[f][c] == "$" or grilla[f][c] =="*":
        return True
  
def juego_ganado(grilla):
    c,f=dimensiones(grilla)
    for i in range(0,f):
        fila = grilla[i]
        for p in range (0,c):
            if fila[p] == "." or fila[p] =="+":
                return False        
    return True

def Movimiento(grilla ,pos_x, pos_y, direccion, jugador_solo):
    grilla_2 = crear_grilla(grilla[:])
   
    if direccion[0] == 0 and direccion[1] ==-1:
           pos_x_1,pos_x_2,pos_y_1,pos_y_2 = pos_x-1,pos_x-2,pos_y,pos_y 

    elif direccion[0] == 0 and direccion[1] ==1: 
            pos_x_1,pos_x_2,pos_y_1,pos_y_2 = pos_x+1,pos_x+2,pos_y,pos_y   

    elif direccion[0] == -1 and direccion[1] == 0:
         pos_x_1,pos_x_2,pos_y_1,pos_y_2 = pos_x,pos_x,pos_y-1,pos_y-2   
    

    elif direccion[0] == 1 and direccion[1] ==0:
         pos_x_1,pos_x_2,pos_y_1,pos_y_2 = pos_x,pos_x,pos_y+1,pos_y+2 
         

    if hay_pared(grilla_2,pos_y_1,pos_x_1):
            return grilla_2 

    elif  hay_caja(grilla_2,pos_y_1,pos_x_1) and hay_objetivo(grilla_2,pos_y_1,pos_x_1):
            
            if  grilla_2[pos_x_2][pos_y_2] == " ":  
             if jugador_solo:    
              grilla_2[pos_x][pos_y] = " " 
             else:grilla_2[pos_x][pos_y] = "."  
             grilla_2[pos_x_1][pos_y_1] = "+"   
             grilla_2[pos_x_2][pos_y_2] = "$"               
             return grilla_2            


            if  hay_objetivo(grilla_2,pos_y_2,pos_x_2):
              if jugador_solo:
               grilla_2[pos_x][pos_y] = " " 
              else:grilla_2[pos_x][pos_y] = "." 
              grilla_2[pos_x_1][pos_y_1]  = "+"   
              grilla_2[pos_x_2][pos_y_2] = "*"            
              return grilla_2    

            if hay_pared(grilla_2,pos_y_2,pos_x_2):
                return grilla_2
            if hay_caja(grilla_2,pos_y_2,pos_x_2):
                return grilla_2    

    elif hay_caja(grilla_2,pos_y_1,pos_x_1):          

            if hay_objetivo(grilla_2,pos_y_2,pos_x_2) and grilla_2[pos_x_2][pos_y_2] != "*":
              if jugador_solo:  
               grilla_2[pos_x][pos_y] = " "
              else: grilla_2[pos_x][pos_y] = "."   
              grilla_2[pos_x_1][pos_y_1] = "@" 
              grilla_2[pos_x_2][pos_y_2] = "*"             
              return grilla_2
                                       
            if grilla_2[pos_x_2][pos_y_2] == " ": 
               if jugador_solo:  
                grilla_2[pos_x][pos_y] = " "
               else: grilla_2[pos_x][pos_y] = "."  
               grilla_2[pos_x_1][pos_y_1] = "@"  
               grilla_2[pos_x_2][pos_y_2] = "$"             
               return grilla_2

            if hay_caja(grilla_2,pos_y_2,pos_x_2):
               return grilla_2   
            if hay_pared(grilla_2,pos_y_2,pos_x_2):
               return grilla_2 
            if grilla_2[pos_x_2][pos_y_2] == "*": 
                return grilla_2       

    elif hay_objetivo(grilla_2, pos_y_1, pos_x_1):
            if jugador_solo:
             grilla_2[pos_x][pos_y] = " " 
            else:grilla_2[pos_x][pos_y] = "."  
            grilla_2[pos_x_1][pos_y_1] = "+"           
            return grilla_2
                    
    elif grilla_2[pos_x_1][pos_y_1] == " ":
           if jugador_solo: 
            grilla_2[pos_x][pos_y] = " "  
           else:
            grilla_2[pos_x][pos_y] = "." 
           grilla_2[pos_x_1][pos_y_1] = "@"
           return grilla_2
    
def mover(grilla,direccion):
     c,f=dimensiones(grilla)
     for i in range(0,f):
        grilla[i] =list(grilla[i]) 
        for p in range (0,c):
            if grilla[i][p] == "@" or grilla[i][p] == "+" :
                jugador_solo=False
                if grilla[i][p] == "@":                    
                    jugador_solo = True                   
                pos_x=int(i)
                pos_y=int(p)
                break
     nueva_grilla = Movimiento(grilla , pos_x , pos_y , direccion , jugador_solo)
     return nueva_grilla
     
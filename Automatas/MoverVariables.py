# -*- coding: utf-8 -*-

import tkinter.messagebox

class MoverVariables:
    
    # INICIALIZADOR print(self.programa[self.cabezal])
    def __init__(self, cadena,cabezal,variable1,variable2):
        self.programa = list(cadena)
        self.variable1 = variable1
        self.variable2= variable2
        self.v1 = self.variable1
        self.v2 = self.variable2
        self.cont = 0
        self.digito = ''
        self.valor = ''
        self.ascii = chr(70)
        self.automata = []
        self.cabezal = cabezal
        self.Activador()
    

       
    def Activador(self):
        conta = 0
        self.DesplazarDraIzq()
        self.BuscarVariable(self.v1)
        
        if self.variable1 == 'A'  and  self.variable2 == 'C':
            self.moverDerecha(self.v2)
            self.BuscarVariable(self.v1)
            self.moverDerecha(self.v2)
            self.BuscarVariable(self.v1)
            self.moverDerecha(self.v2)
            self.cerrar(self.valor)
            
        if self.variable1 == 'A'  and  self.variable2 == 'B':
            self.moverDerecha(self.v2)
            self.BuscarVariable(self.v1)
            self.moverDerecha(self.v2)
            self.BuscarVariable(self.v1)
            self.moverDerecha(self.v2)
            self.cerrar(self.valor)
            
        if self.variable1 == 'C'  and  self.variable2 == 'A':
            self.BuscarVariable(self.v2)
            self.moverDerecha(self.v1)            
            self.BuscarVariable(self.v2)
            #print(self.v1)
            self.moverDerecha(self.v1)
            #print(self.v1)
            self.BuscarVariable(self.v2)
            self.cerrar(self.valor)
        
        if self.variable1 == 'C'  and  self.variable2 == 'B':
            self.BuscarVariable(self.v2)
            #print(self.v1)
            self.moverDerecha(self.v1)
            self.BuscarVariable(self.v2)
            #print(self.v1)
            self.moverDerecha(self.v1)
            #print(self.v1)
            self.BuscarVariable(self.v2)
            self.cerrar(self.valor)
        
        if self.variable1 == 'B'  and  self.variable2 == 'A':
            self.BuscarVariable(self.v2)
            #print(self.v1)
            self.moverDerecha(self.v1)
            self.BuscarVariable(self.v2)
            #print(self.v1)
            self.moverDerecha(self.v1)
            #print(self.v1)
            self.BuscarVariable(self.v2)
            self.cerrar(self.valor)
        
        if self.variable1 == 'B'  and  self.variable2 == 'C':
            self.moverDerecha(self.v2)
            self.BuscarVariable(self.v1)
            self.moverDerecha(self.v2)
            self.BuscarVariable(self.v1)
            self.moverDerecha(self.v2)
            self.cerrar(self.valor)

    
    def DesplazarDraIzq(self):
        #self.cabezal = self.cabezal +1
        digito = self.programa[self.cabezal]
        #print(digito,'<---------------------')
        
        if digito == '0':
            
            #---------------Movimiento en cinta metrica-----------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = 'X'
            #---------------Fin movimiento en cinta metrica------------------- 
            self.valor = 'X'
            
        elif digito == '1':            
            print('esta por aca relajadito sin hacer ni chimba')
            #---------------Movimiento en cinta metrica-----------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = 'Y'
            #---------------Fin movimiento en cinta metrica-------------------
            self.valor = 'Y'
            
     # BUSCA LA VARIABLE A LA IZQUIERDA 
    def BuscarVariable(self,v): 
        estados = ''
        estadosS = ''
        estadosT = []
        self.cabezal = self.cabezal -1
       
        
        # CONDICION PARA MOVERSE HACIA ATRAS EN BUSCA DE LA VARIABLE
        while self.programa[self.cabezal] != v:
            
            #---------------Movimiento en cinta metrica-----------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-------------------
            
            # CONDICIONES PARA CREAR EL AUTOMATA                
            if self.programa[self.cabezal] == 'A':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',L|'               
            elif self.programa[self.cabezal] == 'B':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',L|'                   
            elif self.programa[self.cabezal] == 'C':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',L|'                     
            elif self.programa[self.cabezal] == 'T':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',L|'                     
            elif self.programa[self.cabezal] == '0':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',L|'                     
            elif self.programa[self.cabezal] == '1':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',L|' 
                
            # CONDICION PARA CREAR EL AUTOMARA 
            if estados not in estadosT:
                estadosT.append(estados)
                estadosS = estadosS + estados
            
            # CABEZAL
            self.cabezal = self.cabezal - 1
        
            
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------
        
        # INCERTA LOS ESTADOS Y LA ACCION
        self.automata.append([self.ascii+str(self.cont),estadosS,self.ascii+str(self.cont)])
        self.cont = self.cont + 1 
        self.automata.append([self.ascii+str(self.cont-1),self.variable1+'|'+self.variable1+'|R',self.ascii+str(self.cont)])
        

        
        if self.programa[self.cabezal] == 'Y' or self.programa[self.cabezal] == 'X':
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'            
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'

        
        self.cabezal = self.cabezal + 1
        
        #print(self.digito)
        
        if self.digito == '':
            if (self.programa[self.cabezal] == '0'):
                #---------------Movimiento en cinta metrica-----------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'X'
                #---------------Fin movimiento en cinta metrica-------------------
                self.digito = 'X'
                self.v1 = self.digito
                #self.digito  =''
            elif self.programa[self.cabezal] == '1':
                #---------------Movimiento en cinta metrica-----------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'Y'
                #---------------Fin movimiento en cinta metrica------------------- 
                self.digito = 'Y'
                self.v1 = self.digito
                #self.digito = ''
        else:
            if (self.programa[self.cabezal] == '0'):
                #---------------Movimiento en cinta metrica-----------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = self.digito
                #---------------Fin movimiento en cinta metrica-------------------
                self.v2 = self.digito
                #self.digito = ''
            elif self.programa[self.cabezal] == '1':
                #---------------Movimiento en cinta metrica-----------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = self.digito
                #---------------Fin movimiento en cinta metrica------------------- 
                self.v2 = self.digito
                #self.digito  = ''
        ##print("izq ",self.programa[self.cabezal], "dig ",self.digito)
        ##print(self.v1,"---",self.v2)
    
        
        
    # BUSCA LA VARIABLE A LA DERECHA           
    def moverDerecha(self,va):
        
        # CABEZAL
        self.cabezal = self.cabezal + 1
        
        #VARIABLES
        estados = ''
        estadosS = ''
        estadosT = []
        auxiliar = ''
        
        #print(va)

    # CICLO PARA RECORRE LA CINTA EN BUSCA DE UNA Z HACIA LA DERECHA Y CREA EL AUTOMATA
        while self.programa[self.cabezal] != va:           
            
        #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------

        # CONDICIONALES PARA EVALUAR LOS NODOS Y MOVERSE A LA DERECHA EN BUSCA DE UNA Z
            if self.programa[self.cabezal] == 'A':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'               
            elif self.programa[self.cabezal] == 'B':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'                
            elif self.programa[self.cabezal] == 'C':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'               
            elif self.programa[self.cabezal] == 'T':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'               
            elif self.programa[self.cabezal] == '0':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'                 
            elif self.programa[self.cabezal] == '1':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|' 
        
        # CONDICION PARA CREAR EL AUTOMARA 
            if estados not in estadosT:
                estadosT.append(estados)
                estadosS = estadosS + estados
            self.cabezal = self.cabezal + 1          
        
            
    # INCERTA LOS ESTADOS Y LA ACCION
        self.automata.append([self.ascii+str(self.cont),estadosS,self.ascii+str(self.cont)])
        self.cont = 1
        self.automata.append([self.ascii+str(self.cont-1),self.v2+'|'+self.v2+'|R',self.ascii+str(self.cont)])
        
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------  
        
        #print("der ",self.programa[self.cabezal], "dig ",self.digito)
        if self.programa[self.cabezal] == 'Y' or self.programa[self.cabezal] == 'X':
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'   
                if self.variable1 == 'C' and self.variable2 == 'A':
                    self.digito = ''
                elif self.variable1 == 'C' and self.variable2 == 'B':
                    self.digito = ''
                elif self.variable1 == 'B' and self.variable2 == 'A':
                    self.digito = ''
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'
                if self.variable1 == 'C' and self.variable2 == 'A':
                    self.digito = ''
                elif self.variable1 == 'C' and self.variable2 == 'B':
                    self.digito = ''
                elif self.variable1 == 'B' and self.variable2 == 'A':
                    self.digito = ''
        
        self.cabezal = self.cabezal+1  
        
        #print(self.programa[self.cabezal])
        if self.digito == '':
            if (self.programa[self.cabezal] == '0'):
                #---------------Movimiento en cinta metrica-----------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'X'
                #---------------Fin movimiento en cinta metrica-------------------
                self.digito = 'X'
                self.v1 = self.digito
            elif self.programa[self.cabezal] == '1':
                #---------------Movimiento en cinta metrica-----------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'Y'
                #---------------Fin movimiento en cinta metrica------------------- 
                self.digito = 'Y'
                self.v1 = self.digito
        elif self.digito != '':
            if(self.programa[self.cabezal] == '0'):
                #---------------Movimiento en cinta metrica-----------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = self.digito
                #---------------Fin movimiento en cinta metrica------------------- 
                self.v2 = self.digito
                self.digito = ''
            elif self.programa[self.cabezal] == '1':
                #---------------Movimiento en cinta metrica-----------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = self.digito
                #---------------Fin movimiento en cinta metrica------------------- 
                self.v2 = self.digito
                self.digito = ''
        
        

    def cerrar (self,valor):
        # CABEZAL
        self.cabezal = self.cabezal + 1
        
        #VARIABLES
        estados = ''
        estadosS = ''
        estadosT = []
        auxiliar = ''
        
        #print(va)

        # CICLO PARA RECORRE LA CINTA EN BUSCA DE UNA Z HACIA LA DERECHA Y CREA EL AUTOMATA
        while self.programa[self.cabezal] != valor:           
            
        #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------

        # CONDICIONALES PARA EVALUAR LOS NODOS Y MOVERSE A LA DERECHA EN BUSCA DE UNA Z
            if self.programa[self.cabezal] == 'A':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'               
            elif self.programa[self.cabezal] == 'B':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'                
            elif self.programa[self.cabezal] == 'C':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'               
            elif self.programa[self.cabezal] == 'T':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'               
            elif self.programa[self.cabezal] == '0':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|'                 
            elif self.programa[self.cabezal] == '1':
                estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|' 
        
        # CONDICION PARA CREAR EL AUTOMARA 
            if estados not in estadosT:
                estadosT.append(estados)
                estadosS = estadosS + estados
            self.cabezal = self.cabezal + 1          
        
            
    # INCERTA LOS ESTADOS Y LA ACCION
        self.automata.append([self.ascii+str(self.cont),estadosS,self.ascii+str(self.cont)])
        self.cont = 1
        self.automata.append([self.ascii+str(self.cont-1),self.v2+'|'+self.v2+'|R',self.ascii+str(self.cont)])
        
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------  



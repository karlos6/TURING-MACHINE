# -*- coding: utf-8 -*-
import tkinter.messagebox

class MoverIzquierdaV:
    
    # INICIALIZADOR 
    def __init__(self, cadena,cabezal,variable):
        self.programa = list(cadena)
        self.variable = variable
        self.cont = 0
        self.ascii = chr(70)
        self.automata = []
        self.cabezal = cabezal
        self.Activador()
        
    # ACTIVADOR DE METODOS
    def Activador(self):
        conta = 0
        
        # LOS SIGUIENTES VALORES DESPUES DE LA VARIABLE
        while conta != 2:            
            self.cabezal = self.cabezal + 1 
            self.cont = self.cont + 1             

            # CUANDO EL SIGIENTE VARIABLE VALOR SEA '0'
            if self.programa[self.cabezal] == '0':                
                #---------------Movimiento en cinta metrica--------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'X'
                #---------------Fin movimiento en cinta metrica---------------                
                #posible error armado de automata****************************
                self.automata.append([self.ascii+str(self.cont-1),'0,X,L',self.ascii+str(self.cont)])
                self.BuscarVariable('X',conta)
                self.moverDerecha('X')
                self.variable = 'X' 
                
            # CUANDO EL SIGIENTE VARIABLE VALOR SEA '1'    
            elif self.programa[self.cabezal] == '1':
                #---------------Movimiento en cinta metrica--------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'Y'
                #---------------Fin movimiento en cinta metrica---------------                
                #posible error armado de automata****************************
                self.automata.append([self.ascii+str(self.cont-1),'1,Y,L',self.ascii+str(self.cont)])   
                self.BuscarVariable('Y',conta)
                self.moverDerecha('Y')    
                self.variable = 'Y'
            conta = conta + 1
        
    # BUSCA LA VARIABLE A LA IZQUIERDA 
    def BuscarVariable(self,v,c): 
        estados = ''
        estadosS = ''
        estadosT = []
        self.cabezal = self.cabezal -1
       
        # CONDICION PARA MOVERSE HACIA ATRAS EN BUSCA DE LA VARIABLE
        while self.programa[self.cabezal] != self.variable:
            
            #---------------Movimiento en cinta metrica-----------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASsssssssssssssO:", str(self.programa))
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
        
        
        
        # CONDICIONAL PARA CAMBIAR LAS VARIABLES CUANDO SE MUEVA A LA IZQUIERDA  
        if self.programa[self.cabezal]== 'X':
            self.programa[self.cabezal] = '0'            
        elif self.programa[self.cabezal]== 'Y':
            self.programa[self.cabezal] = '1'
        
        # CABEZAL            
        self.cabezal = self.cabezal + 1
                       
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO111111111:", str(self.programa))
        self.programa[self.cabezal] = v
        #---------------Fin movimiento en cinta metrica-----------------------
        
        # CONDICIONAL PARA CAMBIAR LAS VARIABLES CUANDO SE MUEVA A LA DERECHA
        if c == 1:
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'
                self.automata.append([self.ascii+str(self.cont-1),self.variable+'|'+'0'+'|R',self.ascii+str(self.cont)])
                self.automata.append([self.ascii+str(self.cont-1),self.programa[self.cabezal]+'|'+'0'+'|R',self.ascii+str(self.cont)])
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'
                self.automata.append([self.ascii+str(self.cont-1),self.variable+'|'+'1'+'|R',self.ascii+str(self.cont)])
                self.automata.append([self.ascii+str(self.cont-1),self.programa[self.cabezal]+'|'+'1'+'|R',self.ascii+str(self.cont)])
        elif c == 0:
            self.automata.append([self.ascii+str(self.cont-1),self.variable+'|'+self.variable+'|R',self.ascii+str(self.cont)])
            self.cont = self.cont + 1
            # CABEZAL
            self.cabezal = self.cabezal + 1
            self.automata.append([self.ascii+str(self.cont-1),self.programa[self.cabezal]+'|'+v+'|R',self.ascii+str(self.cont)])
            
            
    # BUSCA LA VARIABLE A LA DERECHA           
    def moverDerecha(self,va):
        


        #VARIABLES
        estados = ''
        estadosS = ''
        estadosT = []
        auxiliar = ''

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
        self.cont = self.cont + 1
        
        
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------       
        
        # CAMBIO DE VARIABLE DE EN LA DERECHA
        if self.programa[self.cabezal]== 'X':
            self.programa[self.cabezal] = '0'
            self.automata.append([self.ascii+str(self.cont-1),va+'|'+'0'+'|R',self.ascii+str(self.cont)])            
        elif self.programa[self.cabezal]== 'Y':
            self.automata.append([self.ascii+str(self.cont-1),va+'|'+'1'+'|R',self.ascii+str(self.cont)])
            self.programa[self.cabezal] = '1'
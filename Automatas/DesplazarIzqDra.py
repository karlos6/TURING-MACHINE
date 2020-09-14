# -*- coding: utf-8 -*-
import tkinter.messagebox

class DesplazarIzqDra:
        # INICIALIZADOR 
    def __init__(self, cadena,ejecucion,cabezal):
        self.programa = list(cadena)
        self.cont = 0
        self.ascii = chr(68)
        self.automata = []
        self.cabezal = cabezal
        self.activador(ejecucion)
        
    def activador(self,ejecucion):
        self.inicioAutomata(ejecucion) 
        self.sacarVariable()
        self.DesplazarDraIzq()
        print(self.variable)
        self.moverDerecha(self.variable)
        
    def inicioAutomata(self,ejecucion):
        listaP = []
        for i in ejecucion:
            self.cont = self.cont + 1
            listaP.append([self.ascii+str(self.cont-1),i+','+i+',R',self.ascii+str(self.cont)])
        self.automata.append(listaP)
     
    
    def sacarVariable(self):
        codigoVar = ''
        variable = '' 
        esta = 0
        while esta != 2:
            self.cabezal = self.cabezal + 1
            self.cont = self.cont + 1            
            #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-----------------------
            codigoVar = codigoVar + self.programa[self.cabezal]
            esta = esta + 1
            
        self.variable = self.variables(codigoVar)  
        print(variable)
        
        
    
    def DesplazarDraIzq(self):
        self.cabezal = self.cabezal +1
        digito = self.programa[self.cabezal]
        print(digito,'<---------------------')
        
        if digito == '0':
            
            #---------------Movimiento en cinta metrica-----------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = 'X'
            #---------------Fin movimiento en cinta metrica------------------- 
            self.moverseIzquierda(digito)
            self.variable = 'X'
            
        elif digito == '1':            
            print('esta por aca relajadito sin hacer ni chimba')
            #---------------Movimiento en cinta metrica-----------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = 'Y'
            #---------------Fin movimiento en cinta metrica-------------------
            self.moverseIzquierda(digito)
            self.variable = 'Y'
       
        
    def moverseIzquierda(self,digito):
        
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
        self.automata.append([self.ascii+str(self.cont-1),self.variable+'|'+self.variable+'|R',self.ascii+str(self.cont)])
        
        self.cabezal = self.cabezal +1
        
        self.condicion_1o0(digito)
        
    def condicion_1o0(self,c):
        if c == '1':
            #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = '0'
            #---------------Fin movimiento en cinta metrica-----------------------
            
            self.cabezal = self.cabezal +1
            
            #---------------Movimiento en cinta metrica---------------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-----------------------
            print('acabo')
            
        elif c == '0':
            #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-----------------------
            
            self.cabezal = self.cabezal +1
            
            aux = self.programa[self.cabezal]
            
            if aux == '0':
                
                #---------------Movimiento en cinta metrica--------------------
                auxiliar = self.programa[self.cabezal]
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = '0'
                #---------------Fin movimiento en cinta metrica----------------
                
                self.cabezal = self.cabezal - 1
                
                #---------------Movimiento en cinta metrica--------------------
                auxiliar = self.programa[self.cabezal]
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = '0'
                #---------------Fin movimiento en cinta metrica----------------
                
                
                
            elif aux == '1':
                #---------------Movimiento en cinta metrica--------------------
                auxiliar = self.programa[self.cabezal]
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = '0'
                #---------------Fin movimiento en cinta metrica----------------
                
                self.cabezal = self.cabezal - 1
                
                #---------------Movimiento en cinta metrica--------------------
                auxiliar = self.programa[self.cabezal]
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = '1'
                #---------------Fin movimiento en cinta metrica----------------
            

    # BUSCA LA VARIABLE A LA DERECHA           
    def moverDerecha(self,va):
        
        # CABEZAL
        self.cabezal = self.cabezal + 1

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
        self.cont = 1
        self.automata.append([self.ascii+str(self.cont-1),self.variable+'|'+self.variable+'|R',self.ascii+str(self.cont)])
        
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------       
        
        # CAMBIO DE VARIABLE DE EN LA DERECHA
        if self.programa[self.cabezal]== 'X':
            self.programa[self.cabezal] = '0'            
        elif self.programa[self.cabezal]== 'Y':
            self.programa[self.cabezal] = '1'
            
            
            
        
        


    
    
    
    
    
        
    def variables(self, op):
            return{
                '00': self.V1A(op),
                '01': self.V2B(op),
                '10': self.V3C(op)
            }.get(op)  
        
    def V1A(self,op):
        listaV = []
        for i in op:
            self.cont = self.cont + 1
            listaV.append([self.ascii+str(self.cont-1),i+','+i+',R',self.ascii+str(self.cont)])
        self.automata.append(listaV)      
        return 'A'
    
    def V2B(self,op):
        listaV = []
        for i in op:
            self.cont = self.cont + 1
            listaV.append([self.ascii+str(self.cont-1),i+','+i+',R',self.ascii+str(self.cont)])
        self.automata.append(listaV)   
        return 'B'
    
    def V3C(self,op):
        listaV = []
        for i in op:
            self.cont = self.cont + 1
            listaV.append([self.ascii+str(self.cont-1),i+','+i+',R',self.ascii+str(self.cont)])
        self.automata.append(listaV) 
        return 'C'
        
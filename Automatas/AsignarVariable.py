# -*- coding: utf-8 -*-
import tkinter.messagebox

class AsignarVariable:
    
    # INIT DEL OBJETO
    def __init__(self, cadena,ejecucion,cabezal):
        self.programa = list(cadena)
        self.cont = 0
        self.ascii = chr(65)
        self.automata = []
        self.cabezal = cabezal
        self.activador(ejecucion)
        self.v1 = ''
        self.v2 = ''
        self.retorno = ''

    # ACTIVADOR DE METODOS
    def activador(self,ejecucion):
        self.inicioAutomata(ejecucion)
        self.sacarVariables()
        
    # INICIA EL AUTOMATA
    def inicioAutomata(self,ejecucion):
        listaP = []
        for i in ejecucion:
            self.cont = self.cont + 1
            listaP.append([self.ascii+str(self.cont-1),i+','+i+',R',self.ascii+str(self.cont)])
        self.automata.append(listaP)
        
    def sacarVariables(self):
        codigoVar = ''
        esta = 0
        while esta != 4:
            self.cabezal = self.cabezal + 1
            self.cont = self.cont + 1            
            #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-----------------------
            codigoVar = codigoVar + self.programa[self.cabezal]
            
            if esta == 1:
                codigoVar = codigoVar + '-'           
            esta = esta + 1
            
            
        if self.programa[self.cabezal]== '0':            
            #---------------Movimiento en cinta metrica---------------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = 'X'
            #---------------Fin movimiento en cinta metrica-----------------------
            self.retorno = 'X'
            separado = codigoVar.split('-')
            self.v1 = self.variables(separado[0])
            self.v2 = self.variables(separado[1])
            self.recorrerIzqDer()
            print(self.programa)
            
        elif self.programa[self.cabezal]== '1':
            #---------------Movimiento en cinta metrica---------------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = 'Y'
            #---------------Fin movimiento en cinta metrica-----------------------
            self.retorno = 'Y'
            separado = codigoVar.split('-')
            self.v1 = self.variables(separado[0])
            self.v2 = self.variables(separado[1])
            self.recorrerIzqDer()
            print(self.programa)
        

    
    def recorrerIzqDer(self):
        cont = 0
        while cont != 2:
            self.BuscarVariable(self.v1,cont)
            self.moverDerecha(self.v2,cont)
            cont = cont + 1 
            
        self.retornarPrograma()
            
    def retornarPrograma(self):
        
         while self.programa[self.cabezal]!= self.retorno:             
            #---------------Movimiento en cinta metrica-----------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-------------------
            self.cabezal = self.cabezal + 1
            
         if self.programa[self.cabezal] == 'X':
            #---------------Movimiento en cinta metrica-----------------------            
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = '0'
            #---------------Fin movimiento en cinta metrica-------------------   
            
         elif self.programa[self.cabezal] == 'Y':            
            #---------------Movimiento en cinta metrica-----------------------            
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = '1'
            #---------------Fin movimiento en cinta metrica-------------------
        
        
        
    # BUSCA LA VARIABLE A LA IZQUIERDA 
    def BuscarVariable(self,v,c):
        print('entro a buscar a la izquierda')

        
       
        # CONDICION PARA MOVERSE HACIA ATRAS EN BUSCA DE LA VARIABLE
        while self.programa[self.cabezal] != v:
            
            self.cabezal = self.cabezal -1
            
            #---------------Movimiento en cinta metrica-----------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASsssssssssssssO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-------------------
            
            
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------
        
        
        
        
        # CONDICIONAL PARA CAMBIAR LAS VARIABLES CUANDO SE MUEVA A LA IZQUIERDA  
        if self.programa[self.cabezal]== 'X':
            self.programa[self.cabezal] = '0'            
        elif self.programa[self.cabezal]== 'Y':
            self.programa[self.cabezal] = '1'
        
        # CABEZAL            
        self.cabezal = self.cabezal + 1
                       
        if self.programa[self.cabezal] == '0':
            #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO111111111:", str(self.programa))
            self.programa[self.cabezal] = 'X'
            #---------------Fin movimiento en cinta metrica-----------------------
            self.v1 = 'X'
            
        elif self.programa[self.cabezal] == '1':
            #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO111111111:", str(self.programa))
            self.programa[self.cabezal] = 'Y'
            #---------------Fin movimiento en cinta metrica-----------------------
            self.v1 = 'Y'

        
        # CONDICIONAL PARA CAMBIAR LAS VARIABLES CUANDO SE MUEVA A LA DERECHA
        if c == 1:
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'
    
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'
                
        elif c == 0:
            # CABEZAL
            self.cabezal = self.cabezal + 1
           
        print('salio de buscar a la izquierda')
            

# BUSCA LA VARIABLE A LA DERECHA           
    def moverDerecha(self,v,c):
        


    # CICLO PARA RECORRE LA CINTA EN BUSCA DE UNA Z HACIA LA DERECHA Y CREA EL AUTOMATA
        while self.programa[self.cabezal] != v:           
            
            #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-----------------------
            
            self.cabezal = self.cabezal + 1 
            
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica----------------------- 
        
        # CONDICIONAL PARA CAMBIAR LAS VARIABLES CUANDO SE MUEVA A LA IZQUIERDA  
        if self.programa[self.cabezal]== 'X':
            self.programa[self.cabezal] = '0'            
        elif self.programa[self.cabezal]== 'Y':
            self.programa[self.cabezal] = '1'
        
        
        self.cabezal = self.cabezal + 1
        
       
            
        #---------------Movimiento en cinta metrica---------------------------
        self.programa[self.cabezal] = '▄'            
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = self.v1
        #---------------Fin movimiento en cinta metrica-----------------------
        self.v2 = self.v1
            
        
            
            
            
        if c == 1:
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'
                self.cabezal = self.cabezal - 1
                
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'               
                self.cabezal = self.cabezal - 1
        elif c == 0:            
            self.cabezal = self.cabezal - 1
           
            
            
        

    
    
    
        
        
    def variables(self, op):
            return{
                '00': self.V1A(op),
                '01': self.V2B(op),
                '10': self.V3C(op),
                '11': self.V4T(),
            }.get(op)  
        
    def V1A(self,op):   
        return 'A'
    
    def V2B(self,op):  
        return 'B'
    
    def V3C(self,op):
        return 'C'
    
    def V4T(self):
        return 'T'

    
        
        
        
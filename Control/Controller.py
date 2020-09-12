# -*- coding: utf-8 -*-
import tkinter.messagebox

class Controller:
    
    def __init__(self, cadena):
        self. programa = list(cadena)
        self. automata = []
        self.cont = 0
        self.cabezal = 0
        self.accionar()
        
    def accionar(self):
        tkinter.messagebox.showinfo("PASO A PASO:", 'INICIO DE CINTA: \n\n' + str(self.programa))
        self.buscarZ()
        print(self.automata)
        
        
        
    def buscarZ(self):        
    #VARIABLES
        estados = ''
        estadosS = ''
        estadosT = []
        auxiliar = ''
        
    # CICLO PARA RECORRE LA CINTA EN BUSCA DE UNA Z HACIA LA DERECHA Y CREA EL AUTOMATA
        while self.programa[self.cabezal] != 'Z':  
            
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            
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
                
        # CABEZAL - (APUNTADOR)
            self.cabezal = self.cabezal + 1        
        
    # INCERTA LOS ESTADOS Y LA ACCION
        self.automata.append([self.cont,estadosS,self.cont])  
        self.cont = 1
        
    # SIGIENTE ESTADO CUANDO ENCUENTRE UNA Z
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        
        estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|' 
        self.automata.append([self.cont-1,estados,self.cont])
        
        
        #tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        

        
        
        
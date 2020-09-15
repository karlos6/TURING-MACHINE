# -*- coding: utf-8 -*-
import tkinter.messagebox


class SumarVar:
    # INIT DEL OBJETO
    def __init__(self, cadena,cabezal,v1,v2):
        self.programa = list(cadena)
        self.cont = 0
        self.ascii = chr(65)
        self.automata = []
        self.cabezal = cabezal
        self.v1 = v1
        self.v2 = v2
        self.aux = ''
        self.activador()
        
    def activador(self):
        self.ejecucionPrograma()
        
        
    def ejecucionPrograma(self):
        
        cont1 = 0
        while cont1 != 2:
            self.izquierda(cont1)
            self.derecha(cont1)            
            cont1 = cont1 +1
        
        
    def izquierda(self, c):
        while self.programa[self.cabezal] != self.v1:
            
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
            print(c,'entro al condicional recorrer izquierda')
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'
                self.aux = 'X'
                print(self.aux)
    
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'
                self.aux = 'Y'
                print(self.aux)
                
        elif c == 0:
            print('entro al condicional 0 de la izquierda')
            self.cabezal = self.cabezal + 1 
            self.aux = self.programa[self.cabezal]
            print(self.aux)


        
    def derecha(self, c):
        
        while self.programa[self.cabezal] != self.v2:           
            
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
        
       
            
        
            
        
            
            
            
        if c == 1:
            
            if self.programa[self.cabezal]== '0':                
                self.cabezal = self.cabezal - 1
                
                if self.aux == 'X':
                    #---------------Movimiento en cinta metrica---------------------------
                    self.programa[self.cabezal] = '▄'            
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = '0'
                    #---------------Fin movimiento en cinta metrica-----------------------
                
                elif self.aux == 'Y':                    
                    #---------------Movimiento en cinta metrica---------------------------
                    self.programa[self.cabezal] = '▄'            
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = '1'
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                
            elif self.programa[self.cabezal]== '1':
                
                self.cabezal = self.cabezal - 1
                
                if self.aux == 'X':                    
                    #---------------Movimiento en cinta metrica---------------------------
                    self.programa[self.cabezal] = '▄'            
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = '1'
                    #---------------Fin movimiento en cinta metrica-----------------------
                
                elif self.aux == 'Y':                    
                    #---------------Movimiento en cinta metrica---------------------------
                    self.programa[self.cabezal] = '▄'            
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = '0'
                    #---------------Fin movimiento en cinta metrica-----------------------
                
        elif c == 0: 
            
            if self.programa[self.cabezal]== '0':
                    
                #---------------Movimiento en cinta metrica---------------------------
                self.programa[self.cabezal] = '▄'            
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'X'
                #---------------Fin movimiento en cinta metrica-----------------------
                self.v2 = 'X'
                
                self.cabezal = self.cabezal + 1
                
                if self.programa[self.cabezal] == '0' and self.aux == '0':
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                    self.cabezal = self.cabezal - 1
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                elif self.programa[self.cabezal] == '0' and self.aux == '1':
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = '1'
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                    self.cabezal = self.cabezal - 1
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                elif self.programa[self.cabezal] == '1' and self.aux == '0':
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                    self.cabezal = self.cabezal - 1
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                elif self.programa[self.cabezal] == '1' and self.aux == '1':
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = '0'
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                    self.cabezal = self.cabezal - 1
                    
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = 'Y'
                    #---------------Fin movimiento en cinta metrica-----------------------
                    self.v2 = 'Y'     
                
                self.cabezal = self.cabezal - 1
                
                
            elif self.programa[self.cabezal]== '1':
                
                
                #---------------Movimiento en cinta metrica---------------------------
                self.programa[self.cabezal] = '▄'            
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'Y'
                #---------------Fin movimiento en cinta metrica-----------------------
                self.v2 = 'Y'
                
                self.cabezal = self.cabezal + 1
                
                if self.programa[self.cabezal] == '0' and self.aux == '0':
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                    self.cabezal = self.cabezal - 1
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                elif self.programa[self.cabezal] == '0' and self.aux == '1':
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = '1'
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                    self.cabezal = self.cabezal - 1
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                elif self.programa[self.cabezal] == '1' and self.aux == '0':
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                    self.cabezal = self.cabezal - 1
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = auxiliar
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                elif self.programa[self.cabezal] == '1' and self.aux == '1':
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = '0'
                    #---------------Fin movimiento en cinta metrica-----------------------
                    
                    self.cabezal = self.cabezal - 1                   
                    
                    #---------------Movimiento en cinta metrica---------------------------
                    auxiliar = self.programa[self.cabezal]
                    self.programa[self.cabezal] = '▄'
                    tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                    self.programa[self.cabezal] = 'Y'
                    #---------------Fin movimiento en cinta metrica-----------------------
                    self.v2 = 'Y'
                    
                self.cabezal = self.cabezal - 1
                
                
    
        
    

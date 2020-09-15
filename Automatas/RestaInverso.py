# -*- coding: utf-8 -*-

import tkinter.messagebox

class RestaInverso:
    
        # INIT DEL OBJETO
    def __init__(self, cadena,cabezal):
        self.programa = list(cadena)
        self.cont = 0
        self.ascii = chr(65)
        self.automata = []
        self.cabezal = cabezal
        self.v1 = 'T'
        self.activador()
        
    def activador(self):
        self.cabezal = self.cabezal + 1
        self.ejecucionPrograma()
        print(self.programa)
        
        
        
    def ejecucionPrograma(self):
        
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------


        if self.programa[self.cabezal] == '1':   
            
            
            self.cabezal = self.cabezal - 1
            
            if self.programa[self.cabezal] == '1':
                #---------------Movimiento en cinta metrica---------------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = '0'
                #---------------Fin movimiento en cinta metrica-----------------------
                
            elif self.programa[self.cabezal] == '0':
                #---------------Movimiento en cinta metrica---------------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = '1'
                #---------------Fin movimiento en cinta metrica-----------------------



# -*- coding: utf-8 -*-
import tkinter.messagebox
from Automatas.AsignarValor import AsignarValor
from Automatas.BuscarZeta import BuscarZeta



class Control:
    
    def __init__(self, cadena):
        self. programa = list(cadena)
        self. automata = []
        self.cont = 0
        self.cabezal = 0        
        #AsignarValor1 = AsignarValor()
        self.accionar()
        
        
#-----------------------------ACCIONAR PROCESOS-------------------------------      
    def accionar(self):        
        tkinter.messagebox.showinfo("PASO A PASO:", 'INICIO DE CINTA: \n\n' + str(self.programa))
        self.automataBuscarZ = BuscarZeta(self.programa)
        self.cabezal = self.automataBuscarZ.cabezal
        self.codigosInstruccion()
        
    def codigosInstruccion(self):
        codigo = ''
        contador = 0
        aux = self.cont
        while contador != 3:
            self.cabezal = self.cabezal + 1            
            #---------------Movimiento en cinta metrica-----------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica--------------------            
            codigo = codigo + self.programa[self.cabezal]  
            contador = contador + 1
        self.switch(codigo)        
        
        

        
    def switch(self, op):
            if op == '000': self.asignarValor(op)
            elif op == '001': self.asignarVariables()
            elif op == '010': self.desplazar()
            elif op == '011': self.sumar()
            elif op == '100': self.restar()
            elif op == '101': self.inicioRepetir()
            elif op == '110': self.finRepetir()
            elif op == '111': self.finPrograma()
            else: print('esta jodido')
        
    def asignarValor(self,op):
        self.automataAsignarValor = AsignarValor(self.programa,op,self.cabezal)
        
        
        


        

# -*- coding: utf-8 -*-
import tkinter.messagebox
from Automatas.SumaIgualarT import SumaIgualarT
from Automatas.SumarVar import SumarVar

class Suma:
    
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
        self.inicioAutomatas(ejecucion)
        self.sacarVariables()
        
    # INICIA EL AUTOMATA
    def inicioAutomatas(self,ejecucion):
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
            self.sumIgual = SumaIgualarT(self.programa,self.cabezal,self.v1)
            self.programa = self.sumIgual.programa
            self.cabezal = self.sumIgual.cabezal
            self.sumvar = SumarVar(self.programa,self.cabezal,self.v2,'T')
            
            print('oooooooooooooooooooooooooooooo')
            print(self.sumvar.programa)
            print('oooooooooooooooooooooooooooooo')
            
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
            self.sumIgual = SumaIgualarT(self.programa,self.cabezal,self.v1)
            self.programa = self.sumIgual.programa
            self.cabezal = self.sumIgual.cabezal
            self.sumvar = SumarVar(self.programa,self.cabezal,self.v2,'T')
            
            
            print('oooooooooooooooooooooooooooooo')           
            print(self.sumvar.programa)
            print('oooooooooooooooooooooooooooooo')

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



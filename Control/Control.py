# -*- coding: utf-8 -*-
import tkinter.messagebox
from Automatas.AsignarValor import AsignarValor
from Automatas.BuscarZeta import BuscarZeta
from Automatas.DesplazarIzqDra import DesplazarIzqDra
from Automatas.AsignarVariables import AsignarVariables
from Automatas.Suma import Suma
from Automatas.Resta import Resta

from Grafica.Graph import Graph


class Control:
    
    def __init__(self, cadena):
        self. programa = list(cadena)
        self. automata = []
        self.cont = 0
        self.cabezal = 0     
        self.bandera = True
        self.accionar()
        
        
#-----------------------------ACCIONAR PROCESOS-------------------------------      
    def accionar(self):        
        tkinter.messagebox.showinfo("PASO A PASO:", 'INICIO DE CINTA: \n\n' + str(self.programa))
        self.automataBuscarZ = BuscarZeta(self.programa)
        self.cabezal = self.automataBuscarZ.cabezal
        self.automata.append(self.automataBuscarZ.automata)
        self.codigosInstruccion()
        #print('--------------------------------------------------------------')
        #print('Buscar Zeta')
        #print(self.automata)
        #print('--------------------------------------------------------------')
#-------SACA LOS CODIGOS PARA EJECUTAR LA ACCION DEL PROGRAMA-----------------
    def codigosInstruccion(self):
        codigo = ''
        contador = 0
        aux = self.cont
        
        if self.bandera == True:            
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
                print(codigo)
            self.switch(codigo)
            
    def switch(self, op):
            if op == '000': self.asignarValor(op)
            elif op == '001': self.asignarVariables(op)
            elif op == '010': self.desplazar(op)
            elif op == '011': self.sumar(op)
            elif op == '100': self.restar(op)
            elif op == '101': self.inicioRepetir()
            elif op == '110': self.finRepetir()
            elif op == '111': self.finPrograma()
            else: print('esta jodido')            
        
    def asignarValor(self,op):
        self.automataAsignarValor = AsignarValor(self.programa,op,self.cabezal)
        self.programa = self.automataAsignarValor.programa
        self.cabezal = self.automataAsignarValor.cabezal+2
        self.enlazarAutomatas(self.automataAsignarValor.automata)

        
        self.codigosInstruccion()        
        
    def desplazar(self, op):
        self.automataDesplazar = DesplazarIzqDra(self.programa,op,self.cabezal)  
        self.programa = self.automataDesplazar.programa
        self.cabezal = self.automataDesplazar.cabezal
        self.codigosInstruccion()
        
    def asignarVariables(self, op):
        self.automataAsignarVariable = AsignarVariables(self.programa,op,self.cabezal)
        self.programa = self.automataAsignarVariable.programa
        self.cabezal = self.automataAsignarVariable.cabezal
        self.codigosInstruccion()
        
    def sumar(self, op):
        self.automataSuma = Suma(self.programa,op,self.cabezal)
        self.programa = self.automataSuma.programa
        self.cabezal = self.automataSuma.cabezal
        self.codigosInstruccion()        
        
    def restar(self, op):
        self.automataResta = Resta(self.programa,op,self.cabezal)
        self.programa = self.automataResta.programa
        self.cabezal = self.automataResta.cabezal
        self.codigosInstruccion()
        
    def finPrograma(self):
        self.bandera = False
        tkinter.messagebox.showinfo("FIN DEL PROGRAMA:", str(self.programa))
        
    def enlazarAutomatas(self,automa):
        aux1 = self.automata[len(self.automata)-1]
        aux1 = aux1[len(aux1)-1]
        aux1 = aux1[len(aux1)-1]
        automa[0][0][0] = aux1
<<<<<<< HEAD
        self.automata.append(automa)
        print(self.automata)
        self.grafico = Graph('AUTOMATA')
        self.grafico.Conexiones(self.automata)
=======
        
        for i in automa:
            self.automata.append(i)       
        print('Automata de asignar valor')
        print(self.automata)
>>>>>>> c1c9b9beb0f0253969ab9dea1d70e22634294a06
        
        
        
        
        
        


        

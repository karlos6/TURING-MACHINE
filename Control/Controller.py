# -*- coding: utf-8 -*-
import tkinter.messagebox
#from automatas.AsignarValor import AsignarValor

class Controller:
    
    def __init__(self, cadena):
        self. programa = list(cadena)
        self. automata = []
        self.cont = 0
        self.cabezal = 0
        #AsignarValor1 = AsignarValor()
        self.accionar()
        
#-----------------------------ACCIONAR PROCESOS-------------------------------      
    def accionar(self):
        
        print(self.programa)
        tkinter.messagebox.showinfo("PASO A PASO:", 'INICIO DE CINTA: \n\n' + str(self.programa))
        self.buscarZ()
        self.codigosInstruccion()
        print(self.automata)       
        
#-------RECORRIDO INICIO EN BUSCA DE LA Z PARA INICIAR PROGRAMA--------------- 
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
            #tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
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

#-----------------------SACA LOS CODIGOS PARA EJECUTAR------------------------        
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
            self.cont = self.cont + 1
            self.automata.append([aux,self.programa[self.cabezal],self.cont])
            aux = aux + 1    
        print(codigo)
        self.switch(codigo)
    
#--------------------------ACCIONES DE CODIGO---------------------------------
    def switch(self, op):
            if op == '000': self.asignarValor()
            elif op == '001': self.asignarVariables()
            elif op == '010': self.desplazar()
            elif op == '011': self.sumar()
            elif op == '100': self.restar()
            elif op == '101': self.inicioRepetir()
            elif op == '110': self.finRepetir()
            elif op == '111': self.finPrograma()
            else: print('esta jodido')
            
#-----------------------------------------------------------------------------
#                               ASIGNAR VALOR    
#-----------------------------------------------------------------------------
# 2 BITS PARA IDENTIFICAR LA VARIABLE Y 4 PARA EL VALOR A ASIGNAR.
    def asignarValor(self):        
        codigo = ''
        esta = 0
        aux = self.cont
        variable = ''
        apuntador = 0
        while esta != 2:
            self.cabezal = self.cabezal + 1
            
            #---------------Movimiento en cinta metrica-----------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-------------------
            
            
            codigo = codigo + self.programa[self.cabezal]
            esta = esta + 1
            self.cont = self.cont + 1
            self.automata.append([aux,self.programa[self.cabezal],self.cont])
            aux = aux + 1   
            print('que pasa guarro')
            print(esta)
        variable = self.switchVariables(codigo)
        
        conta = 0
        suma = 1
        bandera = True
        while conta != 2:    
            
            self.cabezal = self.cabezal + 1
            self.cont = self.cont + 1
            self.automata.append([aux,self.programa[self.cabezal],self.cont])
            dig = self.programa[self.cabezal]
            aux = aux + 1           
            print(variable)     
            apuntaMx = self.cabezal
            apuntaMm = self.cabezal
            self.moverAtras(variable)
            print('despues de moverAtras')
            if bandera == False:
                self.cabezal= self.cabezal + 1

            if dig == 1:
                #---------------Movimiento en cinta metrica-----------------------
                auxiliar = self.programa[self.cabezal]
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = dig
                #---------------Fin movimiento en cinta metrica-------------------
            else:
                
                #---------------Movimiento en cinta metrica-----------------------
                auxiliar = self.programa[self.cabezal]
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = dig
                #---------------Fin movimiento en cinta metrica-------------------
            
        
            
            while self.cabezal != apuntaMx:                
                #---------------Movimiento en cinta metrica-----------------------
                auxiliar = self.programa[self.cabezal]
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = auxiliar
                #---------------Fin movimiento en cinta metrica-------------------
                self.cabezal = self.cabezal + 1
                
            
            
            if bandera :
                bandera = False 
                
            
            
            
            
        
        
#---- MOVER HACIA ATRAS -------------------------------------------------------
    def moverAtras(self, variable):
        
        estados = ''
        estadosS = ''
        estadosT = []
        
        print('entro moverAtras')        
        while self.programa[self.cabezal] != variable:
            
            #---------------Movimiento en cinta metrica-----------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-------------------
                
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
                
            self.cabezal = self.cabezal - 1
            
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------
        
        # INCERTA LOS ESTADOS Y LA ACCION
        self.automata.append([self.cont,estadosS,self.cont])
        self.cont = self.cont + 1 
        self.automata.append([self.cont-1,variable+'|'+variable+'|R',self.cont])
        
        print('se sale de moverAtras')
        self.cabezal = self.cabezal + 1

            
        
#------------------------------------------------------------------------------
#                     SWITCH IDENTIFICADOR DE VARIABLES
#------------------------------------------------------------------------------        
# SWITCH PARA IDETIFICAR LA VARIABLE A CAMBIAR EN LA CINTA        
    def switchVariables(self, op):
            return{
                '00': self.V1A(),
                '01': self.V2B(),
                '10': self.V3C(),
                '11': self.V4T(),
            }.get(op)        
    def V1A(self):
        return 'A'
    def V2B(self):
        return 'B'
    def V3C(self):
        return 'C'
    def V4T(self):
        return 'T'
        

        
        
        
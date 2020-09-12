# -*- coding: utf-8 -*-

class Controlador:
    def __init__(self, cadena):
        self.programa = list(cadena)
        self. automata = []
        self.cont = 0
        self.cabezal = 0
        self.accionar()
        
    def accionar(self):
        self.recorridoInicio()
        #self.instruccion()
        #print(self.automata)

#------------------------------------------------------------------------------
#                            RECORRIDO INICIO   
#------------------------------------------------------------------------------
# PRIMER RECORRIDO HACIA LA DERECHA HASTA ENCONTRAR UNA Z PARA INICIAR EL PROGRAMA (CON AUTOMATA)
    def recorridoInicio(self):
    #VARIABLES
        estados = ''
        estadosS = ''
        estadosT = []
        
    # CICLO PARA RECORRE LA CINTA EN BUSCA DE UNA Z HACIA LA DERECHA Y CREA EL AUTOMATA
        while self.programa[self.cabezal] != 'Z':            
            
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
        estados = self.programa[self.cabezal]+','+self.programa[self.cabezal]+',R|' 
        self.automata.append([self.cont-1,estados,self.cont])

#------------------------------------------------------------------------------
#                           IDENTIFICAR INSTRUCCION
#------------------------------------------------------------------------------            
    def instruccion(self):
        codigo = ''
        contador = 0
        aux = self.cont
        while contador != 3:
            self.cabezal = self.cabezal + 1
            codigo = codigo + self.programa[self.cabezal]
            contador = contador + 1
            self.cont = self.cont + 1
            self.automata.append([aux,self.programa[self.cabezal],self.cont])
            aux = aux + 1    
        print(codigo)
        self.switch(codigo)
            



#------------------------------------------------------------------------------
#                        SWITCH INSTRUCCION A REALIZAR
#------------------------------------------------------------------------------ 
# CONDICIONAL PARA EFECTUAR LA ACCION SEGUN LA CINTA
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
        contador = 0
        aux = self.cont
        variable = ''
        apuntador = 0
        while contador != 2:
            self.cabezal = self.cabezal + 1
            codigo = codigo + self.programa[self.cabezal]
            contador = contador + 1
            self.cont = self.cont + 1
            self.automata.append([aux,self.programa[self.cabezal],self.cont])
            aux = aux + 1            
        variable = self.switchVariables(codigo)
        
                
        contador = 1
        apuntador = self.cabezal
        total = ''
        vGuardar = ''
        while contador != 5:
            
            self.cabezal = self.cabezal+contador            
            vGuardar = self.programa[self.cabezal]
            total = total + vGuardar
            
            estados = ''
            estadosS = ''
            estadosT = []            
            
            while self.programa[self.cabezal] != variable:
                
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
            self.cabezal = self.cabezal+contador            
            self.programa[self.cabezal] = vGuardar
            
            while self.cabezal != apuntador :
                self.cabezal = self.cabezal + 1
            contador = contador + 1
            
        # INCERTA LOS ESTADOS Y LA ACCION
        self.automata.append([self.cont,estadosS,self.cont])  
        self.cont = self.cont + 1
        
        estados = variable+','+variable+',R|' 
        self.automata.append([self.cont-1,estados,self.cont])
        
        contador = 0
        while contador != 4:
            aux = aux +1 
            self.cont = self. cont +1
            self.automata.append([aux,total[contador] ,self.cont])
            contador = contador + 1       
        print(self.programa)
            
            
            
            
#-----------------------------------------------------------------------------
#                            ASIGNAR VARIABLES
#-----------------------------------------------------------------------------
# 2 BITS PRIMERA VAR 2 BITS SEGUNDA VAR. PRIMERA=SEGUNDA
    def asignarVariables(self):
        print('todo bello')
        
#-----------------------------------------------------------------------------
#                               DESPLAZAR
#-----------------------------------------------------------------------------   
# 2 BITS IDENTIFICA VAR. UN BIT SI ES 0 DESPL IZQ 1 DESPL DER
    def desplazar(self):
        print('sisas')
        
#-----------------------------------------------------------------------------
#                                  SUMAR 
#----------------------------------------------------------------------------- 
# 2 BITS PRIMERA VAR 2 BITS SEGUNDA VAR. T=PRIMERA+SEGUNDA
    def sumar(self):
        print('nonas')
        
    def restar (self):
        return "February"
    
    def inicioRepetir(self):
        return "February"
    
    def finRepetir(self):
        return "February"
    
    def finPrograma(self):
        return "February"




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
        
        
        
        
        
        
import tkinter.messagebox
from Automatas.MoverVariables import MoverVariables

class AsignarVariables:
    
    def __init__(self, cadena,ejecucion,cabezal):
        self.programa = list(cadena)
        self.automata = []
        self.cont = 0
        self.ascii = chr(65)
        self.cabezal = cabezal
        self.activador(ejecucion)
    
    def activador(self,ejecucion):
        self.inicioAutomata(ejecucion)
        self.sacarVariable()
    
    def inicioAutomata(self,ejecucion):
        listaP = []
        for i in ejecucion:
            self.cont = self.cont + 1
            listaP.append([self.ascii+str(self.cont-1),i+','+i+',R',self.ascii+str(self.cont)])
        self.automata.append(listaP)
        
        
    def sacarVariable(self):
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
            esta = esta + 1
            
        
        variable1 = self.variables(codigoVar[0]+codigoVar[1])
        variable2 = self.variables(codigoVar[2]+codigoVar[3])
        self.MoverVariables = MoverVariables(self.programa, self.cabezal, variable1,variable2)
        
        #print(self.automata)
        #print(variable1)
        #print(variable2)
        #print(codigoVar)
        
    def variables(self, op):
            return{
                '00': self.V1A(op),
                '01': self.V2B(op),
                '10': self.V3C(op),
                '11': self.V4T(),
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
    
    def V4T(self):
        return 'T'
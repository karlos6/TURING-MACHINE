import tkinter.messagebox

class MoverVariables:
    
    # INICIALIZADOR print(self.programa[self.cabezal])
    def __init__(self, cadena,cabezal,variable1,variable2):
        self.programa = list(cadena)
        self.variable1 = variable1
        self.variable2= variable2
        self.v1 = self.variable1
        self.v2 = self.variable2
        self.cont = 0
        self.ascii = chr(70)
        self.automata = []
        self.cabezal = cabezal
        self.Activador()
        
    def Activador(self):
        conta = 0
        self.BuscarVariable(self.v1,0) 
        
        conta = 1
        while conta != 4:
            
            #print(self.cabezal)
            self.cabezal = self.cabezal + 1
            self.cont = self.cont + 1 
             
            print("conta ",conta," valor ",self.programa[self.cabezal]," cabeza ",self.cabezal)
            if self.programa[self.cabezal] == '0':
                #---------------Movimiento en cinta metrica--------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'X'
                #---------------Fin movimiento en cinta metrica----------------
                
                if self.variable1 == 'A' and self.variable2 == 'C':
                    #print("contar ",conta)
                    self.moverDerecha(self.v2,conta)                    
                    self.BuscarVariable('X',conta)
                    self.v2 = 'X'
                    
                elif self.variable1 == 'A' and self.variable2 == 'B':
                    #print("contar ",conta)
                    self.moverDerecha(self.v2,conta)                    
                    self.BuscarVariable('X',conta)
                    self.v2 = 'X'
                    
                elif self.variable1 == 'C' and self.variable2 == 'A':
                    #print("contar ",conta)
                    self.BuscarVariable(self.v2,conta)             
                    self.v2 = 'X'
                    self.moverDerecha(self.v2,conta) 
                    
                    
                elif self.variable1 == 'C' and self.variable2 == 'B':
                    self.BuscarVariable(self.variable1)
                    
                elif self.variable1 == 'B' and self.variable2 == 'A':
                    self.BuscarVariable(self.variable1)
                    
                elif self.variable1 == 'B' and self.variable2 == 'D':
                    self.moverDerecha(self.variable2)
                            
            elif self.programa[self.cabezal] == '1':
                #---------------Movimiento en cinta metrica--------------------
                self.programa[self.cabezal] = '▄'
                tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
                self.programa[self.cabezal] = 'Y'
                #---------------Fin movimiento en cinta metrica--------------- 
            
            conta = conta + 1

    
     # BUSCA LA VARIABLE A LA IZQUIERDA 
    def BuscarVariable(self,v,c): 
        estados = ''
        estadosS = ''
        estadosT = []
        self.cabezal = self.cabezal -1
       
        # CONDICION PARA MOVERSE HACIA ATRAS EN BUSCA DE LA VARIABLE
        while self.programa[self.cabezal] != v:
            
            #---------------Movimiento en cinta metrica-----------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
            #---------------Fin movimiento en cinta metrica-------------------
            
            # CONDICIONES PARA CREAR EL AUTOMATA                
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
            
            # CABEZAL
            self.cabezal = self.cabezal - 1
        
            
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------
        
        # INCERTA LOS ESTADOS Y LA ACCION
        self.automata.append([self.ascii+str(self.cont),estadosS,self.ascii+str(self.cont)])
        self.cont = self.cont + 1 
        self.automata.append([self.ascii+str(self.cont-1),self.variable1+'|'+self.variable1+'|R',self.ascii+str(self.cont)])
        

        
        # CONDICIONAL PARA CAMBIAR LAS VARIABLES CUANDO SE MUEVA A LA DERECHA
        if c == 1:
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'
                
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'
        
            #self.cabezal = self.cabezal-1     
            
        if c == 2:
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'
                
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'
            
            self.cabezal = self.cabezal-1 

        
        
    # BUSCA LA VARIABLE A LA DERECHA           
    def moverDerecha(self,va,c):
        
        # CABEZAL
        self.cabezal = self.cabezal + 1
        
        #VARIABLES
        estados = ''
        estadosS = ''
        estadosT = []
        auxiliar = ''
        
        #print(va)

    # CICLO PARA RECORRE LA CINTA EN BUSCA DE UNA Z HACIA LA DERECHA Y CREA EL AUTOMATA
        while self.programa[self.cabezal] != va:           
            
        #---------------Movimiento en cinta metrica---------------------------
            auxiliar = self.programa[self.cabezal]
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------

        # CONDICIONALES PARA EVALUAR LOS NODOS Y MOVERSE A LA DERECHA EN BUSCA DE UNA Z
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
            self.cabezal = self.cabezal + 1          
        
            
    # INCERTA LOS ESTADOS Y LA ACCION
        self.automata.append([self.ascii+str(self.cont),estadosS,self.ascii+str(self.cont)])
        self.cont = 1
        self.automata.append([self.ascii+str(self.cont-1),self.v2+'|'+self.v2+'|R',self.ascii+str(self.cont)])
        
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica-----------------------   
        
        if c == 1:
            print("entro")
            self.cabezal = self.cabezal+1
            #---------------Movimiento en cinta metrica--------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = 'X'
            #---------------Fin movimiento en cinta metrica----------------
            self.cabezal = self.cabezal + 1
        
        
        if c == 2:
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'
                
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'
                
        if c == 3:
            if self.programa[self.cabezal]== 'X':
                self.programa[self.cabezal] = '0'
                
            elif self.programa[self.cabezal]== 'Y':
                self.programa[self.cabezal] = '1'
        
        if c == 2 :
            self.cabezal = self.cabezal+1
            #---------------Movimiento en cinta metrica--------------------
            self.programa[self.cabezal] = '▄'
            tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
            self.programa[self.cabezal] = 'X'
            #---------------Fin movimiento en cinta metrica----------------
            self.cabezal = self.cabezal-1
        
        self.cabezal = self.cabezal-1
        
        #---------------Movimiento en cinta metrica---------------------------
        auxiliar = self.programa[self.cabezal]
        self.programa[self.cabezal] = '▄'
        tkinter.messagebox.showinfo("PASO A PASO:", str(self.programa))
        self.programa[self.cabezal] = auxiliar
        #---------------Fin movimiento en cinta metrica----------------------- 

        
        
        
        

            

        
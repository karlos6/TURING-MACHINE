from tkinter import *
import tkinter as tk
from Control.Control import Control

class Windows:     
# Constructor de la ventana   
    def __init__(self):
        self.ventana()         
        
    # Metodo que crea una ventana e inserta un panel de trabajo
    def ventana(self):
        self.view = Tk()     
        self.diseño()        
        self.labelAndInput()
        self.botones()
        self.view.mainloop()

    #Metodo de diseño de la ventana 
    def diseño(self):
        self.view.title("AUTOMATAS Y LENGUAJES FORMALES (TRURING MACHINE)")
        self.view.geometry('500x350+380+180')
        self.panel = Frame(self.view,width=500, height=350).pack()
        
    # Inserta al panel un label y una variable que resive un string
    def labelAndInput(self):               
        self.variable_1 = StringVar()
        label_1 = Label(self.panel,text="PROGRAMA: ").place(x=210, y=44)
        input_1 = Entry(self.panel,textvariable = self.variable_1, width=50).place(x=100, y=70)

    # Botones  
    def botones(self):
        boton1 = Button(self.panel, text="ACEPTAR", width=20,height=2, background="SkyBlue2",
                        command= self.Accionar).place(x=180,y=150)
        
    def Accionar(self):
        programa = 'A00B01C11T00Z'+self.variable_1.get()
        self.controlTotal = Control(programa)

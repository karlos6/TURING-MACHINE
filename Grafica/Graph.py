import graphviz

class Graph:
    
    
    def __init__ (self, nombre):
        self.graph = graphviz.Digraph(nombre,format='pdf')
        self.graph.attr(rankdir='LR', size='8,5')
        
    
    def Conexiones(self, lista):
       
       self.graph.attr('node', shape='circle')
       print("#############################################################")
       for i in lista:
           for j in i:
               print(j)
        #       self.graph.edge(j[0], j[2], label=j[1])
        #for i in lista[1]:
        
       #.graph.view()
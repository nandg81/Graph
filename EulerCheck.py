import warnings
import matplotlib.cbook
import networkx as nx
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

G = nx.Graph()
G.add_nodes_from(['a','b','c','d','e','f','g','h'])
G.add_edges_from([('c','d'),('c','b'),('b','d'),('b','e'),('e','f'),('f','a'),('a','b'),('a','g'),('g','i'),('i','h'),('g','h')])

pos = { 'i': (50, 10), 'h': (70, 10), 'g': (60, 20),'a': (65, 40),'b': (52,52),'f':(75,55),'e':(65,70),'c': (40,70),'d':(50,80)} 


nx.draw_networkx(G, pos=pos,with_labels=True)
plt.savefig('image.png')
plt.show()

if(nx.is_eulerian (G)):
    print("Is Euler")
else:
    print("Not Euler")
    
edges=G.edges()
fout=open("edgedata1.txt","w")
for (v1,v2) in edges:
    fout.write("edge from "+str(v1)+" TO "+str(v2)+"\n")
    ##fout=open("edgedata1.txt","wb")
##nx.write_edgelist(G, fout)
    
fout.close()

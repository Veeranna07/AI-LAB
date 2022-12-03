from collections import deque
class Graph:
    def __init__(self,adj_list):
        self.adj_list=adj_list
    def get_neigh(self,v):
        return self.adj_list[v]
    def heuristic(self,n):
        H={'A':1,'B':1,'C':1,'D':1}
        return H[n]
    def a_star(self,start_node,stop_node):
        openlist=set([start_node])
        closedlist=set([])
        g={}
        g[start_node]=0
        parents={}
        parents[start_node]=start_node
        while len(openlist)>0:
            n=None
            for v in openlist:
                if n==None or g[v]+self.heuristic(v)<g[n]+self.heuristic(n):
                    n=v;
            if n==None:
                print('Path does not exist!!!')
                return None
            if n==stop_node:
                reconstructpath=[]
                while parents[n]!=n:
                    reconstructpath.append(n)
                    n=parents[n]
                reconstructpath.append(start_node)
                reconstructpath.reverse()
                print('Path Found : {}'.format(reconstructpath))
                return reconstructpath
            for(m,weight) in self.get_neigh(n):
                if m not in openlist and m not in closedlist:
                    openlist.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        if m in closedlist:
                            closedlist.remove(m)
                            openlist.add(m)
            openlist.remove(n)
            closedlist.add(n)
        print('Path does not exist!!!')
        return None
adj_list={
    'A':[('B',1),('C',3),('D',7)],
    'B':[('D',5)],
    'C':[('D',12)]
}
graph1=Graph(adj_list)
graph1.a_star('A','D')

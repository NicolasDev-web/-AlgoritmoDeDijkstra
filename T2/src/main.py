import sys

class DirectedEdge:
    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def weight(self):
        return self._weight

    def _from(self):
        return self._v

    def to(self):
        return self._w

    def __str__(self):
        return f"{self._v}->{self._w} {self._weight}"

class EdgeWeightedDigraph:
    def __init__(self, V):
        self._V = V
        self._E = 0
        self._adj = [[] for _ in range(V)]

    def V(self):
        return self._V

    def E(self):
        return self._E

    def add_edge(self, e):
        self._adj[e._from()].append(e)
        self._E += 1

    def adj(self, v):
        return self._adj[v]

    def edges(self):
        bag = []
        for v in range(self._V):
            for e in self._adj[v]:
                bag.append(e)
        return bag

class IndexMinPQ:
    def __init__(self, maxN):
        self.maxN = maxN
        self.n = 0
        self.pq = [0] * (maxN + 1)
        self.qp = [-1] * (maxN + 1)
        self.keys = [None] * (maxN + 1)

    def is_empty(self):
        return self.n == 0

    def contains(self, i):
        return self.qp[i] != -1

    def insert(self, i, key):
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self.swim(self.n)

    def del_min(self):
        min_idx = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        self.qp[min_idx] = -1
        self.keys[min_idx] = None
        self.pq[self.n + 1] = -1
        return min_idx

    def decrease_key(self, i, key):
        self.keys[i] = key
        self.swim(self.qp[i])

    def swim(self, k):
        while k > 1 and self.greater(k // 2, k):
            self.exch(k, k // 2)
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.greater(j, j + 1):
                j += 1
            if not self.greater(k, j):
                break
            self.exch(k, j)
            k = j

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

class DijkstraSP:
    def __init__(self, G, s):
        self._distTo = [10**18] * G.V()
        self._edgeTo = [None] * G.V()
        self._pq = IndexMinPQ(G.V())
        
        self._distTo[s] = 0
        self._pq.insert(s, 0)
        
        while not self._pq.is_empty():
            v = self._pq.del_min()
            for e in G.adj(v):
                self.relax(e)
                
    def relax(self, e):
        v = e._from()
        w = e.to()
        if self._distTo[w] > self._distTo[v] + e.weight():
            self._distTo[w] = self._distTo[v] + e.weight()
            self._edgeTo[w] = e
            if self._pq.contains(w):
                self._pq.decrease_key(w, self._distTo[w])
            else:
                self._pq.insert(w, self._distTo[w])
                
    def distTo(self, v):
        return self._distTo[v]

    def hasPathTo(self, v):
        return self._distTo[v] < 10**18

def solve():
    # Aumentando o limite de recursão por precaução
    sys.setrecursionlimit(200000)
    
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Representação do grafo usando algs4
    G = EdgeWeightedDigraph(n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        G.add_edge(DirectedEdge(u, v, c))
        idx += 3
        
    # Executa o Dijkstra
    sp = DijkstraSP(G, 1)
    
    # Imprime as distâncias da cidade 1 para todas as outras cidades
    dist_results = []
    for i in range(1, n + 1):
        dist_results.append(str(sp.distTo(i)))
        
    print(" ".join(dist_results))

if __name__ == '__main__':
    solve()

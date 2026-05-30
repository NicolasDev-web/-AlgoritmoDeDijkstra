import sys
import heapq

def solve():
    # Aumentando o limite de recursão por precaução
    sys.setrecursionlimit(200000)
    
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Representação do grafo: lista de adjacência
    # adj[u] conterá tuplas (v, peso)
    adj = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        adj[u].append((v, c))
        idx += 3
        
    # Inicialização das distâncias com infinito
    # Usando 10**18 para simular o infinito e evitar problemas de precisão/overflow
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = 0
    
    # Fila de prioridade (Min-Heap) armazenará tuplas (distancia_acumulada, vertice)
    pq = [(0, 1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Otimização crucial: se encontrarmos uma distância maior na fila, descartamos (lazy deletion)
        if d > dist[u]:
            continue
            
        # Relaxamento das arestas
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    # Imprime as distâncias da cidade 1 para todas as outras cidades
    print(" ".join(map(str, dist[1:])))

if __name__ == '__main__':
    solve()

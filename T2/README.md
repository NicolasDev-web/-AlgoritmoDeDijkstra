# Trabalho Prático 2 - Unidade 3: Resolução de Problemas com Grafos

## Grupo A - CSES Shortest Routes I

**Nome do Problema:** Shortest Routes I  
**Link do Problema:** [https://cses.fi/problemset/task/1671](https://cses.fi/problemset/task/1671)  
**Integrantes do Grupo:** [Preencher com os nomes dos alunos]  
**Linguagem Utilizada:** Python 3  

---

## Como Executar a Solução

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Navegue até a pasta raiz deste repositório pelo terminal.
3. Para testar o código com o arquivo de exemplo fornecido, execute o seguinte comando:
   ```bash
   python T2/src/main.py < T2/dados/entradas_do_problema.txt
   ```
4. A saída será impressa no console com as distâncias mínimas separadas por espaço (ex: `0 5 2`).

---

## Explicação da Modelagem do Problema e Representação Adotada

O problema "Shortest Routes I" nos pede para encontrar a menor distância de uma cidade inicial (cidade 1, "Syrjälä") para todas as outras cidades em um mapa com voos conectando cidades.

**Modelagem como Grafo:**
- **Vértices (N):** Representam as cidades, numeradas de 1 a $n$.
- **Arestas (M):** Representam as conexões de voo de uma cidade $u$ para uma cidade $v$. Como os voos são unidirecionais, as arestas são direcionadas.
- **Pesos (C):** Representam o comprimento do voo (ou custo/distância) daquela conexão. O problema garante que os pesos não são negativos (comprimento dos voos).

**Representação Adotada:**
Foi escolhida a **Lista de Adjacência**. Utilizamos um vetor `adj` onde o índice representa a cidade de origem e armazena uma lista de tuplas `(destino, peso)`. 
A lista de adjacência é a melhor escolha porque $N \le 10^5$ e $M \le 2 \cdot 10^5$, o que caracteriza um grafo esparso (uma Matriz de Adjacência causaria estouro de memória, excedendo os limites de complexidade de espaço com $10^{10}$ elementos).

---

## Algoritmo Utilizado

Utilizamos o **Algoritmo de Dijkstra**. O Dijkstra é a escolha ideal e padrão para encontrar o caminho mais curto a partir de uma origem única (Single-Source Shortest Path) em grafos com arestas de peso não-negativo.

A implementação usa uma **Fila de Prioridade Mínima (Min-Heap)** (`heapq` nativo do Python) para sempre processar o vértice com a menor distância acumulada até o momento de forma eficiente. O vetor de distâncias (`dist`) foi inicializado com um valor suficientemente grande (`10**18`) simulando o infinito, de forma a não estourar em virtude do acúmulo de arestas que podem pesar até $10^9$.

---

## Variação de Dijkstra Usada

O problema trata-se de um **Dijkstra Clássico** com múltiplas respostas para todos os vértices partindo da mesma origem (cidade 1). Não requer variações complexas de estado.

Entretanto, para evitar problemas de _Timeout_ (TLE) em casos com muitos relaxamentos, incluímos uma técnica de **lazy deletion** (exclusão preguiçosa) ao retirar um nó da fila:
```python
if d > dist[u]:
    continue
```
Esta linha assegura que distâncias desatualizadas (que foram empurradas para a fila antes de encontrarmos um caminho ainda mais curto para `u`) sejam ignoradas, evitando processar os vizinhos de um vértice múltiplas vezes e economizando recursos computacionais.

---

## Análise de Complexidade

- **Tempo:** $O((V + E) \log V)$, onde $V$ é o número de vértices (cidades) e $E$ é o número de arestas (voos).
  - A extração do mínimo (`heappop`) é feita na pior das hipóteses $O(E)$ vezes, já que podemos empurrar múltiplos caminhos para o mesmo vértice. Cada extração custa $O(\log V)$.
  - O loop de relaxamento verifica os vizinhos no máximo para todas as arestas, e as inserções na heap (`heappush`) ocorrem ao relaxar uma aresta com custo $O(\log V)$.
  - Com a exclusão preguiçosa (_lazy deletion_), garantimos que os laços secundários não reavaliem os mesmos vértices com caminhos piores.
- **Espaço:** $O(V + E)$
  - Lista de adjacência domina o uso da memória: $O(V + E)$.
  - Vetor de distâncias: $O(V)$.
  - Fila de Prioridade: $O(E)$ no pior caso.
  - É perfeitamente viável para $M \le 2 \cdot 10^5$.

---

## Evidência de Accepted

*Atenção: O grupo deve submeter a solução em [https://cses.fi/](https://cses.fi/), tirar um printscreen do status "Accepted" (Aceito) na plataforma e salvar o arquivo como `accepted.png` dentro da pasta `T2/evidencias/`.*

![Accepted](evidencias/accepted.png)

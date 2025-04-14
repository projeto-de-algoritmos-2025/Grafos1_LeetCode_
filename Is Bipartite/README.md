# [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/description/)

Existe um grafo não direcionado com `n` nós, onde cada nó é numerado entre `0` e `n - 1`. Você recebe um array 2D `graph`, onde `graph[u]` é um array de nós ao qual o nó `u` é adjacente. Mais formalmente, para cada nó `v` em `graph[u]`, há uma aresta não direcionada entre o nó `u` e o nó `v`. O grafo tem as seguintes propriedades:

- Não há arestas próprias (`graph[u]` não contém `u` ).
- Não há arestas paralelas (`graph[u]` não contém valores duplicados).
- Se `v` estiver em `graph[u]`, então `u` estará em `graph[v]` (o grafo não é direcionado).
- O grafo pode não estar conectado, o que significa que pode haver dois nós `u` e `v` não haver caminho entre eles.
- Um grafo é bipartido se os nós podem ser particionados em dois conjuntos independentes `A` e `B` de forma que cada aresta no grafo conecta um nó no conjunto `A` e um nó no conjunto `B`.

Retorna `true` se e somente se for bipartido .

## Screenshots

### Caso 1

![Case1](/Is%20Bipartite/assets/img/caso1.png)

### Caso 2

![Case2](/Is%20Bipartite/assets/img/caso2.png)

### Caso 3

![Case3](/Is%20Bipartite/assets/img/caso3.png)

### Submissão

![Submission](/Is%20Bipartite/assets/img/submissao.png)

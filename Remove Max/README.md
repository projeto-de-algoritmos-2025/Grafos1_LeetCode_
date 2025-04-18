# [Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/)

Alice e Bob possuem um grafo **não direcionado** com `n` nós e três tipos de arestas:

- **Tipo 1**: Pode ser percorrida **apenas por Alice**.  
- **Tipo 2**: Pode ser percorrida **apenas por Bob**.  
- **Tipo 3**: Pode ser percorrida **por ambos, Alice e Bob**.

Dado um array `edges` onde `edges[i] = [typei, ui, vi]` representa uma aresta bidirecional do tipo `typei` entre os nós `ui` e `vi`, encontre o **número máximo de arestas que podem ser removidas** de forma que, após a remoção, o grafo **ainda possa ser totalmente percorrido** por **Alice e Bob**.

> O grafo é considerado totalmente percorrido por Alice e Bob se, a partir de qualquer nó, eles puderem alcançar todos os outros nós.

Retorne o **número máximo de arestas que podem ser removidas**, ou retorne `-1` se **não for possível** que Alice e Bob percorram totalmente o grafo.

## Screenshots

### Caso 1

![Case1](/Remove%20Max/assets/img/caso1.png)

### Caso 2

![Case2](/Remove%20Max/assets/img/caso2.png)

### Caso 3

![Case3](/Remove%20Max/assets/img/caso3.png)

### Submissão

![Submission](/Remove%20Max/assets/img/submissao.png)

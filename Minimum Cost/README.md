# [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/)

Dada uma `m x n` grade. Cada célula da grade tem um sinal que aponta para a próxima célula que você deve visitar se estiver atualmente nesta célula. O sinal de `grid[i][j]` pode ser:

- `1` que significa ir para a célula à direita. (ou seja, ir de `grid[i][j]` para `grid[i][j + 1]`)
- `2` que significa ir para a célula à esquerda. (ou seja, ir de `grid[i][j]` para `grid[i][j - 1]`)
- `3` que significa ir para a célula inferior. (ou seja, ir de `grid[i][j]` para `grid[i + 1][j]`)
- `4` que significa ir para a célula superior. (ou seja, ir de `grid[i][j]` para `grid[i - 1][j]`)

Observe que pode haver alguns sinais nas células da grade que apontam para fora da grade.

Você começará inicialmente na célula superior esquerda `(0, 0)`. Um caminho válido na grade é aquele que começa na célula superior esquerda `(0, 0)` e termina na célula inferior direita, `(m - 1, n - 1)` seguindo os sinais na grade. O caminho válido não precisa ser o mais curto.

Você pode modificar o sinal em uma célula com `cost = 1`. Você pode modificar o sinal em uma célula apenas uma vez.

Retorne o custo mínimo para fazer com que a grade tenha pelo menos um caminho válido.

## Screenshots

### Caso 1

![Case1](/Minimum%20Cost/assets/img/caso1.jpeg)

### Caso 2

![Case2](/Minimum%20Cost/assets/img/caso2.jpeg)

### Caso 3

![Case3](/Minimum%20Cost/assets/img/caso3.jpeg)

### Submissão

![Submission](/Minimum%20Cost/assets/img/submissao.jpeg)

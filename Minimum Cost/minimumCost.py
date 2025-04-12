class Solution {
public:
    typedef struct Grafo {
        int valor;
        int visitado = 0;
        vector<int> adj = vector<int>(4, -1); // Direita(0), Cima(1), Esquerda(2), Baixo(3)
    } Grafo;

    int minCost(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<Grafo> grafos;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                Grafo g;
                g.valor = grid[i][j];
                // Colocando peso 1 nas arestas
                if (i - 1 >= 0) g.adj[1] = 1; // Cima
                if (j - 1 >= 0) g.adj[2] = 1; // Esquerda
                if (i + 1 < m) g.adj[3] = 1;  // Baixo
                if (j + 1 < n) g.adj[0] = 1;  // Direita

                // Colocando peso 0 na aresta com seta
                if (g.valor == 1 && g.adj[0] != -1) g.adj[0] = 0; // Direita
                if (g.valor == 2 && g.adj[2] != -1) g.adj[2] = 0; // Esquerda
                if (g.valor == 3 && g.adj[3] != -1) g.adj[3] = 0; // Baixo
                if (g.valor == 4 && g.adj[1] != -1) g.adj[1] = 0; // Cima

                grafos.push_back(g);
            }
        }
        
        // Direcoes: Direita(0), Cima(1), Esquerda(2), Baixo(3)
        int dx[] = {0, -1, 0, 1};
        int dy[] = {1, 0, -1, 0};

        // Matriz de distancias (custos minimos)
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        deque<pair<int, pair<int, int>>> q;

        dist[0][0] = 0;
        q.push_front({0, {0, 0}}); // custo, (x, y)

        while (!q.empty()) {
            int cost = q.front().first;
            int x = q.front().second.first;
            int y = q.front().second.second;
            q.pop_front();

            int idx = x * n + y;
            if (grafos[idx].visitado) continue;
            grafos[idx].visitado = 1;

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grafos[idx].adj[dir] != -1) {
                    int nextCost = cost + grafos[idx].adj[dir];
                    if (nextCost < dist[nx][ny]) {
                        dist[nx][ny] = nextCost;
                        if (grafos[idx].adj[dir] == 0)
                            q.push_front({nextCost, {nx, ny}});
                        else
                            q.push_back({nextCost, {nx, ny}});
                    }
                }
            }
        }

        return dist[m - 1][n - 1];
    }
};
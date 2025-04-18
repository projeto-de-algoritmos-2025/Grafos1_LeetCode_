class Solution {
public:
    struct Grafo {
        vector<int> adj;
    };

    // Funcao para encontrar o representante do componente
    int acharComponente(vector<int>& componente, int u) {
        if (componente[u] != u)
            componente[u] = acharComponente(componente, componente[u]); // compressao de caminho
        return componente[u];
    }

    // Unir dois componentes
    bool unir(vector<int>& componente, int u, int v) {
        int cu = acharComponente(componente, u);
        int cv = acharComponente(componente, v);
        if (cu == cv) return false; // já conectados
        componente[cu] = cv;
        return true; // união feita
    }

    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        // Ordenar edges para tipo 3 vir primeiro
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] > b[0];
        });

        vector<int> compAlice(n + 1), compBob(n + 1);
        for (int i = 1; i <= n; i++) {
            compAlice[i] = i;
            compBob[i] = i;
        }

        int usadas = 0;

        for (const auto& edge : edges) {
            int tipo = edge[0];
            int u = edge[1];
            int v = edge[2];

            if (tipo == 3) {
                bool usouAlice = unir(compAlice, u, v);
                bool usouBob = unir(compBob, u, v);
                if (usouAlice || usouBob) usadas++;
            } else if (tipo == 1) {
                if (unir(compAlice, u, v)) usadas++;
            } else if (tipo == 2) {
                if (unir(compBob, u, v)) usadas++;
            }
        }

        // Checar se todos os nos estao conectados em ambos
        auto conectado = [&](vector<int>& comp) {
            int representante = acharComponente(comp, 1);
            for (int i = 2; i <= n; i++) {
                if (acharComponente(comp, i) != representante)
                    return false;
            }
            return true;
        };

        if (!conectado(compAlice) || !conectado(compBob)) return -1;

        return edges.size() - usadas;
    }
};


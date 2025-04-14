function isBipartite(graph: number[][]): boolean {
    const S: [number, string][] = [];
    const visited: (string | null)[] = new Array(graph.length).fill(null);

    for (let i = 0; i < graph.length; i++) {
        if (visited[i] !== null) continue;

        S.push([i, 'A']);
        visited[i] = 'A';

        while (S.length > 0) {
            const [u, layer] = S.shift()!;
            const nextLayer = layer === 'A' ? 'B' : 'A';

            for (const v of graph[u]) {
                if(visited[v] === null) {
                    visited[v] = nextLayer;
                    S.push([v, nextLayer]);
                } else if (visited[v] === layer)
                    return false;
            }
        }
    }

    return true;
};
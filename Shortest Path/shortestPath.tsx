function shortestPathLength(graph: number[][]): number {
    const n = graph.length;
    const allVisitedMask = (1 << n) - 1;
    const visited = new Set<string>();
    const S: [number, number, number][] = [];

    for (let i = 0; i < n; i++) {
        const mask = 1 << i;
        S.push([i, mask, 0]);
        visited.add(`${i}-${mask}`);
    }

    while (S.length > 0) {
        const [u, mask, dist] = S.shift()!;

        if (mask === allVisitedMask) { 
            return dist;
        }

        for (const v of graph[u]) {
            const nextMask = mask | (1 << v);
            const key = `${v}-${nextMask}`;

            if (!visited.has(key)) {
                visited.add(key);
                S.push([v, nextMask, dist + 1]);
            }
        }
    }

    return 0;
};
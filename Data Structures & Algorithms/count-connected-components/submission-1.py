class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        components = 0

        def dfs(node: int) -> None:
            visited.add(node)
            for next in adj[node]:
                if next not in visited:
                    dfs(next)              


        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)

        return components
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1 :
            return False

        adj = {i: []for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node: int, parent: int) -> bool:
            visited.add(node)

            for next in adj[node]:
                if next == parent:
                    continue
                
                if next in visited:
                    return False

                if not dfs(next, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n
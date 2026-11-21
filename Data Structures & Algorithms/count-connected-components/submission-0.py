class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n
        self.components = n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return           
            
            elif rank[root_a] < rank[root_b]:
                parent[root_a] = root_b

            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            
            elif rank[root_a] == rank[root_b]:
                parent[root_b] = root_a
                rank[root_a] += 1

            self.components -= 1   
        
        for u, v in edges:
            union(u, v)

        return self.components
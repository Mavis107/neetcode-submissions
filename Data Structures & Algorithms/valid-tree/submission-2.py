class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))
        rank = [0] * n
        self.components = n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return False
            
            elif rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
        
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a

            else:
                parent[root_b] = root_a
                rank[root_a] += 1

            self.components -= 1
        
            return True              

        for u, v in edges:
            if not union(u,v):
                return False
        
        return self.components == 1

        




        
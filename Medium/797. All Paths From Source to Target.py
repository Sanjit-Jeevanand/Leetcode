class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(node,curr):
            curr.append(node)
            if node == n-1:
                ans.append(curr.copy())
            else:
                for nei in graph[node]:
                    dfs(nei, curr)
            curr.pop()
        dfs(0,[])
        return ans
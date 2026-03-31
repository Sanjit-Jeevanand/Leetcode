class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def adj(arr):
            adj_list = defaultdict(list)
            for i,j in arr:
                adj_list[j].append(i)
            return adj_list
        graph = adj(prerequisites)
        visited, pathVisited = set(), set()
        def dfs(node):
            if node in pathVisited:
                return True
            if node in visited:
                return False
            visited.add(node)
            pathVisited.add(node)
            for nei in graph[node]:
                if dfs(nei):
                    return True   
            pathVisited.remove(node)
            return False
        for course in range(numCourses):
            if dfs(course):
                return False
        return True
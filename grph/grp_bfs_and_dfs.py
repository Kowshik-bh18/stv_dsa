graph = {
    1: [2,3],
    2: [1,4],
    3: [1],
    4: [2]
}

def dfs(node,visited):
    visited.add(node)
    print(node)
    for neigh in graph[node]:
        if neigh not in visited:
            dfs(neigh,visited)
dfs(1,set())
            
#bfs
from collections import deque

def bfs(start):
    visited = set([start])
    q = deque([start])

    while q:
        node = q.popleft()
        
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                q.append(neigh)

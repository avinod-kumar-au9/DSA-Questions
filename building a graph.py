
# Adjacency List representation

def addEdge(u, v, graph, undirected=True):
    if u not in graph:
        graph[u] = list()
    graph[u].append(v)
 
    if undirected:
        if v not in graph:
            graph[v] = list()
        graph[v].append(u)
 
def addEdgeWithWeight(u, v, weight, graph, undirected=True):
    if u not in graph:
        graph[u] = list()
    graph[u].append((v, weight))
 
    if undirected:
        if v not in graph:
            graph[v] = list()
            graph[v].append((u, weight))
 
 
# Adjacency Matrix representation
 
def addEdgeAdjMatrix(u, v, graph, undirected=True):
    graph[u][v] = 1
    if undirected:
        graph[v][u] = 1
 
# def addEdgeAdjMatrixWeighted(u, v, weight, graph, undirected=True):
#     graph[u][v] = weight
#     if undirected:
#         graph[v][u] = weight
 
# representing in a graph
# graph traversal
def bfs(x,n,graph):
    queue=list()
    visited= [False for _ in range(n)]

    queue.append(x)
    visited[x]=True

    while len(queue) > 0:
        _x=queue.pop(0)
        print(_x)
        for i in range(0,n):
            if graph[_x][i] == 1 and not visited[i]:
                visited[i]=True
                queue.append(i)


# representing in a graph
# graph traversal
def dfs(x,n,graph,visited):
    
    visited[x]=True
    print(x)
    for i in range(0,n):
        if graph[x][i]==1 and not visited[i]:
            dfs(i,n,graph,visited)

def dfs_adjacency_list(x,n,graph,visited):
    visited[x]=True
    print(x)

    for neighbour in graph[x]:
        if not visited[neighbour]:
            dfs_adjacency_list(neighbour,n,graph,visited)




 
if __name__ == '__main__':
    graph = dict()
    addEdge(1, 2, graph, False)
 
    n=5
    graph=[[0 for x in range(n)] for x in range(n)]
    addEdgeAdjMatrix(0,1,graph)
    addEdgeAdjMatrix(1,2,graph)
    addEdgeAdjMatrix(0,3,graph)
    addEdgeAdjMatrix(0,4,graph)
    
    bfs(0,n,graph)

    visited= [False for _ in range(n)]
    dfs(0,n,graph,visited)


    graph = dict()

    addEdge(0,1,graph)
    addEdge(1,2,graph)
    addEdge(0,3,graph)
    addEdge(0,4,graph)

    dfs_adjacency_list(0,n,graph,visited)

    



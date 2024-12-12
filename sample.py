matrix = [
 [0,2,4,3,4],
 [2,0,3,0,0],
 [4,3,0,3,3],
 [0,0,3,3,2],
 [4,0,3,2,0]


]

visited = [0, 0, 0, 0,0]

def dfs(i):
    print(i)
    visited[i] = 1
    for j in range(len(visited)):
        if matrix[i][j] == 1 and visited[j] == 0:
            dfs(j)

def add_vertex():
    global matrix, visited
    # Add a new row and column of 0s
    for row in matrix:
        row.append(0)
    matrix.append([0] * (len(matrix) + 1))
    visited.append(0)

def delete_vertex(v):
    global matrix, visited
    # Remove the row and column corresponding to the vertex
    matrix.pop(v)
    for row in matrix:
        row.pop(v)
    visited.pop(v)

def add_edge(v1, v2):
    global matrix
    # Set the edges to 1 for both directions
    if v1 < len(matrix) and v2 < len(matrix):
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1
    else:
        print("Error: One or both vertices do not exist.")

def delete_edge(v1, v2):
    global matrix
    # Set the edges to 0 for both directions
    if v1 < len(matrix) and v2 < len(matrix):
        matrix[v1][v2] = 0
        matrix[v2][v1] = 0
    else:
        print("Error: One or both vertices do not exist.")
        
        
        
def get_edges(matrix):
    edges = []
    for i in range(len(matrix)): 
        for j in range(i + 1, len(matrix)):  # Avoid duplicates
            if matrix[i][j] != 0:
                edges.append([i, j])  # Add (u, v)  
    return edges
 
# Kruskal's algorithm
def kruskal_simple_with_cost(matrix):
    edges = get_edges(matrix)
    print("Before Sort ",edges)
    edges.sort(key=lambda edge: matrix[edge[0]][edge[1]])
    
    print("Sorted Edges ",edges)
    mst = []
    total_cost = 0
    groups = list(range(len(matrix)))  # Each node starts in its own group

    for u, v in edges:
        if groups[u] != groups[v]:  # If u and v are not in the same group
            mst.append([u, v])
            total_cost += matrix[u][v]  # Add edge weight to the total cost
            old_group = groups[v]
            new_group = groups[u]
            # Merge the groups by updating group numbers
            for i in range(len(groups)):
                if groups[i] == old_group:
                    groups[i] = new_group
    return mst, total_cost



def prims_algorithm(graph, vertices):
    INF = 9999999  # A very large number representing infinity
    selected = [False] * vertices  # Track selected vertices
    selected[0] = True  # Start from the first vertex
    mst=0
    print("Edge : Weight")
    for i in range(vertices - 1):  # Repeat until we have V-1 edges
        min_weight = INF
        x, y = 0, 0  # Initialize start and end vertices for the edge

        # Find the smallest edge connecting a selected vertex to an unselected vertex
        for j in range(vertices):
            if selected[j]:  # Only check edges from selected vertices
                for k in range(vertices):
                    if not selected[k] and graph[j][k] > 0 and graph[j][k] < min_weight:
                        min_weight = graph[j][k]
                        x, y = j, k

        print(f"{x}-{y} : {graph[x][y]}")  # Print the selected edge and its weight
        mst=mst+graph[x][y]
        selected[y] = True  # Mark the new vertex as selected
    print("Total Cost Of MST is ",mst)

# Test the simplified Kruskal's algorithm


# Test the functions
dfs(2)
print("\nInitial matrix:")
print(matrix)

# add_vertex()
# print("\nMatrix after adding a vertex:")
# print(matrix)

# add_edge(2, 5)
# print("\nMatrix after adding an edge between 2 and 5:")
# print(matrix)

# delete_edge(2, 5)
# print("\nMatrix after deleting the edge between 2 and 5:")
# print(matrix)

# delete_vertex(4)
# print("\nMatrix after deleting vertex 4:")
# print(matrix)


mst, cost = kruskal_simple_with_cost(matrix)
print("Minimum Spanning Tree (MST) edges:")
for u, v in mst:
    print(f"Edge: {u} - {v}, Weight: {matrix[u][v]}")
print(f"Total cost of MST: {cost}")

prims_algorithm(matrix,5)
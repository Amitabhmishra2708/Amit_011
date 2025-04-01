

# AI PROGRAMS

these are the searching algorithms in python 
#bfs
def bfs(graph, start_node):
   
    visited = set()
    
    queue = deque([start])
   
    visited.add(start)
    
    while queue:
     
        current_node = queue.popleft()
        print(current_node, end=" ")  
        
       
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


bfs(graph, 'A')

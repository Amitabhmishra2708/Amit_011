def dfs_with_stack(graph, start):
 
  
    stack = [start]
    visited = set()
    while stack:
       
        current_node = stack.pop()
        if current_node not in visited:
          
            visited.add(current_node)
            print(current_node, end=" ")  # Process the node (print it in this case)
            
          
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


dfs_with_stack(graph, 'A')

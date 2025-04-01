

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
#dfs
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
#vaccume_cleaner_agent
def reflex_vacuum_agent(location,status):
  if status == "Dirty":
    return "Suck"
  elif location == "A":
    return "Right"
  elif location == "B":
    return "Left"
    
    
location =  "A"
status = "Dirty"


action = reflex_vacuum_agent(location,status)
print(f"Location: {location}, Status: {status}, Action : {action}")


def reflex_vacuum_agent(location,status):
  if status == "Dirty":
    return "Suck"
  elif location == "A":
    return "Right"
  elif location == "B":
    return "Left"
    
    
location =  "A"
status = "Dirty"
locations = ["A","B"]


for _ in range(5):
  action = reflex_vacuum_agent(location,status)
  print(f"Location: {location}, Status: {status}, Action : {action}")
  if action == "Suck":
    status = "Clean"
  elif action == "Right":
    location = "B"
  elif action == "Left":
    location = "A"
    
    
def move_towards_goal(position,goal):
  while position < goal:
    position +=1
    print(f"Current Position: {position}")
  print("Reached the goal!")
  
  
initial_pos=0
goal_pos=5


move_towards_goal(initial_pos,goal_pos)


def display(room):
  print(room)
  
  
room = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print("All the rooms are dirty")
display(room)


#Randomly assign rooms as dirty
x=0


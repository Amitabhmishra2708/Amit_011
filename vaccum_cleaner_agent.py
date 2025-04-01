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

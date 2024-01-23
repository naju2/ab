import heapq

example_map = {
'S': {'A':1,'G':10},
'A': {'B':2, 'C':1, 'S':1},
'B': {'D':5, 'A':2},
'C': {'D':1, 'G':4, 'A':1},
'D': {'G':2, 'C':1, 'B':5},
'G': {'S':10, 'C':4, 'D':2},
}

heuristic1 = {
    'S' :5,
    'A' :3,
    'B' :4,
    'C' :2,
    'D' :6,
    'G' :0,
    
}

# A* search algorithm
def a_star_search(graph, start, goal, heuristic):
    open_list = [(0,start)]
    closed_list =set()
    g_score ={location : float('inf') for location in graph}
    g_score[start] =0
    
    while open_list:
        current_g, current_node = heapq.heappop(open_list)
        
        if current_node ==goal:
            return g_score[goal]
        
        if current_node in closed_list:
            continue
        
        closed_list.add(current_node)
        for neighbor, distance in graph[current_node].items():
            tentative_g =g_score[current_node] + distance
            
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic1[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
                
    return float('inf') # if no path is found

start_location = 'S'
goal_location = 'G'

shortest_distance = a_star_search(example_map, start_location, goal_location, heuristic1)

if shortest_distance < float('inf'):
    print("\nThe shortest distance from {0} to {1} is {2} km.\n".format(start_location,goal_location,shortest_distance))
else:
    print("No path found {start_location} to {goal_location}")
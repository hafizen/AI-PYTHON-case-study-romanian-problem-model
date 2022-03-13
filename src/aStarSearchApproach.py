from queue import PriorityQueue

# Store adjacency city path and this actual distance in nested dictionary
graph = {
    'BL':{'J':233},
    'J':{'BL':233, 'B':56, 'C':219},
    'B':{'J':56, 'Ba':124},
    'C':{'Ba':129, 'S':234, 'Ci':170, 'P':146},
    'Ba':{'B':124, 'C':129, 'T':111},
    'T':{'Ba':111, 'Ci':140},
    'Ci':{'T':140, 'C':172, 'P':50},
    'P':{'Ci':50, 'C':146, 'Y':168},
    'S':{'C':234, 'Y':130},
    'Y':{ 'S':130, 'Ci':172, 'P':168},
}

# Store heuristic value (estimate cost) to reach goal state
straightLineDistance = {
    'BL': 629,
    'J': 446,
    'B': 421,
    'Ba': 320,
    'C': 246,
    'T': 248,
    'P': 132,
    'Ci': 156,
    'S': 108,
    'Y': 0
}

# Define function to implement A * Search
def aStarSearch(graph, straightLineDistance, start, goal):
    
    sld = straightLineDistance

    pq = PriorityQueue()
    explored = {}

    pq.put((sld[start], 0, start, [start]))

    explored[start] = sld[start]

    while not pq.empty():
        (heuristic, cost, vertex, path) = pq.get()

        if vertex == goal:
            return path
        for next_node in graph[vertex].keys():
            current_cost = cost + graph[vertex][next_node]
            heuristic = current_cost + sld[next_node]
            
            if not next_node in explored or explored[next_node] >= heuristic:
                explored[next_node] = heuristic
                pq.put((heuristic, current_cost, next_node , path + [next_node]))
            
# Define main function to operate function
def main():

    # Define start state and goal state
    start = 'BL'
    goal = 'Y'

    # Display path from result A * Search
    if start not in graph or goal not in graph:
        print('City does not exist.')
    else:
        path = aStarSearch(graph, straightLineDistance, start, goal)
        print(' -> '.join(i for i in path))

# Run the program using call main function
main()


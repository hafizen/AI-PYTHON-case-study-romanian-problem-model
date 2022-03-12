# Store adjacency city path and this estimate cost form goal state in nested dictionary
graph = {
    'BL':[['J',446]],
	'J':[['BL',629], ['B',421], ['C',246]],
	'B':[['J',446], ['Ba',320]],
	'C':[['Ba',320], ['S',108], ['Ci',156], ['P',132]],
	'Ba':[['B',320], ['C',246], ['T',248]],
	'T':[['Ba',320], ['Ci',156]],
	'Ci':[['T',248], ['C',246], ['P',132]],
	'P':[['Ci',156], ['C',246], ['Y',0]],
	'S':[['C',246], ['Y',0]],
	'Y':[['S',108], ['Ci',156], ['P',132]]
}

# Define function to implement Greedy Best First Search
def greedyBestFirstSearch(graph, start, goal):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in explored:
            explored.append(node)
            if node == goal:
                break
            adjacent = graph[node]
            adjacent.sort(key=lambda a: a[1])
            queue = adjacent.pop(0)

    print( ' -> '.join(i for i in explored))


# Define main function to operate A * Star function
def main():
    # Define start state and goal state
    start = 'BL'
    goal = 'Y'

    # get path route using call the function A * Search
    greedyBestFirstSearch(graph, start, goal)

# Run the program using call main function
main()
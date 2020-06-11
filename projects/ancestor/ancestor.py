
def earliest_ancestor(ancestors, starting_node):
    #store data in graph
    graph = {}

    #put graph in reverse order relationships
    #normal relationships help find children easily, but we are interested in ancestors
    for a1, a2 in ancestors:
        if a2 in graph:
            graph[a2].append(a1)
        else:
            graph[a2] = [a1]
    
    #if no ancestors, return -1
    if starting_node not in graph:
        return -1

    #otherwise, iterate through ancestors to find earliest    
    else:

        #data structures for finding ancestor
        levels = {starting_node: 0}
        current_max = 0
        max_ancestor = starting_node
        stack = [starting_node]

        #iterate over all ancestors, storing the earliest ones
        while stack:
            node = stack.pop()
            if node in graph:
                for a in graph[node]:
                    levels[a] = levels[node] + 1
                    stack.append(a)
                    if levels[a] > current_max:
                        current_max = levels[a]
                        max_ancestor = a
        return max_ancestor
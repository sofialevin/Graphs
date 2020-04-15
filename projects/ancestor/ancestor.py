from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    graph.add_vertex(starting_node)

    for i in ancestors:
        if i[1] == starting_node:
            graph.add_vertex(i[0])
            graph.add_edge(i[1], i[0])
    for i in ancestors:
        if i[1] in graph.vertices and i[0] not in graph.vertices[i[1]]:
            graph.add_vertex(i[0])
            graph.add_edge(i[1], i[0])

    graph.dfs(starting_node, 10)

    path = ["0"]
    for i in ancestors:
        if graph.dfs(starting_node, i[0]) and len(graph.dfs(starting_node, i[0])) > len(path):
            path = graph.dfs(starting_node, i[0])

    if len(path) == 1:
        return - 1
    
    return path[-1]

    # while len(ancestors) > 0:
    #     for i in range(len(ancestors) - 1):
    #         if ancestors[i][1] == starting_node:
    #             graph.add_vertex(ancestors[i][0])
    #             graph.add_edge(ancestors[i][0], ancestors[i][1])
    #             del ancestors[i]
    #         elif ancestors[i][1] in graph.vertices and ancestors[i][0] not in graph.vertices:
    #             graph.add_vertex(ancestors[i][0])
    #             graph.add_edge(ancestors[i][0], ancestors[i][1])
    #             del ancestors[i]


        # current_node = ancestors.pop()
        # if current_node[1] == starting_node:
        #     graph.add_vertex(current_node[0])
        #     graph.add_edge(current_node[1], current_node[0])
        # if current_node[1] in graph.vertices and current_node[0] not in graph.vertices:
        #     graph.add_vertex(current_node[0])
        #     graph.add_edge(current_node[1], current_node[0])

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(ancestors, 1)
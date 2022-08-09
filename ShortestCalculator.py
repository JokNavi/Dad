import igraph as ig
def shortestPath(Input, Weight, Goal):
    g = Input
#6,        [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)]
    # Find the shortest path on a weighted graph
    g.es["weight"] = Weight

    # g.get_shortest_paths() returns a list of edge ID paths
    results = g.get_shortest_paths(
        0,
        to=Goal,
        weights=g.es["weight"],
        output="epath",
    )
    #print(results) 

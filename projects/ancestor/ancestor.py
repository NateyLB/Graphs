from graph import Graph
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_edge(pair[0], pair[1])
    def find_ancestors(starting_node, ancestors=[]):
        # find parents
        for key, val in graph.vertices.items():
            for v in val:
                if v == starting_node:
                    # add ancestors
                    ancestors.append(key)
        # if ancestors exist
        if len(ancestors) > 0:
            new_start = ancestors.pop()
            return find_ancestors(new_start, ancestors)
        else:
            return starting_node
        
    oldest = find_ancestors(starting_node)
    if oldest == starting_node:
        return -1
    return oldest
       

if __name__ == "__main__":
     test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
     print(earliest_ancestor(test_ancestors, 2))
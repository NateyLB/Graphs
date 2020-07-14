from graph import Graph
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_edge(pair[0], pair[1])
    def find_ancestors(starting_node, ancestors=[]):
        # if len(ancestors) == 0:
        #     return starting_node
        for key, val in graph.vertices.items():
            for v in val:
                if v == starting_node:
                    ancestors.append(key)
        # print(ancestors)
        if len(ancestors) > 0:
            new_start = ancestors.pop()
            find_ancestors(new_start, ancestors)
        else:
            # print(len(ancestors), "LEN")
            print(starting_node, "starting")
            return starting_node
            
    return find_ancestors(starting_node)
       

    # if len(ancestors) > 0:
    #     return ancestors.pop()
    # return -1
if __name__ == "__main__":
     test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    #  test_ancestors =[(5,3), (6,3), (7,1), (4,7), (1,2), (7,6), (2,4), (3,5), (2,3), (4,6)]
     print(earliest_ancestor(test_ancestors, 9))
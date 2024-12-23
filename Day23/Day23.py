
from collections import defaultdict

def parse_input(file_path):
    """
    Reads the input file and returns a list of connections.
    """
    with open(file_path, 'r') as f:
        connections = [line.strip().split('-') for line in f.readlines()]
    return connections

def build_graph(connections):
    """
    Builds an adjacency list representation of the graph from the connections.
    """
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triangles(graph):
    """
    Finds all triangles (sets of three fully-connected nodes) in the graph.
    """
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            common_neighbors = neighbors & graph[neighbor]
            for cn in common_neighbors:
                triangle = tuple(sorted([node, neighbor, cn]))
                triangles.add(triangle)
    return triangles

def count_triangles_with_t(triangles):
    """
    Counts the triangles where at least one node starts with 't'.
    """
    return sum(1 for triangle in triangles if any(node.startswith('t') for node in triangle))

def find_largest_clique(graph):
    """
    Finds the largest clique (set of fully-connected nodes) in the graph.
    """
    def is_clique(nodes):
        return all(graph[a].issuperset(nodes - {a}) for a in nodes)

    largest_clique = set()
    nodes = list(graph.keys())

    def backtrack(current_clique, remaining_nodes):
        nonlocal largest_clique
        if len(current_clique) > len(largest_clique):
            largest_clique = set(current_clique)

        for i, node in enumerate(remaining_nodes):
            new_clique = current_clique | {node}
            if is_clique(new_clique):
                backtrack(new_clique, remaining_nodes[i+1:])

    backtrack(set(), nodes)  # Use a list for remaining_nodes
    return largest_clique

def get_password(largest_clique):
    """
    Generates the password for the LAN party from the largest clique.
    """
    return ",".join(sorted(largest_clique))

def main():
    input_file = "input.txt"  # Change this to your input file's name
    connections = parse_input(input_file)
    graph = build_graph(connections)

    # Part 1: Find triangles with at least one node starting with 't'
    triangles = find_triangles(graph)
    triangles_with_t_count = count_triangles_with_t(triangles)
    print(f"Total triangles with at least one 't' computer: {triangles_with_t_count}")

    # Part 2: Find the largest clique and get the LAN party password
    largest_clique = find_largest_clique(graph)
    password = get_password(largest_clique)
    print(f"Password to get into the LAN party: {password}")

if __name__ == "__main__":
    main()

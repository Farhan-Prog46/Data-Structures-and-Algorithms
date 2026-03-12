# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 06
# ----------------------------------------
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# South American countries
countries = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia",
    "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname",
    "Uruguay", "Venezuela"
]

# Weighted edgesArhge
weighted_edges = [
    ("Argentina", "Bolivia", 1824),
    ("Argentina", "Brazil", 2239),
    ("Argentina", "Chile", 1140),
    ("Argentina", "Paraguay", 1002),
    ("Argentina", "Uruguay", 950),
    ("Bolivia", "Brazil", 1477),
    ("Bolivia", "Chile", 1702),
    ("Bolivia", "Paraguay", 1210),
    ("Bolivia", "Peru", 1086),
    ("Brazil", "Colombia", 2456),
    ("Brazil", "Guyana", 2460),
    ("Brazil", "Paraguay", 1331),
    ("Brazil", "Peru", 3012),
    ("Brazil", "Suriname", 2798),
    ("Brazil", "Uruguay", 1769),
    ("Brazil", "Venezuela", 2193),
    ("Chile", "Peru", 2344),
    ("Colombia", "Ecuador", 1287),
    ("Colombia", "Peru", 1887),
    ("Colombia", "Venezuela", 1022),
    ("Ecuador", "Peru", 1324),
    ("Guyana", "Suriname", 285),
    ("Guyana", "Venezuela", 1536),
    ("Paraguay", "Uruguay", 1114)
]

# ---------------------------------------------------
# Build adjacency list
# ---------------------------------------------------
def build_graph(countries, edges):
    graph = {country: [] for country in countries}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph

# ---------------------------------------------------
# Print adjacency list
# ---------------------------------------------------
def print_adjacency_list(graph, title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    for node in graph:
        print(f"{node}: {graph[node]}")

# ---------------------------------------------------
# Union-Find for Kruskal
# ---------------------------------------------------
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

# ---------------------------------------------------
# Kruskal's Algorithm
# ---------------------------------------------------
def kruskal_mst(countries, edges):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    ds = DisjointSet(countries)

    mst = []
    total_weight = 0

    for u, v, w in sorted_edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight

# ---------------------------------------------------
# Prim's Algorithm
# ---------------------------------------------------
def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_node, parent)
    mst = []
    total_weight = 0

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)

        if parent is not None:
            mst.append((parent, current, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst, total_weight

# ---------------------------------------------------
# Convert edge list to adjacency list
# ---------------------------------------------------
def mst_to_adjacency_list(countries, mst_edges):
    mst_graph = {country: [] for country in countries}
    for u, v, w in mst_edges:
        mst_graph[u].append((v, w))
        mst_graph[v].append((u, w))
    return mst_graph

# ---------------------------------------------------
# Print MST edges
# ---------------------------------------------------
def print_mst(mst, total_weight, title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    for u, v, w in mst:
        print(f"{u} -- {v} : {w} km")
    print(f"\nTotal Weight = {total_weight} km")

# ---------------------------------------------------
# Draw graph using networkx
# ---------------------------------------------------
def draw_graph(countries, edges, title):
    G = nx.Graph()
    G.add_nodes_from(countries)

    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos,
        with_labels=True,
        node_size=2000,
        node_color="lightblue",
        font_size=8,
        font_weight="bold"
    )

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    plt.title(title)
    plt.show()

# ---------------------------------------------------
# Main
# ---------------------------------------------------
def main():
    graph = build_graph(countries, weighted_edges)

    # Original graph adjacency list
    print_adjacency_list(graph, "Original Graph Adjacency List")

    # User input for Prim
    print("\nAvailable countries:")
    for country in countries:
        print("-", country)

    start_country = input("\nEnter starting country for Prim's Algorithm: ").strip()

    if start_country not in countries:
        print("Invalid country name. Using Argentina as default.")
        start_country = "Argentina"

    # Kruskal
    kruskal_edges, kruskal_weight = kruskal_mst(countries, weighted_edges)
    print_mst(kruskal_edges, kruskal_weight, "Kruskal's MST")

    # Prim
    prim_edges, prim_weight = prim_mst(graph, start_country)
    print_mst(prim_edges, prim_weight, f"Prim's MST (Start: {start_country})")

    # Adjacency list of both MSTs
    kruskal_graph = mst_to_adjacency_list(countries, kruskal_edges)
    prim_graph = mst_to_adjacency_list(countries, prim_edges)

    print_adjacency_list(kruskal_graph, "Kruskal MST Adjacency List")
    print_adjacency_list(prim_graph, "Prim MST Adjacency List")

    # Comparison
    print("\n" + "=" * 60)
    print("Comparison of Kruskal's and Prim's MST")
    print("=" * 60)
    print(f"Kruskal Total Weight: {kruskal_weight} km")
    print(f"Prim Total Weight:    {prim_weight} km")

    if kruskal_weight == prim_weight:
        print("\nBoth algorithms produced MSTs with the same total weight.")
        print("This is expected because both correctly compute a Minimum Spanning Tree.")
        print("The order of selected edges may differ, especially depending on the starting node in Prim's algorithm.")
    else:
        print("\nThe total weights are different.")
        print("This can happen if there are implementation issues or if the graph handling is incorrect.")

    # Draw graphs
    draw_graph(countries, weighted_edges, "Original South American Graph")
    draw_graph(countries, kruskal_edges, "Kruskal's Minimum Spanning Tree")
    draw_graph(countries, prim_edges, f"Prim's Minimum Spanning Tree (Start: {start_country})")

if __name__ == "__main__":
    main()
# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 06
# ----------------------------------------
import heapq

# List of South American countries
countries = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia",
    "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname",
    "Uruguay", "Venezuela"
]

# Weighted edges (country1, country2, distance in km)
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

# Function to build adjacency list
def build_graph(countries, weighted_edges):
    graph = {country: [] for country in countries}

    for country1, country2, distance in weighted_edges:
        graph[country1].append((country2, distance))
        graph[country2].append((country1, distance))  # undirected graph

    return graph

# Dijkstra's Algorithm
def dijkstra(graph, start):
    # Distance from start to every country
    distances = {country: float('inf') for country in graph}
    distances[start] = 0

    # To store previous node for path reconstruction
    previous = {country: None for country in graph}

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_country = heapq.heappop(priority_queue)

        # Skip if we already found a shorter path
        if current_distance > distances[current_country]:
            continue

        # Check all neighbors
        for neighbor, weight in graph[current_country]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_country
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous

# Function to reconstruct path
def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == start:
        return path
    return []

# Function to display adjacency list
def display_adjacency_list(graph):
    print("\nAdjacency List:")
    for country in graph:
        print(f"{country}: {graph[country]}")

# Function to display shortest paths
def display_results(graph, start):
    distances, previous = dijkstra(graph, start)

    print("\n" + "=" * 60)
    print(f"Shortest paths from {start}")
    print("=" * 60)

    for country in graph:
        if country == start:
            continue

        if distances[country] == float('inf'):
            print(f"{start} -> {country}: No path found")
        else:
            path = get_path(previous, start, country)
            print(f"{start} -> {country}")
            print(f"Distance: {distances[country]} km")
            print(f"Path: {' -> '.join(path)}")
            print("-" * 60)

# Main program
def main():
    graph = build_graph(countries, weighted_edges)

    display_adjacency_list(graph)

    while True:
        print("\nAvailable countries:")
        for country in countries:
            print("-", country)

        start_country = input("\nEnter starting country: ").strip()

        if start_country not in graph:
            print("Invalid country name. Please try again.")
            continue

        display_results(graph, start_country)

        choice = input("\nDo you want to try another starting country? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Program ended.")
            break

if __name__ == "__main__":
    main()
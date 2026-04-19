import heapq

# Chennai delivery network graph (adjacency list)
graph = {
    "Warehouse_TNagar": [("Kodambakkam", 3), ("Nungambakkam", 4), ("Guindy", 5)],
    "Kodambakkam": [("Warehouse_TNagar", 3), ("Vadapalani", 2), ("AnnaNagar", 6)],
    "Nungambakkam": [("Warehouse_TNagar", 4), ("Egmore", 3), ("AnnaNagar", 5)],
    "Guindy": [("Warehouse_TNagar", 5), ("Velachery", 4), ("Adyar", 6)],
    "Vadapalani": [("Kodambakkam", 2), ("AnnaNagar", 4)],
    "AnnaNagar": [("Kodambakkam", 6), ("Nungambakkam", 5), ("Vadapalani", 4), ("Egmore", 4)],
    "Egmore": [("Nungambakkam", 3), ("AnnaNagar", 4), ("Mylapore", 5)],
    "Velachery": [("Guindy", 4), ("Tambaram", 8), ("Adyar", 3)],
    "Adyar": [("Guindy", 6), ("Velachery", 3), ("Mylapore", 4)],
    "Mylapore": [("Egmore", 5), ("Adyar", 4)],
    "Tambaram": [("Velachery", 8)]
}


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


def get_path(previous, destination):
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path
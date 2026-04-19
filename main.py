from graph import graph, dijkstra, get_path

def main():
    source = "Warehouse_TNagar"
    distances, previous = dijkstra(graph, source)

    print("=" * 60)
    print("  DELIVERY OPTIMIZATION USING DIJKSTRA'S ALGORITHM")
    print("=" * 60)
    print(f"  Source: {source}\n")

    for destination in graph:
        if destination == source:
            continue
        path = get_path(previous, destination)
        print(f"Destination : {destination}")
        print(f"Distance    : {distances[destination]} km")
        print(f"Route       : {' -> '.join(path)}")
        print("-" * 60)

if __name__ == "__main__":
    main()
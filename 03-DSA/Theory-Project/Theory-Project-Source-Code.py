# ==========================================
#       WEIGHTED CITY ROUTE FINDER
#       DIJKSTRA'S SHORTEST PATH
# ==========================================


# PART 1: CUSTOM QUEUE (FOR BFS)

class Queue:

    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.items[self.front]
        self.front += 1
        return item

    def is_empty(self):
        return self.front == len(self.items)


# PART 2: GRAPH

class Graph:

    def __init__(self):
        self.locations = {}

    # Add location
    def add_location(self, name):

        name = name.strip().title()

        if not name:
            print("Location name cannot be empty.")

        elif name in self.locations:
            print("Location already exists.")

        else:
            self.locations[name] = {}
            print("Location added successfully.")

    # Remove location
    def remove_location(self, name):

        name = name.strip().title()

        if name not in self.locations:
            print("Location not found.")
            return

        for neighbours in self.locations.values():
            neighbours.pop(name, None)

        del self.locations[name]

        print("Location removed successfully.")

    # Add road with distance
    def add_road(self, loc1, loc2, distance):

        loc1 = loc1.strip().title()
        loc2 = loc2.strip().title()

        if loc1 not in self.locations or loc2 not in self.locations:
            print("Location not found.")
            return

        if loc1 == loc2:
            print("A location cannot connect to itself.")
            return

        if distance <= 0:
            print("Distance must be greater than zero.")
            return

        if loc2 in self.locations[loc1]:
            print("Road already exists. Use Update Road Distance.")
            return

        # Undirected weighted connection
        self.locations[loc1][loc2] = distance
        self.locations[loc2][loc1] = distance

        print("Road added successfully.")

    # Remove road
    def remove_road(self, loc1, loc2):

        loc1 = loc1.strip().title()
        loc2 = loc2.strip().title()

        if loc1 not in self.locations or loc2 not in self.locations:
            print("Location not found.")
            return

        if loc2 not in self.locations[loc1]:
            print("Road does not exist.")
            return

        del self.locations[loc1][loc2]
        del self.locations[loc2][loc1]

        print("Road removed successfully.")

    # Update road distance
    def update_road(self, loc1, loc2, distance):

        loc1 = loc1.strip().title()
        loc2 = loc2.strip().title()

        if loc1 not in self.locations or loc2 not in self.locations:
            print("Location not found.")
            return

        if loc2 not in self.locations[loc1]:
            print("Road does not exist.")
            return

        if distance <= 0:
            print("Distance must be greater than zero.")
            return

        self.locations[loc1][loc2] = distance
        self.locations[loc2][loc1] = distance

        print("Road distance updated successfully.")

    # Display weighted city map
    def display_map(self):

        if not self.locations:
            print("City map is empty.")
            return

        print("\n========== WEIGHTED CITY MAP ==========")

        for location in self.locations:

            print("\n" + location)

            if not self.locations[location]:
                print("   No road connections.")
            else:
                for neighbour, distance in self.locations[location].items():
                    print("   -->", neighbour, ":", distance, "km")

    # Dijkstra's shortest distance algorithm
    def shortest_route(self, start, destination):

        start = start.strip().title()
        destination = destination.strip().title()

        if start not in self.locations or destination not in self.locations:
            print("Invalid location.")
            return

        if start == destination:
            print("\nYou are already at your destination.")
            print("Route:", start)
            print("Total distance: 0 km")
            return

        # Store shortest known distances
        distances = {}

        # Store previous location
        parent = {}

        # Store unvisited locations
        unvisited = set(self.locations)

        for location in self.locations:
            distances[location] = float('inf')
            parent[location] = None

        distances[start] = 0

        # Dijkstra's main loop
        while unvisited:

            current = min(
                unvisited,
                key=lambda location: distances[location]
            )

            if distances[current] == float('inf'):
                break

            unvisited.remove(current)

            if current == destination:
                break

            # Check connected neighbours
            for neighbour, weight in self.locations[current].items():

                if neighbour in unvisited:

                    new_distance = distances[current] + weight

                    if new_distance < distances[neighbour]:

                        distances[neighbour] = new_distance
                        parent[neighbour] = current

        # Check whether destination is reachable
        if distances[destination] == float('inf'):
            print("No route exists.")
            return

        # Reconstruct shortest route
        path = []
        current = destination

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        print("\n========== DIJKSTRA SHORTEST ROUTE ==========")

        for location in path:
            print(location)

        print("\nTotal locations:", len(path))
        print("Total roads:", len(path) - 1)
        print("Total distance:", distances[destination], "km")

        # Show individual road distances
        print("\nRoad-wise distances:")

        for i in range(len(path) - 1):

            distance = self.locations[path[i]][path[i + 1]]

            print(
                path[i], "-->",
                path[i + 1], ":",
                distance, "km"
            )

    # BFS: Route with minimum number of roads
    def fewest_roads_route(self, start, destination):

        start = start.strip().title()
        destination = destination.strip().title()

        if start not in self.locations or destination not in self.locations:
            print("Invalid location.")
            return

        queue = Queue()
        visited = set()
        parent = {}

        queue.enqueue(start)
        visited.add(start)
        parent[start] = None

        found = False

        while not queue.is_empty():

            current = queue.dequeue()

            if current == destination:
                found = True
                break

            for neighbour in self.locations[current]:

                if neighbour not in visited:

                    visited.add(neighbour)
                    parent[neighbour] = current
                    queue.enqueue(neighbour)

        if not found:
            print("No route exists.")
            return

        # Build route
        path = []
        current = destination

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        # Calculate distance of this BFS route
        total_distance = 0

        for i in range(len(path) - 1):
            total_distance += self.locations[path[i]][path[i + 1]]

        print("\n========== BFS ROUTE (FEWEST ROADS) ==========")

        for location in path:
            print(location)

        print("Total roads:", len(path) - 1)
        print("Total distance:", total_distance, "km")


# PART 3: CREATE CITY

city = Graph()

locations = [
    "University",
    "Hospital",
    "Airport",
    "Shopping Mall",
    "Railway Station",
    "Bus Terminal",
    "Stadium",
    "City Center",
    "Library",
    "Park"
]

for location in locations:
    city.add_location(location)


# Sample road distances in kilometres
# These are illustrative values, not actual measurements.

roads = [
    ("University", "City Center", 4),
    ("University", "Library", 2),
    ("City Center", "Hospital", 5),
    ("City Center", "Railway Station", 3),
    ("City Center", "Shopping Mall", 4),
    ("Library", "Park", 3),
    ("Park", "Hospital", 4),
    ("Hospital", "Airport", 8),
    ("Railway Station", "Airport", 6),
    ("Railway Station", "Bus Terminal", 2),
    ("Shopping Mall", "Stadium", 3),
    ("Stadium", "Airport", 7),
    ("Bus Terminal", "Airport", 4)
]

for road in roads:
    city.add_road(road[0], road[1], road[2])


# PART 4: MAIN MENU

while True:

    print("\n========== CITY ROUTE FINDER ==========")
    print("1. Add Location")
    print("2. Remove Location")
    print("3. Add Road")
    print("4. Remove Road")
    print("5. Update Road Distance")
    print("6. Display Weighted City Map")
    print("7. Find Shortest Distance (Dijkstra)")
    print("8. Find Route with Fewest Roads (BFS)")
    print("9. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":

        name = input("Enter location name: ")
        city.add_location(name)

    elif choice == "2":

        name = input("Enter location to remove: ")
        city.remove_location(name)

    elif choice == "3":

        loc1 = input("Enter first location: ")
        loc2 = input("Enter second location: ")

        try:
            distance = float(input("Enter road distance in km: "))
            city.add_road(loc1, loc2, distance)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":

        loc1 = input("Enter first location: ")
        loc2 = input("Enter second location: ")

        city.remove_road(loc1, loc2)

    elif choice == "5":

        loc1 = input("Enter first location: ")
        loc2 = input("Enter second location: ")

        try:
            distance = float(input("Enter new distance in km: "))
            city.update_road(loc1, loc2, distance)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "6":

        city.display_map()

    elif choice == "7":

        start = input("Enter starting location: ")
        destination = input("Enter destination: ")

        city.shortest_route(start, destination)

    elif choice == "8":

        start = input("Enter starting location: ")
        destination = input("Enter destination: ")

        city.fewest_roads_route(start, destination)

    elif choice == "9":

        print("Thank you for using City Route Finder!")
        break

    else:

        print("Invalid choice. Try again.")
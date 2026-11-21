# ==================================================
# OBJECT:
# ELECTRICAL POWER DISTRIBUTION SYSTEM
# USING TREE DATA STRUCTURE
# ==================================================


# 1. NODE CLASS

class Node:

    def __init__(self, name, type):

        self.name = name
        self.type = type
        self.children = []


# 2. TREE CLASS

class ElectricalPowerTree:

    def __init__(self):

        self.root = Node("Power Plant", "Power Plant")


    # 3. ADD COMPONENT

    def add_component(self, parent_name, name, type):

        parent = self.search(parent_name)

        if parent == None:
            print("Parent not found!")
            return

        if self.search(name) != None:
            print("Component already exists!")
            return

        new_node = Node(name, type)

        parent.children.append(new_node)

        print(name, "added successfully!")


    # 4. SEARCH COMPONENT

    def search(self, name, node=None):

        if node == None:
            node = self.root

        if node.name == name:
            return node

        for child in node.children:

            result = self.search(name, child)

            if result != None:
                return result

        return None


    # 5. PREORDER TRAVERSAL

    def preorder(self, node=None):

        if node == None:
            node = self.root

        print(node.name)

        for child in node.children:
            self.preorder(child)


    # 6. LEVEL ORDER TRAVERSAL

    def level_order(self):

        queue = [self.root]

        while len(queue) > 0:

            node = queue.pop(0)

            print(node.name)

            for child in node.children:
                queue.append(child)


    # 7. DISPLAY TREE

    def display(self, node=None, level=0):

        if node == None:
            node = self.root

        print("    " * level + "|-- " + node.name)

        for child in node.children:
            self.display(child, level + 1)


# 8. CREATE ELECTRICAL DISTRIBUTION SYSTEM

tree = ElectricalPowerTree()

# Add Grid Station
tree.add_component("Power Plant", "Grid Station", "Grid Station")

# Add Substations
tree.add_component("Grid Station", "Substation 1", "Substation")
tree.add_component("Grid Station", "Substation 2", "Substation")

# Add Transformers
tree.add_component("Substation 1", "Transformer 1", "Transformer")
tree.add_component("Substation 1", "Transformer 2", "Transformer")

tree.add_component("Substation 2", "Transformer 3", "Transformer")
tree.add_component("Substation 2", "Transformer 4", "Transformer")

# Add Houses
tree.add_component("Transformer 1", "House 1", "House")
tree.add_component("Transformer 1", "House 2", "House")

tree.add_component("Transformer 2", "House 3", "House")
tree.add_component("Transformer 2", "House 4", "House")

tree.add_component("Transformer 3", "House 5", "House")
tree.add_component("Transformer 3", "House 6", "House")

tree.add_component("Transformer 4", "House 7", "House")
tree.add_component("Transformer 4", "House 8", "House")


# 9. MAIN MENU

while True:

    print("\n======================================")
    print(" ELECTRICAL POWER DISTRIBUTION SYSTEM")
    print("======================================")

    print("1. Display Complete System")
    print("2. Add New Component")
    print("3. Search Component")
    print("4. Preorder Traversal")
    print("5. Level Order Traversal")
    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        print("\nComplete Distribution System:")
        tree.display()


    elif choice == "2":

        parent = input("Enter parent name: ")
        name = input("Enter component name: ")
        type = input("Enter component type: ")

        tree.add_component(parent, name, type)


    elif choice == "3":

        name = input("Enter component name to search: ")

        result = tree.search(name)

        if result != None:

            print("Component Found!")
            print("Name:", result.name)
            print("Type:", result.type)

        else:

            print("Component Not Found!")


    elif choice == "4":

        print("\nPreorder Traversal:")
        tree.preorder()


    elif choice == "5":

        print("\nLevel Order Traversal:")
        tree.level_order()


    elif choice == "6":

        print("Thank you for using the system!")
        break


    else:

        print("Invalid choice! Try again.")
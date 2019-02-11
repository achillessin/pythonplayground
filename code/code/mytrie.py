class Node:
    def __init__(self, val):
        self.val = val
        self.cities = list()
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = Node("")

    def add_city(self, city):
        self._add_string(self.root, city, city)

    def _add_string(self, node, string, city):
        node.cities.append(city)
        if len(string) > 0:
            first_char = string[0]
            if not node.children.get(first_char.lower()):
                node.children[first_char.lower()] = Node(first_char.lower())
            self._add_string(node.children[first_char.lower()], string[1:], city)

    def search_cities(self, string):
        search_node = self.root
        search_string = string
        matches = []
        while len(search_string) > 0:
            first_char = search_string[0]
            search_node = search_node.children.get(first_char)
            if not search_node:
                return matches
            else:
                matches = search_node.cities
        return matches



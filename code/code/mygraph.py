from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = dict()
    def add_neighbor(self, node):
        self.neighbors[node.val] = node
    def __str__(self):
        return '%s: %s' % (self.val, str([v.val for k,v in self.neighbors.items()]))

class Graph(object):
    def __init__(self):
        self.nodes = dict()

    def add_node(self, node):
        self.nodes[node.val] = node

    def add_edge(self, node1, node2):
        self.nodes[node1.val].add_neighbor(node2)

    def clone_bfs(self):
        """ O(V+E)"""
        queue = deque()
        visited = dict()
        cloned_graph = Graph()
        for _,n in self.nodes.items():
            new_node = Node(n.val)
            cloned_graph.nodes[new_node.val] = new_node
            queue.append(n)

        while queue:
            print('queue size at start: ', len(queue))
            node_to_traverse = queue.pop()
            visited[node_to_traverse.val] = node_to_traverse
            cloned_node = cloned_graph.nodes[node_to_traverse.val]
            print('working with node:', node_to_traverse.val)

             # add the neighbors
            for _,n in node_to_traverse.neighbors.items():
                cloned_node_2 = cloned_graph.nodes[n.val]
                cloned_graph.add_edge(cloned_node, cloned_node_2)
                if n.val not in visited:
                    queue.append(n)

        return cloned_graph


    def clone_dfs_recursive(self):
        """O(V+E)"""
        global_visited = dict()
        cloned_graph = Graph()
        for _,n in self.nodes.items():
            new_node = Node(n.val)
            cloned_graph.nodes[new_node.val] = new_node

        for _,n in self.nodes.items():
            print('ensuring path for node %s is covered' % n.val)
            self._dfs_util_recursive(cloned_graph, n, global_visited, dict())

        return cloned_graph


    def _dfs_util_recursive(self, cloned_graph, node, global_visited, local_visited):
        print('working with node %s' % node.val)
        if node.val in global_visited:
            return None

        if node.val in local_visited:
            print('oh no, cycle')
            raise Exception('cycle')

        for _,n in node.neighbors.items():
            cloned_node = Node(n.val)
            existing_node = cloned_graph.nodes[node.val]
            cloned_graph.add_edge(existing_node, cloned_node)

            local_visited[n.val] = True
            self._dfs_util_recursive(cloned_graph, n, global_visited, local_visited)
            local_visited[n.val] = False

        global_visited[node.val] = True

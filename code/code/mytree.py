class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.visited = False

class Traversal:
    POST_ORDER = "POST"
    PRE_ORDER = "PRE"
    INORDER = "IN"

    TYPES = [POST_ORDER, PRE_ORDER, INORDER]
    def __init__(self, type):
        if type not in Traversal.TYPES:
            raise Exception("Unknown type")
        self.type = type

    def pre_order_traverse(self, node):
        traversal_stack = list()
        traversal_stack.append(node)
        while traversal_stack:
            n = traversal_stack.pop()
            print("visited:", n.val)

            if n.right:
                traversal_stack.append(n.right)
            if n.left:
                traversal_stack.append(n.left)

    def in_order_traverse(self, node):
        traversal_stack = list()
        traversal_stack.append(node)

        while traversal_stack:
            n = traversal_stack.pop()
            if not n.left or n.left.visited == True:
                print("visited:", n.val)
                n.visited=True
                if n.right:
                    traversal_stack.append(n.right)
            else:
                traversal_stack.append(n)
                traversal_stack.append(n.left)

    def post_order_trasverse(self, node):
        traversal_stack = list()
        traversal_stack.append(node)

        while traversal_stack:
            n = traversal_stack.pop()
            if not n.left and not n.right:
                print("visited:", n.val)
                n.visited=True
            elif (not n.left or n.left.visited == True) and (not n.right or n.right.visited ==True):
                print("visited:", n.val)
                n.visited=True
            else:
                traversal_stack.append(n)
                if n.right and n.right.visited!=True:
                    traversal_stack.append(n.right)
                if n.left and n.left.visited!=True:
                    traversal_stack.append(n.left)

    def traverse(self, root_node):
        if self.type == self.INORDER:
            self.in_order_traverse(root_node)
        elif self.type == self.POST_ORDER:
            self.post_order_trasverse(root_node)
        else:
            self.pre_order_traverse(root_node)


#tree = Node(1)
#tree.left = Node(2)
#tree.right = Node(3)
#tree.left.left = Node(4)
#tree.left.right = Node(5)
#tree.right.left = Node(6)
#tree.right.right = Node(7)

#print("PRE")
#t = Traversal("PRE")
#t.traverse(tree)

#print("POST")
#t = Traversal("POST")
#t.traverse(tree)

#print("IN")
#t = Traversal("IN")
#t.traverse(tree)

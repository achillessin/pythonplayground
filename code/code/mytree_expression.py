class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


# postfix = tree
def is_operand(str):
    if str.is_digit():
        return True
    return False

def is_operator(str):
    if str in ['+','-','%','*']:
        return True
    return False

def get_next_token(str):
    if str == "" or len(str) == 0:
        return None, None
    return str[0], str[1:]

def convert_postfix(exp):
    if exp == "":
        return None

    holder_stack = list()
    while exp:
        token1, exp = get_next_token(exp)
        n = Node(token1)
        if is_operator(token1):
            l = holder_stack.pop()
            r = holder_stack.pop()
            n.left = l
            n.right = r
        holder_stack.append(n)
    return holder_stack.pop()

# prefix = tree
#function MakeBinaryTree(expr):
#    element = next element in expr
#    if element is a number:
#        return a leaf node of that number
#    else: // element is an operator
#        left = MakeBinaryTree(expr)
#        right = MakeBinaryTree(expr)
#    return a binary tree with subtrees left and right and with operator element

# infix = tree
https://web.iiit.ac.in/~ratnakumat.kvr/assign/ass1.pdf

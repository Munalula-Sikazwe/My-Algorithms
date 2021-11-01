class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


def inorder_traversal(tree, arr):
    if tree is None:
        return
    inorder_traversal(tree.left, arr)
    arr.append(tree.data)
    inorder_traversal(tree.right, arr)


def preorder_traversal(tree, arr):
    if tree is None:
        return
    arr.append(tree.data)
    inorder_traversal(tree.left, arr)
    inorder_traversal(tree.right, arr)


def is_subtree(tree, subtree):
    if subtree is None:
        return True
    if tree is None:
        return False
    tree_array = []
    subtree_array = []
    inorder_traversal(tree, tree_array)
    inorder_traversal(subtree, subtree_array)

    tree_array = "".join(tree_array)
    subtree_array = "".join(subtree_array)

    if subtree_array in tree_array:
        return True
    else:
        return False

main_tree = Node(1)
main_tree.left_node = Node(2)
main_tree.right_node = Node(3)
main_tree.left_node.left_node = Node(4)
main_tree.left_node.right_node = Node(5)
main_tree.right_node.left_node = Node(6)
main_tree.right_node.right_node = Node(7)

sub_tree = Node(3)
sub_tree.left_node = Node(4)
sub_tree.right_node = Node(5)

print(is_subtree(main_tree,sub_tree))
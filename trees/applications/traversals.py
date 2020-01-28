from trees.tree import Tree
from trees.linked_binary_tree import LinkedBinaryTree


def preorder_indent(tree: Tree, position: Tree.Position, depth: int):
    """
    Print preorder representation of subtree of T rooted at p at depth depth
    :param tree: tree
    :param position: root
    :param depth: depth
    """
    print(2 * depth * " ", str(position.element()))
    for c in tree.children(position):
        preorder_indent(tree, c, depth + 1)


def preorder_label(tree: Tree, position: Tree.Position, depth: int, path: [int]):
    """
    Print preorder representation of subtree of T rooted at p at depth depth
    :param tree: tree
    :param position: root
    :param depth: depth
    :param path: a list of ints to represent the path of the position
    """
    label = ".".join([str(j+1) for j in path])
    print(2 * depth * " ", label, str(position.element()))

    path.append(0)
    for c in tree.children(position):
        preorder_label(tree, c, depth + 1, path)
        path[-1] += 1
    path.pop()


def parenthesis(tree: Tree, position: Tree.Position):
    """
    Print parenthesized representation of tree rooted at the position
    :param tree: tree
    :param position: position
    :return:
    """
    print(position.element(), end="")
    if not tree.is_leaf(position):
        first_time = Tree

        for c in tree.children(position):
            if first_time:
                print("(", end="")
            else:
                print(",", end=" ")
            first_time = False
            parenthesis(tree, c)
        print(")", end="")


class File:
    def __init__(self, name: str, size: float):
        self.size = size
        self.name = name

    def __str__(self):
        return f"{self.name}    {self.size}.KB"


def disk_space(tree: Tree, position: Tree.Position):
    """
    :param tree: tree
    :param position: position
    :return: the total disk space for subtree of tree rooted at position
    """
    total = 0
    if tree.is_leaf(position) and isinstance(position.element(), File):
        total = position.element().size
    for c in tree.children(position):
        total += disk_space(tree, c)
    return total


t = LinkedBinaryTree()
root = t._add_root("Data Structure")
left = t._add_left(root, "Tree")
t._add_right(root, "List")

t._add_left(left, "Array Tree")
right = t._add_right(left, "Linked Tree")

t._add_left(right, "Binary Tree")
t._add_right(right, "RB Tree")


# parenthesis(t, root)

disk = LinkedBinaryTree()

root = disk._add_root("C://")
disk._add_left(root, "Pictures")
doc = disk._add_right(root, "Documents")
py = disk._add_left(doc, "Python")
disk._add_right(doc, "Java")
disk._add_left(py, File("tree.py", 3.2))
disk._add_right(py, File("list.py", 1.8))

preorder_indent(disk, root, 0)
space = disk_space(disk, root)
print(f"Total space: {space}KB")

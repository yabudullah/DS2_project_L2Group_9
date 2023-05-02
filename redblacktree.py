class RedBlackTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1  # 0: Black, 1: Red

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = RedBlackTreeNode(key)
            self.root.color = 0
            return

        new_node = RedBlackTreeNode(key)
        current = self.root
        parent = None

        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def search(self, key, node=None):
        if node is None:
            node = self.root

        while node and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return node

    def delete(self, key):
        node = self.search(key)
        if not node:
            return

        self.delete_node(node)

    # Helper methods for Red-Black Tree
    def fix_insert(self, node):
        while node != self.root and node.parent.color == 1:
            if node.parent == self.get_grandparent(node).left:
                uncle = self.get_uncle(node)

                if uncle and uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    self.get_grandparent(node).color = 1
                    node = self.get_grandparent(node)
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = 0
                    self.get_grandparent(node).color = 1
                    self.rotate_right(self.get_grandparent(node))
            else:
                uncle = self.get_uncle(node)

                if uncle and uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    self.get_grandparent(node).color = 1
                    node = self.get_grandparent(node)
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = 0
                    self.get_grandparent(node).color = 1
                    self.rotate_left(self.get_grandparent(node))

        self.root.color = 0

    def rotate_left(self, node):
        y = node.right
        node.right = y.left
        if y.left:
            y.left.parent = node
        y.parent = node.parent
        if not node.parent:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        if x.right:
            x.right.parent = node
        x.parent = node.parent
        if not node.parent:
            self.root = x
        elif node == node.parent.right:
            node.parent.right = x
        else:
            node.parent.left = x
        x.right = node
        node.parent = x

    def get_sibling(self, node):
        if node.parent is None:
            return None
        if node == node.parent.left:
            return node.parent.right
        return node.parent.left

    def get_uncle(self, node):
        if node.parent is None or self.get_grandparent(node) is None:
            return None
        return self.get_sibling(node.parent)

    def get_grandparent(self, node):
        if node.parent is None:
            return None
        return node.parent.parent

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete_node(self, node):
        y = node
        y_original_color = y.color
        if node.left is None:
            x = node.right
            self.transplant(node, node.right)
        elif node.right is None:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                if x:
                    x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == 0:
            self.fix_delete(x)

    def fix_delete(self, x):
        while x is not self.root and (x is None or x.color == 0):
            if x and x == x.parent.left:  # Add a check for x before accessing its attributes
                sibling = x.parent.right
                if sibling is not None and sibling.color == 1:
                    # Case 1: sibling is red
                    sibling.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    sibling = x.parent.right

                # Case 2: both sibling's children are black
                if sibling is None or (
                    (sibling.right is None or sibling.right.color == 0) and
                    (sibling.left is None or sibling.left.color == 0)
                ):
                    if sibling is not None:
                        sibling.color = 1
                    x = x.parent
                else:
                    # Case 3: sibling's right child is black
                    if sibling.right is None or sibling.right.color == 0:
                        if sibling.left is not None:
                            sibling.left.color = 0
                        sibling.color = 1
                        self.right_rotate(sibling)
                        sibling = x.parent.right

                    # Case 4: sibling's left child is black
                    sibling.color = x.parent.color
                    x.parent.color = 0
                    if sibling.right is not None:
                        sibling.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                if x:  # Add a check for x before accessing its attributes
                    sibling = x.parent.left
                else:
                    sibling = None
                    
                if sibling is not None and sibling.color == 1:
                    # Case 1: sibling is red
                    sibling.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    sibling = x.parent.left

                # Case 2: both sibling's children are black
                if sibling is None or (
                    (sibling.left is None or sibling.left.color == 0) and
                    (sibling.right is None or sibling.right.color == 0)
                ):
                    if sibling is not None:
                        sibling.color = 1
                    x = x.parent
                else:
                    # Case 3: sibling's left child is black
                    if sibling.left is None or sibling.left.color == 0:
                        if sibling.right is not None:
                            sibling.right.color = 0
                        sibling.color = 1
                        self.left_rotate(sibling)
                        sibling = x.parent.left

                    # Case 4: sibling's right child is black
                    sibling.color = x.parent.color
                    x.parent.color = 0
                    if sibling.left is not None:
                        sibling.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        if x is not None:
            x.color = 0


    def minimum(self, node):
        while node.left:
            node = node.left
        return node
    
# Test calls for Red-Black Tree
rb_tree = RedBlackTree()

# values_to_insert = [10, 20, 30, 40, 50]
# values_to_search = [10, 20, 30, 40, 50, 60]
# values_to_delete = [20, 30, 40]

#Testcase for n = 1000
# values_to_insert = [895, 886, 624, 97, 354, 61, 293, 725, 267, 956, 250, 688, 231, 584, 186, 352, 327, 791, 544, 424, 91, 774, 468, 926, 539, 891, 543, 408, 384, 45, 451, 402, 642, 817, 253, 463, 127, 864, 424, 140, 715, 150, 173, 530, 289, 899, 845, 171, 258, 510, 151, 187, 296, 527, 94, 327, 298, 985, 998, 540, 617, 458, 413, 632, 868, 144, 114, 270, 547, 342, 532, 191, 904, 768, 639, 791, 873, 205, 883, 571, 168, 166, 335, 593, 447, 877, 699, 914, 168, 717, 639, 786, 299, 291, 32, 417, 546, 484, 10, 319, 328, 862, 177]
# values_to_search = [895, 886, 624, 97, 354, 61, 293, 725, 267, 956, 250, 688, 231, 584, 186, 352, 327, 791, 544, 424, 91, 774, 468, 926, 539, 891, 543, 408, 384, 45, 451, 402, 642, 817, 253, 463, 127, 864, 424, 140, 715, 150, 173, 530, 289, 899, 845, 171, 258, 510, 151, 187, 296, 527, 94, 327, 298, 985, 998, 540, 617, 458, 413, 632, 868, 144, 114, 270, 547, 342, 532, 191, 904, 768, 639, 791, 873, 205, 883, 571, 168, 166, 335, 593, 447, 877, 699, 914, 168, 717, 639, 786, 299, 291, 32, 417, 546, 484, 10, 319, 328, 862, 177, 1000]
# values_to_delete = [191, 332, 639]

# # Insert values
# for value in values_to_insert:
#     rb_tree.insert(value)

# # Search for values
# for value in values_to_search:
#     found = rb_tree.search(value)
#     print(f"Value {value} found in Red-Black Tree: {found}")

# # Delete values
# for value in values_to_delete:
#     rb_tree.delete(value)
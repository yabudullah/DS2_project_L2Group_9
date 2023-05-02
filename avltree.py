class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, key, root):
        if root is None:
            return AVLTreeNode(key)

        if key < root.key:
            root.left = self.insert(key, root.left)
        else:
            root.right = self.insert(key, root.right)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, key, root=None):
        if not root:
            return None

        if key == root.key:
            return root

        if key < root.key:
            return self.search(key, root.left)

        return self.search(key, root.right)

    def delete(self, key, root):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(key, root.left)
        elif key > root.key:
            root.right = self.delete(key, root.right)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(temp.key, root.right)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        if z is None:
            return z
        
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, y):
        if y is None:
            return y

        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x


    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root

        return self.get_min_value_node(root.left)

# Test calls for AVL Tree
# avl_tree = AVLTree()
# root = None

# values_to_insert = [10, 20, 30, 40, 50]
# values_to_search = [10, 20, 30, 40, 50, 60]
# values_to_delete = [20, 30, 40]

# #Testcase for n = 1000
# values_to_insert = [895, 886, 624, 97, 354, 61, 293, 725, 267, 956, 250, 688, 231, 584, 186, 352, 327, 791, 544, 424, 91, 774, 468, 926, 539, 891, 543, 408, 384, 45, 451, 402, 642, 817, 253, 463, 127, 864, 424, 140, 715, 150, 173, 530, 289, 899, 845, 171, 258, 510, 151, 187, 296, 527, 94, 327, 298, 985, 998, 540, 617, 458, 413, 632, 868, 144, 114, 270, 547, 342, 532, 191, 904, 768, 639, 791, 873, 205, 883, 571, 168, 166, 335, 593, 447, 877, 699, 914, 168, 717, 639, 786, 299, 291, 32, 417, 546, 484, 10, 319, 328, 862, 177]
# values_to_search = [895, 886, 624, 97, 354, 61, 293, 725, 267, 956, 250, 688, 231, 584, 186, 352, 327, 791, 544, 424, 91, 774, 468, 926, 539, 891, 543, 408, 384, 45, 451, 402, 642, 817, 253, 463, 127, 864, 424, 140, 715, 150, 173, 530, 289, 899, 845, 171, 258, 510, 151, 187, 296, 527, 94, 327, 298, 985, 998, 540, 617, 458, 413, 632, 868, 144, 114, 270, 547, 342, 532, 191, 904, 768, 639, 791, 873, 205, 883, 571, 168, 166, 335, 593, 447, 877, 699, 914, 168, 717, 639, 786, 299, 291, 32, 417, 546, 484, 10, 319, 328, 862, 177, 1000]
# values_to_delete = [191, 332, 639]

# # Insert values
# for value in values_to_insert:
#     root = avl_tree.insert(value, root)

# # Search for values
# for value in values_to_search:
#     found = avl_tree.search(value, root)
#     print(f"Value {value} found in AVL Tree: {found}")

# # Delete values
# for value in values_to_delete:
#     root = avl_tree.delete(value, root)
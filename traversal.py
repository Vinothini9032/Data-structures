from typing import List, Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Traversal:
    def __init__(self):
        self.pre = 0   # pointer for preorder
    
    def buildTreeFromInPre(self, inorder: List[int], preorder: List[int]) -> Optional[Node]:
        inorder_map = {val: i for i, val in enumerate(inorder)}  # value → index map

        def helper(left, right):
            if left > right:
                return None

            # Take current root from preorder
            root_val = preorder[self.pre]
            self.pre += 1
            root = Node(root_val)

            # Find index in inorder
            index = inorder_map[root_val]

            # Build left & right subtrees
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root

        return helper(0, len(inorder) - 1)

    # ---------------- Traversal wrappers ----------------
    def inorderTraversal(self, root: Optional[Node]) -> List[int]:
        return self._inorder(root, [])

    def preorderTrav(self, root: Optional[Node]) -> List[int]:
        return self._preorder(root, [])

    def postorderTrav(self, root: Optional[Node]) -> List[int]:
        return self._postorder(root, [])

    # ---------------- Recursive helpers ----------------
    def _inorder(self, node, result):
        if not node: return result
        self._inorder(node.left, result)   # ✅ call helper
        result.append(node.data)
        self._inorder(node.right, result)  # ✅ call helper
        return result

    def _preorder(self, node, result):
        if not node: return result
        result.append(node.data)
        self._preorder(node.left, result)   # ✅ call helper
        self._preorder(node.right, result)  # ✅ call helper
        return result

    def _postorder(self, node, result):
        if not node: return result
        self._postorder(node.left, result)   # ✅ call helper
        self._postorder(node.right, result)  # ✅ call helper
        result.append(node.data)
        return result


# ---------------- Test Example ----------------
inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]

sol = Traversal()
root = sol.buildTreeFromInPre(inorder, preorder)

print("Inorder:  ", sol.inorderTraversal(root)) 
print("Preorder: ", sol.preorderTrav(root))
print("Postorder:", sol.postorderTrav(root))

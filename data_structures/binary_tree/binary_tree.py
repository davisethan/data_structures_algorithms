class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        values = []
        self.dfs(self, values)
        return str(values)

    def dfs(self, root, values):
        if root is None:
            return
        values.append(root.data)
        self.dfs(root.left, values)
        self.dfs(root.right, values)

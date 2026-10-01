class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

class Arbol:
    def __init__(self):
        self.root = None

    def buscarElementosBst(self,key):
        actual = self.root
        while actual is not None:
            if key == actual.key:
                return actual
            actual = actual.left if key < actual.key else actual.right
        return None

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):

        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:

            # No tiene hijos
            if node.left is None and node.right is None:
                return None

            # Solo tiene hijo derecho
            if node.left is None:
                return node.right

            # Solo tiene hijo izquierdo
            if node.right is None:
                return node.left

            # Tiene dos hijos
            sucesor = node.right

            while sucesor.left is not None:
                sucesor = sucesor.left

            node.key = sucesor.key

            node.right = self._delete(node.right, sucesor.key)

        return node


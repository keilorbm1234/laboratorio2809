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

    def insertar(self, key):
        self.root = self._insertar(self.root, key)

    def _insertar(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insertar(node.left, key)
        elif key > node.key:
            node.right = self._insertar(node.right, key)

        return node
    def esBST(self, nodo=None) -> bool:  # Recibe root porque eso pide el lab
        if nodo is None:
            root = self.root
        else:
            root = nodo

        # Le ponemos valores grandes por defecto al iniciar
        return self._esBST(root, -9999, 9999)
    def _esBST(self, root, min, max) -> bool:
        if root is None:
            return True

        if root.key is None or not (min < root.key < max):
            return False

        else:
            return self._esBST(root.left,min,root.key) and self._esBST(root.right,root.key,max)


    # extra - imprimir
    def print_tree(self):
        """Print the tree structure in a readable format."""
        self._print_tree(" ", self.root, False)

    def _print_tree(self, p, r, is_left):
        if r:
            print(p, end='')
            if is_left:
                print("|--", end='')
                s = "|    "
            else:
                print("'--", end='')
                s = "    "
            print(r.key)
            self._print_tree(p + s, r.left, True)
            self._print_tree(p + s, r.right, False)
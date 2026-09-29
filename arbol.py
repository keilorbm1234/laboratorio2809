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

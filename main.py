from arbol import Arbol, Node

arbolito = Arbol()

arbolito.root = Node(50)

arbolito.root.left = Node(30)
arbolito.root.right = Node(70)

arbolito.root.left.left = Node(20)
arbolito.root.left.right = Node(40)

arbolito.root.right.left = Node(60)
arbolito.root.right.right = Node(80)

resultado = arbolito.buscarElementosBst(40)

if resultado is not None:
    print("Encontrado:", resultado.key)
else:
    print("No encontrado")

arbolito.delete(40)

resultado = arbolito.buscarElementosBst(40)

if resultado is not None:
    print("40 todavía existe")
else:
    print("40 fue eliminado")


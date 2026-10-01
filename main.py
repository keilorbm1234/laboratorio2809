from arbol import Arbol

arbol = Arbol()

# Insertar un valor en el arbol
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

arbol.print_tree()

# Borrar un valor del arbol
arbol.delete(30)

resultado = arbol.buscarElementosBst(30)

if resultado is not None:
    print("El elemento 30 sigue en el árbol")
else:
    print("El elemento 30 fue eliminado")

arbol.print_tree()

# Buscar un valor del arbol
resultado = arbol.buscarElementosBst(40)

if resultado is not None:
    print("Elemento encontrado:", resultado.key)
else:
    print("Elemento no encontrado")

resultado = arbol.buscarElementosBst(90)

if resultado is not None:
    print("Elemento encontrado:", resultado.key)
else:
    print("Elemento no encontrado")

# Un método que reciba un nodo a la raíz de un árbol y determine si es BST o no
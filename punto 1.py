import binary_tree as bt
tree = bt.BinaryTree(bt.BinaryTree.Node(1))
tree.add_node(2, 1)
tree.add_node(3, 1)
tree.add_node(4, 2)
tree.add_node(5, 2)
tree.add_node(6, 3)
tree.add_node(7, 4)
"""""
Árbol inicial:
             1
           /   \
          /     \
         2       3
        / \     /
       4   5   6
      /
     7
"""""
tree.add_node(8, 7)
tree.transversal(tree.root, [])
print()
print("El abuelo es:",tree.find_grandfather(tree.return_node(4)))
print("El tío es:", tree.find_uncle(tree.return_node(6)))

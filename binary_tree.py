import sys

class BinaryTree:
    class Node:
        def __init__(self, data: int, right = None, left = None) -> None:
            self.data = data
            self.right = right
            self.left = left
        
        def __str__(self) -> str:
            return str(self.data)

    def __init__(self, root: Node) -> None:
        self.root = root
    
    #Este método añade un nodo con valor data como hijo de un nodo cuyo valor sea where.
    #Si el nodo cuyo valor es where está libre a la izquierda, se añadirá el nuevo nodo a la izquierda.
    #Si no es el caso, entonces se añadirá el nuevo nodo a la derecha.
    #Si el nodo ya tiene dos hijos, entonces no se podrá agregar el valor
    def add_node(self, data: int, where: int) -> None:
        node = self.return_node(where)
        if node:
            if node.left == None:
                node.left = self.Node(data)
            elif node.right == None:
                node.right = self.Node(data)
            else:
                print("Este nodo ya tiene dos hijos")
            self.balance()
        else:
            print("El nodo no fue encontrado")

    def delete_node(self, where: int) -> None:
        #Primero se verifica el caso en el que
        #el nodo a eliminar sea la raíz del árbol
        if where == self.root.data:
            #Si es así, la raíz pasa a ser el hijo izquierdo
            #en caso de que exista
            #y el hijo derecho pasa abajo del todo
            if self.root.left != None:
                temp = self.root
                self.root = self.root.left
                if self.root.right == None:
                    self.root.right = temp.right
                else:
                    leaf = self.root.right
                    while leaf.left != None:
                        leaf = leaf.left
                    leaf.left = temp.right
            #En el otro caso contrario, la raíz pasa a ser 
            #el hijo derecho
            else:
                self.root = self.root.right
            return
        #Se busca el nodo que se desea borrar
        node = self.return_node(where)
        if node:
            #Si lo encuentra, se buscará el nodo padre por medio de un recorrido
            #por nivel.
            temp = self.father(node)
            if temp.left == node:
                #Si el nodo a eliminar está a la izquierda, entonces, se subirá el hijo
                #izquierdo en caso de que este no sea nulo#
                if node.left != None:
                    temp.left = node.left
                    #Si el hijo derecho del nodo que reemplazó al eliminado
                    #es nulo, entonces se le coloca como hijo derecho
                    #el nodo que ya se encontraba en esa posición
                    if temp.left.right == None:
                        temp.left.right = node.right
                    #Si el hijo derecho ya existe, entonces el antiguo hijo derecho
                    #pasará a ser el hijo izquierdo de la hoja izquierda del subárbol
                    #cuya raíz es el hijo derecho del nodo que reemplazó al nodo eliminado
                    else:
                        leaf = temp.left.right
                        while leaf.left != None:
                            leaf = leaf.left
                        leaf.left = node.right
                    #Si el nodo no tenía hijo izquierdo, entonces se reemplaza el nodo
                    #por su hijo derecho
                else:
                    temp.left = node.right
            #Se procede de forma análoga en caso de que el nodo a elminar esté a la derecha
            else:
                if node.left != None:
                    temp.right = node.left
                    if temp.right.right == None:
                        temp.right.right = node.right
                    else:
                        leaf = temp.right.right
                        while leaf.left != None:
                            leaf = leaf.left
                        leaf.left = node.right
                else:
                    temp.right = node.right
            self.balance()
        else:
            print("El nodo no fue encontrado")

    #Para encontrar el padre de un nodo
    #Recorremos por nivel hasta encontrar un nodo
    #cuyo hijo sea el nodo que se busca
    def father(self, node: Node) -> Node:
        q = []
        q.append(self.root)
        while q != []:
            temp = q.pop(0)
            if temp.left == node or temp.right == node:
                return temp
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)

    #Se obtiene la altura de un nodo del árbol de forma recursiva
    def get_height(self, node) -> int:
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def left_rotation(self, data: int) -> None:
        node = self.return_node(data)
        if node:
            if node.left == None:
                return
            father = self.father(node)
            temp = node
            if father.left == node:
                father.left = node.left
                father.left.right = temp
            else:
                father.right = node.left
                father.right.right = temp
            temp.left = None
    
    def right_rotation(self, data: int) -> None:
        node = self.return_node(data)
        if node:
            if node.right == None:
                return
            father = self.father(node)
            temp = node
            if father.left == node:
                father.left = node.right
                father.left.left = temp
            else:
                father.right = node.right
                father.right.left = temp
            temp.right = None

    def double_left_rotation(self, data: int) -> None:
        node = self.return_node(data)
        if node:
            if node.left == None:
                print("No se puede realizar la doble rotación izquierda")
                return
            self.right_rotation(node.left.data)
            self.left_rotation(node.data)
    
    def double_right_rotation(self, data: int) -> None:
        node = self.return_node(data)
        if node:
            if node.right == None:
                print("No se puede realizar la doble rotación derecha")
                return
            self.left_rotation(node.right.data)
            self.right_rotation(node.data)

    def balance(self) -> None:
        node = self.root
        while abs(self.get_height(node.left)-self.get_height(node.right))> 3:
            if self.get_height(node.right) - self.get_height(node.left) < -1:
                node = node.left
            elif self.get_height(node.right) - self.get_height(node.left) > 1:
                node = node.right   

        if self.get_height(node.left) > self.get_height(node.right):
            self.left_rotation(node.data)      

        elif self.get_height(node.right) > self.get_height(node.left):
            self.right_rotation(node.data)
        
        else:
            if node.left:
                pass
        

    def preorden(self, node: Node) -> None:
        if node == None:
            return
        print(node.data, end=" ")
        self.preorden(node.left)
        self.preorden(node.right)
    
    #Se busca un nodo de a partir del elemento data, recorriendo el árbol
    #por nivel.
    def return_node(self, data: int) -> Node:
        q = []
        q.append(self.root)
        while q != []:
            temp = q.pop(0)
            if temp.data == data: 
                return temp
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)
    
    def transversal(self, node: Node, q) -> None:
        #Se verifica el caso el que estemos en la raíz
        if node == self.root and q == []:
            print(node.data, end=" ")
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
            self.transversal(node, q)
        #Luego, se procede de forma casi análoga
        #al caso no recursivo
        elif q != []:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left != None:
                q.append(node.left)

            if node.right != None:
                q.append(node.right)
            self.transversal(node, q)
    
    #Hallamos el abuelo apoyandonos en el método para hallar el padre
    def find_grandfather(self, node: Node):
        if (self.root == node or self.root.left == node
            or self.root.right == node):
            return("Este nodo no tiene abuelo")
        else:
            return(self.father(self.father(node)))
    
    #Hallamos el tío apoyandonos en el método para hallar al abuelo
    def find_uncle(self, node: Node):
        if (self.root == node or self.root.left == node
            or self.root.right == node):
            return("Este nodo no tiene tío")
        else:
            #Si el padre del nodo que se busca, es el izquierdo del abuelo
            #entonces el tío es el derecho si existe
            grandfather = self.find_grandfather(node)
            if grandfather.left:
                if grandfather.left.left == node \
                    or grandfather.left.right == node:
                    if grandfather.right:
                        return grandfather.right
                    else:
                        return "Este nodo no tiene tío"

            #Si el padre del nodo que se busca, es el derecho del abuelo
            #entonces el tío es el izquierdo si existe
            if grandfather.right:
                if grandfather.right.left == node \
                    or grandfather.right.right == node:
                    if grandfather.left:
                        return grandfather.left
                    else:
                        return "Este nodo no tiene tío"

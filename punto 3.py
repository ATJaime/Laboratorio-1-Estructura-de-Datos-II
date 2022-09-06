#El problema a resolver es encontrar el máximo común divisor de n números enteros positivos, 
# partiendo de un árbol B+ que, en el primer nivel tiene como raíz 1, en el segundo nivel
#los números a los que hallaremos el mcd y en el tercer nivel los divisores de cada número.

#Se crea la clase de árboles B+
class BpTree:
    class Node:
        def __init__(self, value: int, links = []) -> None:
            self.value = value
            self.links = links
            #Como puede tener múltiples nodos, los links son una lista

        def __str__(self) -> str:
            return str(self.value)

    def __init__(self, root = Node(1)) -> None:
        self.root = root
    
    #Se agregan los números a los que vamos a sacar el mcd y sus divisores 
    def add_nodes(self, value: int) -> None:
        divisores = self.divisores(value)
        q = []
        for d in divisores:
            n = self.Node(d)
            q.append(n)
        self.root.links.append(self.Node(value, q))
        
    #Se hallan los divisores del valor ingresado
    def divisores(self, value: int):
        divisores = []
        for i in range(1, value+1):
            if value%i == 0:
                divisores.append(i)
        return divisores
    
    #Se obtiene la interesección entre los divisores y se retorna el máximo de ellos
    def find_mcd(self) -> int:
        ndiv = set()
        n = self.root.links[0]
        for d in n.links:
            ndiv.add(d.value)
        for m in self.root.links:
            mdiv = set()
            for k in m.links:
                mdiv.add(k.value)
            ndiv = ndiv.intersection(mdiv)
        return max(ndiv)

tree = BpTree()

n = int(input("¿A cuántos números quiere hallar el mcd? "))

for i in range(0, n):
    m = int(input("Ingrese número "))
    tree.add_nodes(m)

print("El mcd entre los números es",tree.find_mcd())
class Node(object):
    def __init__(self, node):
        self.node = node
        self.child = []

    def add_child(self, par_node):
        self.child.append(par_node)



n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')
n1.add_child(n2)
n1.add_child(n3)
n1.add_child(n4)
n2.add_child(n5)
n2.add_child(n6)

for i in n1.child:
    print(i.node)

print("---------------------")

for j in n2.child:
    print(j.node)
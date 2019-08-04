# 4th August,2019


class Node(object):
    def __init__(self, data):
        self.nexval = None
        self.data = data
        self.preval = None


class ListOperations(object):
    def __init__(self):
        self.head = None

    def append_node(self, node):
        if self.head is None:
            self.head = node
        else:
            temp_iter = self.head
            while temp_iter.nexval is not None:
                temp_iter = temp_iter.nexval
            temp_iter.nexval = node
            node.preval = temp_iter

    def traversing(self):
        if self.head is None:
            print("****** No Data Available ********")
        else:
            temp_iter = self.head
            count = 0
            while temp_iter is not None:
                count+=1
                print('{0} Node Data : {1} '.format(count,temp_iter.data))
                temp_iter = temp_iter.nexval


obj = ListOperations()
num = int(input("How many Nodes : "))
for i in range(num):
    obj.append_node(Node(input("Enter Data : ")))
obj.traversing()
# 30-07-2019 Linked List Basic Syntax

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nexval = None


class ListOperations(object):
    def __init__(self):
        self.head = None

    def append_list(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp_iter = self.head
            while temp_iter.nexval is not None:
                temp_iter = temp_iter.nexval
            temp_iter.nexval = Node(data)

    def insert_at_beg(self, node):
        temp_data = self.head
        self.head = node
        node.nexval = temp_data

    def insert_in_mid(self, comp_data, node):
        if self.head is None :
            print("*********** No Data Available ***********")
        else:
            count = 0
            prev_ele = curr_ele = self.head
            while curr_ele is not None:
                count+=1
                if curr_ele.data == comp_data:
                    if count == 1:
                        self.insert_at_beg(node)
                    else:
                        node.nexval = curr_ele
                        prev_ele.nexval = node
                    break
                prev_ele = curr_ele
                curr_ele = curr_ele.nexval
            else:
                print("*********** No Data Available ***********")

    def traversing(self):
        temp = self.head
        count = 1
        if temp is None:
            print("*********** No Data Available ***********")
        else:
            while temp is not None:
                print("{0} Node Data : {1}".format(count, temp.data))
                temp = temp.nexval
                count += 1


obj = ListOperations()
for i in range(int(input("Enter Number of Nodes : "))):
    print("Enter {0} node Data".format(i + 1))
    obj.append_list(input())
response = input("Want to do Operations - y or n : ")
while response.lower() == 'y':
    res = input("Insertion or Deletion - i or d : ")
    if res == 'i':
        data = input("Enter Data : ")
        num = int(input("Press 1 - Insertion in Beg , Press 2 - Insertion in mid, Press 3 -Insertion in end : "))
        if num == 1:
            obj.insert_at_beg(Node(data))
        elif num == 2:
            comp_data = input("Enter comparable element : ")
            obj.insert_in_mid(comp_data,Node(data))
        else:
            obj.append_list(Node(data))
    response = input("Want to do more operations ? y or n : ")

obj.traversing()

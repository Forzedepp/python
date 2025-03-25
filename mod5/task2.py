class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start:
            self.start.pref = None
        else:
            self.end = None
        return val

    def insert(self, n, val):
        if n < 1:
            return
        current = self.start
        count = 0
        while current and count < n - 1:
            current = current.nref
            count += 1
        if not current:
            return
        new_node = Node(val)
        new_node.pref = current
        new_node.nref = current.nref
        if current.nref:
            current.nref.pref = new_node
        current.nref = new_node
        if new_node.nref is None:
            self.end = new_node

    def print(self):
        current = self.start
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.nref
        print(' '.join(elements))
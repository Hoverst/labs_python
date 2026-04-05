class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class BinaryTreePriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
        else:
            self._insert_recursive(self.root, value, priority)

    def _insert_recursive(self, current_node, value, priority):
        if priority >= current_node.priority:
            if current_node.left is None:
                current_node.left = Node(value, priority)
            else:
                self._insert_recursive(current_node.left, value, priority)
        else:
            if current_node.right is None:
                current_node.right = Node(value, priority)
            else:
                self._insert_recursive(current_node.right, value, priority)

    def pop(self):
        if self.root is None:
            raise IndexError("Empty queue")

        parent = None
        current = self.root

        while current.left is not None:
            parent = current
            current = current.left

        if parent is None:
            self.root = current.right
        else:
            parent.left = current.right

        return current.value, current.priority

    def peek(self):
        if self.root is None:
            raise IndexError("Empty queue")

        current = self.root
        while current.left is not None:
            current = current.left

        return current.value, current.priority

    def view_all(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        return elements

    def _in_order_traversal(self, node, elements):
        if node is not None:
            self._in_order_traversal(node.left, elements)
            elements.append((node.value, node.priority))
            self._in_order_traversal(node.right, elements)
 

if __name__ == "__main__":
    pq = BinaryTreePriorityQueue()

    pq.insert("A", 1)
    pq.insert("B", 10)
    pq.insert("C", 5)
    pq.insert("D", 15)
    pq.insert("E", 10) 

    for val, prio in pq.view_all():
        print(f"{prio}: {val}")

    print(pq.peek())

    # while pq.root is not None:
    #     print(pq.pop())
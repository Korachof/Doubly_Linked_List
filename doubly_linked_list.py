class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Print the value of each Node of the Linked List
        :return: None
        """
        temp_node = self.head

        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next

    def append(self, value):
        """
        Append a node with the given value to the DLL
        :param value: The value of the Node to be appended
        :return: True if the Node is successfully appended.
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        """
        Removes the last node of the DLL
        :return: Node Object that was removed
        """
        if self.length == 0:
            return None

        remove_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = None
            remove_node.prev = None

        self.length -= 1
        return remove_node

    def prepend(self, value):
        """
        Add a node with the given value to the front of the DLL
        :param value: The value of the Node to be prepended
        :return: True when the Node is successfully prepend
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        """
        Removes the first Node in the DLL
        :return: The Node that was removed, or None if no Node is found.
        """
        if self.length == 0:
            return None

        remove_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None
            remove_node.next = None

        self.length -= 1
        return remove_node

    def get(self, index):
        """
        Get the value of the Node at the specified index
        :param index: The index of the Node to be found
        :return: The node at the specified index
        """
        if index < 0 or index >= self.length:
            return None

        get_node = self.head

        if index < self.length / 2:
            for _ in range(index):
                get_node = get_node.next

        else:
            get_node = self.tail
            for _ in range(self.length - 1, index, - 1):
                get_node = get_node.prev

        return get_node

    def set_value(self, index, value):
        """
        Set the value of the Node at the specified index to the given value.
        :param index: The index of the Node to be changed
        :param value: The new value of the Node
        :return: Bool (True if the Node at the index is found and successfully changed, False otherwise)
        """
        set_node = self.get(index)

        if set_node:
            set_node.value = value
            return True

        return False

    def insert(self, index, value):
        """
        Insert a new Node with the given Value at the given index
        :param index: Index where the new Node will be inserted
        :param value: Value of the new Node
        :return: Bool (True if successfully inserted, False otherwise)
        """
        new_node = Node(value)

        if index < 0 or index > self.length:
            return False

        if index == self.length:
            return self.append(value)

        elif index == 0:
            return self.prepend(value)

        get_node = self.get(index)

        if get_node:
            get_node.prev.next = new_node
            new_node.next = get_node
            new_node.prev = get_node.prev
            get_node.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        """
        Remove the Node at the given index
        :param index: The index of the node to be removed
        :return: The removed Node
        """
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        elif index == self.length - 1:
            return self.pop()

        remove_node = self.get(index)

        if remove_node:
            remove_node.prev.next = remove_node.next
            remove_node.next.prev = remove_node.prev
            remove_node.next = None
            remove_node.prev = None

        self.length -= 1
        return remove_node
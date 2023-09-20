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
        temp_node = self.head

        while temp_node:
            print(temp_node.value )
            temp_node = temp_node.next

    def append(self, value):
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
        set_node = self.get(index)

        if set_node:
            set_node.value = value
            return True

        return False

    def insert(self, index, value):
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
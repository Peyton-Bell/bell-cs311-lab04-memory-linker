"""
Lab 4: The Memory Linker -- starter.

Complete DoublyLinkedList below. See the assignment,
Part B, for the full requirements. No node may ever become
unreachable from `head` after any sequence of operations.
"""

from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    __slots__ = ("value", "prev", "next")

    def __init__(self, value: T) -> None:
        self.value = value
        self.prev: Optional["_Node[T]"] = None
        self.next: Optional["_Node[T]"] = None


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[_Node[T]] = None
        self.tail: Optional[_Node[T]] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def insert_front(self, value: T) -> None:
        new_node = _Node(value)
        if self.head is None:
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def insert_back(self, value: T) -> None:
        new_node = _Node(value)
        if self.head is None:
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1



    def delete(self, value: T) -> bool:
        """Remove the first node matching `value`. Return True if removed, False if not found."""
        current_node = self.head
        while current_node is not None and current_node.value != value:
            current_node = current_node.next

        if current_node is None:
            return False
        elif current_node == self.head and current_node == self.tail:
            self.head = None
            self.tail = None
        elif current_node == self.head:
            self.head = current_node.next
            self.head.prev = None
        elif current_node == self.tail:
            self.tail = current_node.prev
            self.tail.next = None
        else:
            current_node.next.prev = current_node.prev
            current_node.prev.next = current_node.next
            current_node.next = None
            current_node.prev = None
        self._size -= 1
        return True
        
            


    def reverse(self) -> None:
        """Reverse the list in place."""
        current_node = self.head
        while current_node is not None:
            current_node.prev, current_node.next = current_node.next, current_node.prev
            current_node = current_node.prev
        self.head, self.tail = self.tail, self.head

    def insert(self, index: int, value: T) -> None:
        """
        Insert `value` so it becomes the element at `index` (0 through
        len(self), inclusive). Traverse from whichever end is closer to
        `index` to minimize steps.
        """
        new_node = _Node(value)


        if len(self) == index:
            self.insert_back(value)
        elif index == 0:
            self.insert_front(value)

        elif index >= len(self) / 2:
            #start at tail
            current_node = self.tail
            for i in range((len(self) - 1) - index):
                current_node = current_node.prev
            new_node.next = current_node
            new_node.prev = current_node.prev
            current_node.prev.next = new_node
            current_node.prev = new_node
            self._size += 1
        else:
            #start at head
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            new_node.next = current_node
            new_node.prev = current_node.prev
            current_node.prev.next = new_node
            current_node.prev = new_node
            self._size += 1


    def delete_at(self, index: int) -> T:
        """Remove and return the value at `index`. Raise IndexError if out of range."""
        if index < 0 or index > (len(self) - 1):
            raise IndexError("index is out of range")
        
        elif index >= len(self) / 2:
            #start at tail
            current_node = self.tail
            for i in range((len(self) - 1) - index):
                current_node = current_node.prev

            if current_node == self.head and current_node == self.tail:
                self.head = None
                self.tail = None
            elif current_node == self.head:
                self.head = current_node.next
                self.head.prev = None
            elif current_node == self.tail:
                self.tail = current_node.prev
                self.tail.next = None
            else:
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                current_node.next = None
                current_node.prev = None
            self._size -= 1
            return current_node.value
            
        else:
            #start at head
            current_node = self.head
            for i in range(index):
                current_node = current_node.next

            if current_node == self.head and current_node == self.tail:
                self.head = None
                self.tail = None
            elif current_node == self.head:
                self.head = current_node.next
                self.head.prev = None
            elif current_node == self.tail:
                self.tail = current_node.prev
                self.tail.next = None
            else:
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                current_node.next = None
                current_node.prev = None
            self._size -= 1
            return current_node.value

    def __iter__(self) -> Iterator[T]:
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

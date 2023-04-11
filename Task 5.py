class Unit:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        unit = self.first
        string = ''
        while unit:
            string += str(unit) + ' '
            unit = unit.next
        return string

    def push(self, new_value):
        new_unit = Unit(new_value)
        if self.last is None:
            self.last = new_unit
            self.first = new_unit
        else:
            self.last.next = new_unit
            temp = self.last
            self.last = new_unit
            self.last.prev = temp

    def pop(self):
        if self.first is None or self.last is None:
            return
        else:
            self.last = self.last.prev
            self.last.next = None

    def unshift(self, new_value):
        new_unit = Unit(new_value)
        if self.first is None:
            self.first = new_unit
            self.last = new_unit
        else:
            self.first.prev = new_unit
            temp = self.first
            self.first = new_unit
            self.first.next = temp

    def shift(self):
        if self.first is None or self.last is None:
            return
        else:
            self.first = self.first.next


D = DoublyLinkedList()

D.push(1)
D.push(4)
D.pop()
D.unshift(11)
D.unshift(12)
D.shift()
D.push(2)
D.push(5)

print(D)

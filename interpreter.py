from enum import Enum

class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Type(Enum):
    INT = 1
    SHORT = 2
    LONG = 3
    DOUBLE = 4
    CHAR = 5
    FLOAT = 6
    ENUM = 7
    STRUCT = 8
    UNION = 9
    VOID = 10


class Variable:
    def __init__(self, name: str, signed: bool, constant: bool, type: Type, array: bool, ptr: bool, value = None):
        self.name = name
        self.signed = signed
        self.constant = constant
        self.type = type
        self.array = array
        self.ptr = ptr
        self.assigned = False
        self.value = Variable.assign(value)

    def assign(self, value):
        if self.constant and self.assigned: 
            raise Exception("cannot reassign value of a constant")
        match self.type:
            case Type.INT:
                pass
            case Type.SHORT:
                pass
            case Type.LONG:
                pass
            case Type.DOUBLE:
                pass
            case Type.CHAR:
                pass
            case Type.FLOAT:
                pass
            case Type.ENUM:
                pass
            case Type.STRUCT:
                pass
            case Type.UNION:
                pass
            case Type.VOID:
                pass

        self.value = value
        self.assigned = True

variables = Stack() # dictionary keys map to variable class object
typedefs = Stack()

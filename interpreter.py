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
        value_length = len(value)
        match self.type:
            case Type.INT:
                self.value = int(value)
            case Type.SHORT:
                self.value = int(value)
            case Type.LONG:
                self.value = int(value)
            case Type.DOUBLE:
                self.value = float(value)
            case Type.FLOAT:
                self.value = float(value)
            case Type.CHAR:
                escape = '\\' in value
                if (not escape and value_length != 3) or (escape and value_length != 4):
                    raise Exception("invalid character: {}".format(value))
                self.value = value
            case Type.ENUM:
                pass
            case Type.STRUCT:
                pass
            case Type.UNION:
                pass
            case Type.VOID:
                self.value = value

        self.assigned = True

variables = Stack() # dictionary keys map to variable class object
typedefs = Stack()

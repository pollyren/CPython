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
    DOUBLE = 2
    CHAR = 3
    STRUCT = 4
    ENUM = 5
    UNION = 6
    VOID = 7

NUMERIC_TYPE = [Type.INT, Type.DOUBLE]

class Value:
    def __init__(self, ptr: bool, ptr_depth: int, signed: bool, tag: Type, value):
        self.ptr = ptr
        self.ptr_depth = ptr_depth
        self.tag = tag
        self.value = value

class Variable:
    def __init__(self, name: str, signed: bool, constant: bool, type: Type, ptr: bool, value=None):
        self.name = name
        self.signed = signed
        self.constant = constant
        self.type = type
        self.ptr = ptr
        self.assigned = False
        self.value = Variable.assign(value)
        # push variable onto the stack somehow

    def assign(self, value):
        if value is None: return
        if self.constant and self.assigned: 
            raise Exception("cannot reassign value of a constant")
        value_length = len(value)
        # check types
        match self.type:
            case Type.INT:
                self.value = int(value)
            case Type.DOUBLE:
                self.value = float(value)
            case Type.CHAR:
                escape = '\\' in value
                if (not escape and value_length != 3) or (escape and value_length != 4):
                    raise Exception("invalid character: {}".format(value))
                self.value = value
            case Type.STRUCT:
                pass
            case Type.ENUM:
                pass
            case Type.UNION:
                pass
            case Type.VOID:
                self.value = value

        self.assigned = True

variables = Stack() # dictionary keys map to variable class object
typedefs = Stack()

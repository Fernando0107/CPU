class Memory():
    
    def __init__(self, size):
        self.memoria = [None] * size


class Registers(Memory):
    
    A = Memory(4).memoria
    B = Memory(4).memoria
    C = Memory(4).memoria
    D = Memory(4).memoria
    PC = 0
    IR = Memory(4).memoria
    OR = Memory(4).memoria



class RAM(Memory):
    
    def __init__(self, size):
        self.RAM = Memory(size).memoria              # Memoria de 16 bits 

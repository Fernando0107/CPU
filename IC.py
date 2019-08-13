class IC:

    def __init__(self, name, manufacture, build_date, porpose):
        self.name = name
        self.manufacture = manufacture
        self.build = build_date
        self.porpose = porpose


class Memory(IC):

    memoria = [None] * 4


class ALU(IC):

    def __init__(self, OPcode, Input, Output):
        self.zero = False
        self.Overflow = False
        self.Negative = False
        self.op = OPcode
        self.inp = Input
        self.out = Output


class CU(IC):

    pass


class Registers(Memory):

    def __init__(self):
        self.A = super().memoria
        self.B = super().memoria
        self.C = super().memoria
        self.D = super().memoria
        self.PC = 0
        self.IR = super().memoria
        self.OR = super().memoria

    def write(binario, registro):
        for x in range(len(binario)):
            registro[x] = int(binario[x])


class Ram(Memory):
    
    def __init__(self):
        self.RAM = super().memoria*2


reg = Registers()
REM = Ram()

Registers.write('0110', reg.A)
print(reg.A)
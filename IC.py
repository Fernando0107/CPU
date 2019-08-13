class IC: 

    def __init__(self, name, manufacture, build_date, porpose):
        self.name = name
        self.manufacture = manufacture
        self.build = build_date
        self.porpose = porpose

class Memory(IC):

    pass

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
        self.A = ""
        self.B = ""
        self.C = ""
        self.D = ""
        self.PC = 0
        self.IR = ""
        self.OR = ""

class Ram(Memory):

    pass

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


class CU():

    def read_file(filename):

        #Open File and split
        alm = []                                            #Almacenador de input 
        spliter = []                                        #Almacenador de input sin # y por espacios
        for line in open(filename):
            li = line.strip()

            if not li.startswith("#"):                      #Ignorar el # del archivo

                x = line.rstrip()

                alm.append(x)

        for i in range(len(alm)):
            spliter = spliter + alm[i].split(" ")               #Hacer el split cuando haya un espacio

        return spliter

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
        self.RAM = super().memoria*4                #Memoria de 16 bits 


reg = Registers()
REM = Ram()
read = CU()

#Registers.write('0110', reg.A)
#print(reg.A)

#CU.read_file('instrucciones.code')


Registers.write(CU.read_file('instructions.code')[0], reg.A)
print('Test Registro A:\n',reg.A)

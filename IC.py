import time

class IC:

    def __init__(self, name, manufacture, build_date, porpose):
        self.name = name
        self.manufacture = manufacture
        self.build = build_date
        self.porpose = porpose


class Memory():

    def __init__(self, size):
        self.memoria = [None] * size


class ALU(IC):

    def __init__(self, OPcode, Input, Output):
        self.zero = False
        self.Overflow = False
        self.Negative = False
        self.op = OPcode
        self.inp = Input
        self.out = Output

    def convert(operand):
        s = [str(i) for i in operand]
        result = "".join(s)
        return result

    def addition(operand1, operand2):
        operand1 = ALU.convert(operand1)
        operand2 = ALU.convert(operand2)
        result = str(bin(int(operand1, 2) + int(operand2, 2))).replace('b', '0', 1)     # Transforma los operandos en integers, luego opera binariamente sobre estos
        return result

class CU():

    def read_instructions(filename):

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

    def read_bios_ram(filename, ram):                               # Buscar los datos a cargar en la RAM
        x = 0
        with open(filename, 'r') as f:
            for line in f:
                if 'RAM_' in line:
                    for line in f:
                        li = line.strip()
                        ram.append(li[2][0])
                        x += 1
        for y in range(len(ram)):                                   # Cambiar los strings a ints
            ram[y] = int(ram[y])
        return ram

    def turn_on(self, filename1, filename2, ram):
        self.read_bios_ram(filename1, ram)
        self.read_instructions(filename2)


class Registers(Memory):

    A = Memory(4).memoria
    B = Memory(4).memoria
    C = Memory(4).memoria
    D = Memory(4).memoria
    PC = 0
    IR = Memory(4).memoria
    OR = Memory(4).memoria

    def write(binario, registro):
        for x in range(len(binario)):
            registro[x] = int(binario[x])


class Ram(Memory):
    
    def __init__(self):
        self.RAM = []                # Memoria de 16 bits 

class Clock(IC):

    def Hz():
        time.sleep(float(CU.read_file('bios.yml')[1]))        # La velocidad del reloj esta definida por el archivo bios.yaml

reg = Registers(4)
REM = Ram()
read = CU()

CU.turn_on(CU, 'bios.yml', 'instructions.code', REM.RAM)                 # Imprime los valores de la ram en decimales

instruc = CU.read_instructions('instructions.code')                      # Instruc es el arreglo de instrucciones

Registers.write(instruc[0], reg.A)
Registers.write(instruc[1], reg.B)
Registers.write(ALU.addition(reg.A, reg.B), reg.C)
print(reg.C)


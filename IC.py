import time

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

    def addition(operand1, operand2):
        result = str(bin(int(operand1, 2) + int(operand2, 2))).replace('b', '0', 1)     # Transforma los operandos en integers, luego opera binariamente sobre estos
        return result

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
        self.RAM = []                #Memoria de 16 bits 

class Clock(IC):

    def Hz():
        time.sleep(float(CU.read_file('bios.yml')[1]))        # La velocidad del reloj esta definida por el archivo bios.yaml

reg = Registers()
REM = Ram()
read = CU()
print(CU.read_bios_ram('bios.yml', REM.RAM))                  # Imprime los valores de la ram en decimales



#Registers.write(CU.read_file('instructions.code')[0], reg.A)
#print('Test Registro A:\n',reg.A)
#print(ALU.addition('0001', '0010'))

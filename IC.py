from Memory import *                                            #From file Memory, import erything
from Clock import *
#from ALU import *
import random


class IC:

    def __init__(self, name, manufacture, build_date, porpose):
        self.name = name
        self.manufacture = manufacture
        self.build = build_date
        self.porpose = porpose

class CU():

    def orchestra(instruc):
        idops = ['OR', 'AND', 'ADD', 'SUB', 'NOT']
        for x in range(len(instruc)):
            try:
                CU.opCode(instruc[x], instruc[x+1])
            except:
                pass
        if instruc[x] in idops:
            if instruc[x+1][0:2] == '00':
                var0 = reg.A
            if instruc[x+1][2:4] == '00':
                var1 = reg.A
            if instruc[x+1][0:2] == '01':
                var0 = reg.B
            if instruc[x+1][2:4] == '01':
                var1 = reg.B 
            CU.opCode(instruc[x], var0, var1)


    def read_instructions(filename):

        #Open File and split
        alm = []                                            #Almacenador de input 
        spliter = []                                        #Almacenador de input sin # y por espacios
        for line in open(filename):
            li = line.strip()

            if not li.startswith("#"):                      #Ignorar el # del archivo

                x = line.rstrip()                           #Remueve la linea con #

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
                        try:
                            li = li[2] + li[3]
                            ram[x] = ALU.binary(int(li))
                        except:
                            ram[x] = ALU.binary(int(li[2]))
                        
                        x += 1
        for y in range(len(ram)):                                   # Cambiar los strings a ints
            ram[y] = int(ram[y])
        return ram

    def turn_on(self, filename1, filename2, ram):
        self.read_bios_ram(filename1, ram)
        self.read_instructions(filename2)

    def opCode(opcode, value=0, value2='default', value3='default'):

        #self.instruction = opcode
        #self.value = value
        alm = [0000, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, '0000', '0001',
               '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
        alm2 = ['OUTPUT', 'LD_A', 'LD_B', 'AND', 'ILD_A','STR_A', 'STR_B', 'OR', 'ILD_B', 'ADD', 'SUB', 'JMP', 'JMP_N', 'NOT', 'HALT']
        ins = {
            0000:'OUTPUT',
            1:'LD_A',
            10:'LD_B',
            11:'AND',
            100:'ILD_A',
            101:'STR_A',
            110:'STR_B',
            111:'OR',
            1000:'ILD_B',
            1001:'ADD',
            1010:'SUB',
            1011:'JMP',
            1100:'JMP_N',
            1101:'LD_RD',
            1110:'NOT',
            1111:'HALT',
            'OUTPUT': 'OUTPUT',
            'LD_A': 'LD_A',
            'LD_B': 'LD_B',
            'AND': 'AND',
            'ILD_A': 'ILD_A',
            'STR_A': 'STR_A',
            'STR_B': 'STR_B',
            'OR': 'OR',
            'ILD_B': 'ILD_B',
            'ADD': 'ADD',
            'SUB': 'SUB',
            'JMP': 'JMP',
            'LD_RD': 'LD_RD',
            'NOT': 'NOT',
            'HLT': 'HALT'
        }
        if str(opcode).isdigit():                                               #Revisa si el opcode es un numero o es un strig

            if opcode in alm:                                                       #Verifica si el numero esta en el almacenador de opcodes en digitos 
                
                x = ins[int(opcode)]                                            #Almacena el valor del Opcode, que sera el atributo del motodo ALU
                brain = getattr(ALU(), x, '\nOpcode instruction is not valid.\n')    # getatrr es equivalente a objeto.atrubuto | retorna el atributo
                
                if value2 == 'default' and value3 == 'default':
                    brain(value)
                if value2 != 'default' and value3 == 'default':
                    brain(value, value2)
                if value2 != 'default' and value3 != 'default':
                    brain(value, value2, value3)                                                             #Manda a llamar la funcion  manda el valor a el metodo 

            else:
                print('\nOpcode instruction is not valid.\n')

        else:
            if opcode in alm2:                                                  #Verifica si el string  esta en el almacenador de opcodes en string

                y = ins[(opcode)]
                brain = getattr(ALU(), y, '\nOpcode instruction is not valid.\n')

                if value2 == 'default' and value3 == 'default':
                    brain(value)
                if value2 != 'default' and value3 == 'default':
                    brain(value, value2)
                if value2 != 'default' and value3 != 'default':
                    brain(value, value2, value3)     
            else:
                print('\nOpcode instruction is not valid.\n')
class ALU(IC):
    
    OVERFLOW_FLAG = False
    NEGATIVE_FLAG = False
    ZERO_FLAG = False

    def __init__(self):
        #self.op = OPcode
        #self.inp = Input
        #self.out = Output
        pass

    def write(binario, registro):
        try:
            for x in range(len(binario)):
                registro[x] = int(binario[x])
        except IndexError:
            if binario[0] == '1':
                ALU.OVERFLOW_FLAG = True
            y = 1
            for x in range(len(registro)):
                registro[x] = int(binario[y])
                y += 1

    def convert(operand):
        s = [str(i) for i in operand]
        result = "".join(s)
        return result

    def decimal(n):
        return int(n, 2)

    def binary(n):
        return bin(n).replace("0b", "")

    def STR_A(self, operand, address, RAM):
        result = ALU.convert(operand)
        result = int(result)
        addrs = ALU.decimal(address)
        RAM[addrs] = result

    def STR_B(self, operand, address, RAM):
        result = ALU.convert(operand)
        result = int(result)
        addrs = ALU.decimal(address)
        RAM[addrs] = result

    def ILD_A(self, binario):
        try:
            for x in range(len(binario)):
                reg.A[x] = int(binario[x])
        except IndexError:
            if binario[0] == '1':
                ALU.OVERFLOW_FLAG = True
            y = 1
            for x in range(len(reg.A)):
                reg.A[x] = int(binario[y])
                y += 1

    def ILD_B(self, binario):
        try:
            for x in range(len(binario)):
                reg.B[x] = int(binario[x])
        except IndexError:
            if binario[0] == '1':
                ALU.OVERFLOW_FLAG = True
            y = 1
            for x in range(len(reg.B)):
                reg.B[x] = int(binario[y])
                y += 1

    def fill(uncomp):
        if len(uncomp) == 1:
            uncomp = '000'+uncomp
        if len(uncomp) == 2:
            uncomp = '00'+uncomp
        if len(uncomp) == 3:
            uncomp = '0'+uncomp
        else:
            pass
        return uncomp

    def negative(value):
        if value[0] == '-':
            ALU.NEGATIVE_FLAG = True
            value = value.replace('-', '0', 1)
        return value

    def OUTPUT(self, value):
        print('Output:\n', value)

    def LD_A(self, operand, address, RAM):
        addrs = ALU.decimal(address)
        result = str(RAM[addrs])
        result = ALU.fill(result)
        ALU.write(result, operand)

    def LD_B(self, operand, address, RAM):
        addrs = ALU.decimal(address)
        result = str(RAM[addrs])
        result = ALU.fill(result)
        ALU.write(result, operand)

    def LD_RD(self, operand):
        result = random.randint(0, 15)
        result = ALU.binary(result)
        result = ALU.fill(result)
        ALU.write(result, operand)

    def ADD(self, operand1, operand2):
        operands1 = ALU.convert(operand1)
        operands2 = ALU.convert(operand2)
        # Transforma los operandos en integers, luego opera binariamente sobre estos
        result = str(bin(int(operands1, 2) + int(operands2, 2))
                     ).replace('b', '0', 1)
        result = ALU.fill(result)
        ALU.write(result, operand2)

    def SUB(self, operandsub, operandsub2):
        operandsub = ALU.convert(operandsub)
        operandsub2 = ALU.convert(operandsub2)
        resultsub = str(
            bin(int(operandsub, 2)-int(operandsub2, 2))).replace('b', '0', 1)
        resultsub = ALU.negative(resultsub)
        return resultsub

    def AND(self, operanda, operandb):
        result = [0, 0, 0, 0]
        for i in range(len(result)):
            if operanda[i] == operandb[i]:
                result[i] = 1
            else:  
                result[i] = 0
        ALU.write(result, operandb)

    def OR(self, operanda, operandb):
        result = [0, 0, 0, 0]
        for i in range(len(result)):
            if operanda[i] == operandb[i]:
                result[i] = 0
            else:  
                result[i] = 1
        ALU.write(result, operandb)

    def NOT(self, operandnot, operandnotsave):
        print('test')
        y = 0

        for x in operandnot:
            if x == 0:
                operandnot[y] = 1
            else:
                operandnot[y] = 0
            y += 1
        f = ALU.convert(operandnot)
        ALU.write(f, operandnotsave)

    def ZERO(operand0):

        alm = ['0000', 0000]
        if operand0 in alm:
            ALU.ZERO_FLAG = True                             # Se arreglo la funcion
        else:
            ALU.ZERO_FLAG = False


brain = IC('Brain PC', "I don't know", '24/08/2019','Get a good grade in this project')
reg = Registers(4)
REM = RAM(16)
read = CU()

CU.turn_on(CU, 'bios.yml', 'instructions.code', REM.RAM)                 # Imprime los valores de la ram en decimales

instruc = CU.read_instructions('instructions.code')                      # Instruc es el arreglo de instrucciones
CU.orchestra(instruc)
print(reg.B)
        
from Memory import *                                            #From file Memory, import erything
from Clock import *
#from ALU import *
import time
import random


class IC:

    def __init__(self, name, manufacture, build_date, porpose):
        self.name = name
        self.manufacture = manufacture
        self.build = build_date
        self.porpose = porpose

class CU():

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
                        ram[x] = ALU.binary(int(li[2][0])) 
                        x += 1
        for y in range(len(ram)):                                   # Cambiar los strings a ints
            ram[y] = int(ram[y])
        return ram

    def turn_on(self, filename1, filename2, ram):
        self.read_bios_ram(filename1, ram)
        self.read_instructions(filename2)

    def opCode(opcode, value):

        #self.instruction = opcode
        #self.value = value
        alm = [0000, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]
        alm2 = ['OUTPUT', 'LD_A', 'LD_B', 'AND', 'ILD_A','STR_A', 'STR_B', 'OR', 'ILD_B', 'ADD', 'SUB', 'JMP', 'JMP_N', 'HALT']
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
            1110:'',
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
            'New Op 2 ': '',
            'HLT': 'HALT'
        }

        if str(opcode).isdigit():                                               #Revisa si el opcode es un numero o es un strig

            if opcode in alm:                                                       #Verifica si el numero esta en el almacenador de opcodes en digitos 
                
                x = ins[int(opcode)]                                            #Almacena el valor del Opcode, que sera el atributo del motodo ALU

                brain = getattr(ALU(), x, '\nOpcode instruction is not valid.\n')    # getatrr es equivalente a objeto.atrubuto | retorna el atributo
                
                brain(value)                                                     #Manda a llamar la funcion  manda el valor a el metodo 

            else:
                print('\nOpcode instruction is not valid.\n')

        else:
            if opcode in alm2:                                                  #Verifica si el string  esta en el almacenador de opcodes en string

                y = ins[(opcode)]
                
                brain = getattr(ALU(), y, '\nOpcode instruction is not valid.\n')

                brain(value) 
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

    def LD_A(operand, address, RAM):
        addrs = ALU.decimal(address)
        result = str(RAM[addrs])
        result = ALU.fill(result)
        ALU.write(result, operand)

    def LD_B(operand, address, RAM):
        addrs = ALU.decimal(address)
        result = str(RAM[addrs])
        result = ALU.fill(result)
        ALU.write(result, operand)

    def LD_RD(operand):
        result = random.randint(0, 15)
        result = ALU.binary(result)
        result = ALU.fill(result)
        ALU.write(result, operand)

    def ADD(self, operand1, operand2):
        operand1 = ALU.convert(operand1)
        operand2 = ALU.convert(operand2)
        # Transforma los operandos en integers, luego opera binariamente sobre estos
        result = str(bin(int(operand1, 2) + int(operand2, 2))
                     ).replace('b', '0', 1)
        return result

    def SUB(self, operandsub, operandsub2):
        operandsub = ALU.convert(operandsub)
        operandsub2 = ALU.convert(operandsub2)
        resultsub = str(
            bin(int(operandsub, 2)-int(operandsub2, 2))).replace('b', '0', 1)
        resultsub = ALU.negative(resultsub)
        return resultsub

    def AND(self, operanda, operandb):
        operanda = ALU.convert(operanda)
        operandb = ALU.convert(operandb)
        if operanda == True and operandb == True:
            return True
        else:
            return False

    def OR(self, operanda1, operandb1):
        operanda1 = ALU.convert(operanda1)
        operandb1 = ALU.convert(operandb1)
        if operanda1 == True:
            return True
        elif operandb1 == True:
            return True
        else:
            return False

    def XOR(self, operanda3, operandb3):
        operanda3 = ALU.convert(operanda3)
        operandb3 = ALU.convert(operandb3)
        if operanda3 != operandb3:
            return True
        else:
            return False

    def NEGATIVE(self, operandneg):
       #operandneg = ALU.convert(operandneg)
        if operandneg < 0:
            return True
            print("Negative number")

    def NOT(operandnot):

        y = 0

        for x in operandnot:
            if x == 0:
                operandnot[y] = 1
            else:
                operandnot[y] = 0
            y += 1
        return operandnot

    def ZERO(operand0):

        alm = ['0000', 0000]
        if operand0 in alm:
            ALU.ZERO_FLAG = True                             # Se arreglo la funcion
        else:
            ALU.ZERO_FLAG = False



reg = Registers(4)
REM = RAM(16)
read = CU()

CU.turn_on(CU, 'bios.yml', 'instructions.code', REM.RAM)                 # Imprime los valores de la ram en decimales

instruc = CU.read_instructions('instructions.code')                      # Instruc es el arreglo de instrucciones
'''
ALU.write(instruc[0], reg.A)
ALU.write(instruc[1], reg.B)
ALU.write(ALU.ADD(ALU,reg.A, reg.B), reg.C)
print(reg.C)
print(REM.RAM)
print(ALU.OVERFLOW_FLAG)
ALU.write('0010', reg.B)
ALU.write('0001', reg.A)
'''

ALU.ZERO('0000')

CU.opCode(0000,70)

print(ALU.NOT(reg.A))
print(ALU.ZERO_FLAG)

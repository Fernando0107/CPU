from Memory import *                                            #From file Memory, import erything
from Clock import *
import sys
import random
import time


class IC:

    def __init__(self, name, manufacture, build, porpose):
        self.name = name
        self.manufacture = manufacture
        self.build = build
        self.porpose = porpose
    
    def brian_IC(self):
    
        print('\nCPU Name:',self.name,'\n')
        print('Manufacture: \n' ,self.manufacture,'\n')
        print('Build date:', self.build, '\n')
        print('Porpuse: \n', self.porpose, '\n')

class CU():


    def orchestra(instruc, clock_speed, RAM):
        PC = 0
        mult = [None] * instruc.count('JMP') * 16
        mult_n = [None] * instruc.count('JMP_N') * 16
        idstr = ['LD_A', 'LD_B', 'STR_A', 'STR_B', 'OUTPUT']
        idops = ['OR', 'AND', 'ADD', 'SUB', 'NOT', '1010', '1001', '0011', '0111', '1110']
        if 'JMP' in instruc:
            instruc.extend(mult)
        if 'JMP_N' in instruc:
            instruc.extend(mult_n)
        for x in range(len(instruc)):
            if instruc[PC] == None:
                break
            if instruc[PC] == 'JMP':
                subindex = ALU.decimal(instruc[PC+1])
                PC = subindex
            if instruc[PC] == 'JMP_N' and ALU.NEGATIVE_FLAG == True:
                subindex = ALU.decimal(instruc[PC+1])
                PC = subindex
            if instruc[PC] == 'HALT':
                ALU.HALT()

            try:
                if PC % 2 == 0:
                    #Clock.Hz(clock_speed)
                    print('\n FETCH {} \n'.format(instruc[PC]))
                    if float(clock_speed) == 0:
                        input('PRESS A KEY TO CONTINUE')
                    if float(clock_speed) > 0:
                        Clock.Hz(clock_speed)
                    print('\n EXECUTE {} \n'.format(instruc[PC]))
                    CU.opCode(instruc[PC], instruc[PC+1])                
            except:
                pass
            if instruc[PC] in idops:
                if instruc[PC+1][0:2] == '00':
                    var0 = REG.A
                if instruc[PC+1][2:4] == '00':
                    var1 = REG.A
                if instruc[PC+1][0:2] == '01':
                    var0 = REG.B
                if instruc[PC+1][2:4] == '01':
                    var1 = REG.B
                if instruc[PC+1][0:2] == '10':
                    var0 = REG.C
                if instruc[PC+1][2:4] == '10':
                    var1 = REG.C
                if instruc[PC+1][0:2] == '11':
                    var0 = REG.D
                if instruc[PC+1][2:4] == '11':
                    var1 = REG.D
                if PC % 2 == 0:  
                    CU.opCode(instruc[PC], var0, var1)
            if instruc[PC] in idstr:
                if PC % 2 == 0:
                    CU.opCode(instruc[PC], instruc[PC+1], RAM)

            PC = PC + 1           

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
        alm2 = ['OUTPUT', 'LD_A', 'LD_B', 'AND', 'ILD_A', 'STR_A', 'STR_B',
                'OR', 'ILD_B', 'ADD', 'SUB', 'JMP', 'JMP_N', 'HALT', 'NOT', 'LD_RD']
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
            'HALT': 'HALT',
            'OUTPUT': 'OUTPUT',
            'LOAD_A': 'LD_A',
            'LOAD_B': 'LD_B',
            'ILOAD_A': 'ILD_A',
            'STORE_A': 'STR_A',
            'STORE_B': 'STR_B',
            'OR': 'OR',
            'ILOAD_B': 'ILD_B',
            'JUMP': 'JMP',
            'LOAD_RD': 'LD_RD',
        }
        if str(opcode).isdigit():                                               #Revisa si el opcode es un numero o es un strig

            #if opcode == 'HALT' or opcode == '1111':
                    #ALU.HALT()

            if opcode in alm:                                                       #Verifica si el numero esta en el almacenador de opcodes en digitos 
                
                x = ins[int(opcode)]                                            #Almacena el valor del Opcode, que sera el atributo del motodo ALU
                brain = getattr(ALU(), x, '\nOpcode instruction is not valid.\n')    # getatrr es equivalente a objeto.atrubuto | retorna el atributo

                if value == 0 and value2 == 'default' and value3 == 'default':
                    ALU.HALT()
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

                if value ==0 and value2 == 'default' and value3 == 'default':
                    ALU.HALT()
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

    def STR_A(self, address, RAM):
        result = ALU.convert(REG.A)
        result = int(result)
        addrs = ALU.decimal(address)
        RAM[addrs] = result

    def STR_B(self, address, RAM):
        result = ALU.convert(REG.B)
        result = int(result)
        addrs = ALU.decimal(address)
        RAM[addrs] = result

    def ILD_A(self, binario):
        try:
            for x in range(len(binario)):
                REG.A[x] = int(binario[x])
        except IndexError:
            if binario[0] == '1':
                ALU.OVERFLOW_FLAG = True
            y = 1
            for x in range(len(REG.A)):
                REG.A[x] = int(binario[y])
                y += 1

    def ILD_B(self, binario):
        try:
            for x in range(len(binario)):
                REG.B[x] = int(binario[x])
        except IndexError:
            if binario[0] == '1':
                ALU.OVERFLOW_FLAG = True
            y = 1
            for x in range(len(REG.B)):
                REG.B[x] = int(binario[y])
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

    def OUTPUT(self, value, RAM):
        if type(RAM) is list:

            result = RAM[ALU.decimal(value)]
            result = str(result)
            result = ALU.fill(result)
            print('OUTPUT:',result)
        '''if type(value) is list:
                                    value = ALU.convert(value)
                                    value = int(value)
                                elif type(value) is int:
                                    value = str(value)
                                    value = ALU.fill(value)
                                print('Output:\n', value)'''

    def LD_A(self, address, RAM):
        addrs = ALU.decimal(address)
        result = str(RAM[addrs])
        result = ALU.fill(result)
        ALU.write(result, REG.A)

    def LD_B(self, address, RAM):
        addrs = ALU.decimal(address)
        result = str(RAM[addrs])
        result = ALU.fill(result)
        ALU.write(result, REG.B)

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
        if len(result) < 4:
            result = ALU.fill(result)
        if len(result) > 4:
            subindexx = len(result) - 4
            result = result[subindexx:]
        ALU.write(result, operand2)
        

    def SUB(self, operandsub, operandsub2):
        operandsubs = ALU.convert(operandsub)
        operandsubs2 = ALU.convert(operandsub2)
        resultsub = str(
            bin(int(operandsubs, 2)-int(operandsubs2, 2))).replace('b', '0', 1)
        resultsub = ALU.negative(resultsub)
        #resultsub = ALU.fill(resultsub)
        resultsub = ALU.negative(resultsub)
        ALU.write(resultsub, operandsub2)

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
        y = 0
        for x in operandnot:
            if x == 0:
                operandnot[y] = 1
            else:
                operandnot[y] = 0
            y += 1
        f = ALU.convert(operandnot)
        ALU.write(f, operandnotsave)
        #print('NOT?:\n', operandnot)

    def ZERO(operand0):

        alm = ['0000', 0000]
        if operand0 in alm:
            ALU.ZERO_FLAG = True                             # Se arreglo la funcion
        else:
            ALU.ZERO_FLAG = False
    
    def HALT():
        print('\n ---------- End Program ---------- \n')
        sys.exit()


def Brain():

    print('---------- Welcome! ----------')

    brain = IC("Brain PC", "I don't know","26/08/2019", "Conquer the cyber world!")

    brain.brian_IC()

    x = input('Continue with file No. 1? (y/n)\n')

    if x == 'n' or x == 'N':
        ALU.HALT()
    else:
        pass

    print('\n---------- Executing file No. 1 ----------')
    # Instruc es el arreglo de instrucciones
    instruc = CU.read_instructions('instructions.code')
    CU.orchestra(instruc, clock_speed[1], REM.RAM)

    x = input('Continue with file No. 2? (y/n)\n')

    if x == 'n' or x == 'N':
        ALU.HALT()
    else:
        pass

    print('\n---------- Executing file No. 2 ----------')
    instruc = CU.read_instructions('ins2.code')
    CU.orchestra(instruc, clock_speed[1], REM.RAM)

    x = input('Continue with file No. 3? (y/n)\n')

    if x == 'n' or x == 'N':
        ALU.HALT()
    else:
        pass

    print('\n---------- Executing file No. 3 ----------')
    instruc = CU.read_instructions('ins3.code')
    CU.orchestra(instruc, clock_speed[1], REM.RAM)

    x = input('Continue with file No. 4? (y/n)\n')

    if x == 'n' or x == 'N':
        ALU.HALT()
    else:
        pass

    print('\n---------- Executing file No. 4 ----------')
    instruc = CU.read_instructions('ins4.code')
    CU.orchestra(instruc, clock_speed[1], REM.RAM)

    x = input('Continue with file No. 5? (y/n)\n')

    if x == 'n' or x == 'N':
        ALU.HALT()
    else:
        pass

    print('\n---------- Executing file No. 5 ----------')
    instruc = CU.read_instructions('ins5.code')
    CU.orchestra(instruc, clock_speed[1], REM.RAM)

    print('\n ---------- End Program ---------- \n')

if __name__ == "__main__":

    REG = Registers(4)
    REM = RAM(16)
    read = CU()
    clock = Clock('clock', 'i5', 'Intel')

    CU.turn_on(CU, 'bios.yml', 'instructions.code', REM.RAM)                 # Imprime los valores de la ram en decima
    clock_speed = (CU.read_instructions('bios.yml'))
    Brain()
    #instruc = CU.read_instructions('instructions.code')                      # Instruc es el arreglo de instrucciones
    #CU.orchestra(instruc, clock_speed[1], REM.RAM)


    

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
                        ram[x] = li[2][0] 
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
            1101:'',
            1110:'',
            1111:'HALT',
                                #Esto es solo por si nos envian las intrucciones en string y no en 0's y 1's.
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
            'New Op': '',
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
    
    def __init__(self, size):
        self.RAM = Memory(size).memoria              # Memoria de 16 bits 

class ALU(IC):
    
    def __init__(self):
        self.zero = False
        self.Overflow = False
        self.Negative = False
        #self.op = OPcode
        #self.inp = Input
        #self.out = Output

    def convert(operand):
        s = [str(i) for i in operand]
        result = "".join(s)
        return result

    def OUTPUT(self,value):

        print('Output:\n', value)

    def addition(operand1, operand2):
        operand1 = ALU.convert(operand1)
        operand2 = ALU.convert(operand2)
        result = str(bin(int(operand1, 2) + int(operand2, 2))).replace('b', '0', 1)     # Transforma los operandos en integers, luego opera binariamente sobre estos
        return result

class Clock(IC):

    def Hz():
        time.sleep(float(CU.read_file('bios.yml')[1]))        # La velocidad del reloj esta definida por el archivo bios.yaml

reg = Registers(4)
REM = Ram(16)
read = CU()

CU.turn_on(CU, 'bios.yml', 'instructions.code', REM.RAM)                 # Imprime los valores de la ram en decimales

instruc = CU.read_instructions('instructions.code')                      # Instruc es el arreglo de instrucciones

Registers.write(instruc[0], reg.A)
Registers.write(instruc[1], reg.B)
Registers.write(ALU.addition(reg.A, reg.B), reg.C)
print(reg.C)
print(REM.RAM)

testOp = CU.opCode(0000,10)         #CU.opCode(Opcode, valor)
testOp2 = CU.opCode('OUTPUT',70)         #CU.opCode(Opcode, valor)

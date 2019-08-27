# CPU

This is a CPU (Control Process Unit) simulator implemented in python.

## Introduction 

In this project, we develop a Register file machine 4-bit CPU with 16 bytes of RAM and 4 registers plus one extra, one ALU (Arithmetic Logic Unit).

### Information

#### CPU

A CPU (control process unit) is conformed in the most simple way of:

<p align="center">
  <img width="460" height="300" src="https://upload.wikimedia.org/wikipedia/commons/d/d8/ABasicComputer.gif">
</p>

#### CU

A Control Unit is responsible of fetching the instruction set, controlling the data flow across the whole CPU,  controls the timing of each operation and the interaction with peripheral devices. 

#### ALU

Arithmetic Logic Unit, is a digital electronic circuit responsible for (depending on the processor) doing all the arithmetic operations such as (but not limited to): 

* Add
* Subtraction
* Subtract with borrow
* One’s complement
* Two’s complement
* AND
* OR
* Bit shift operations

#### Registers

An important piece of memory that the CU and the ALU can store temporarily the data, one important register is the program counter which keeps track  of where the CPU is reading from the instruction set.

* Instruction Register (Current instruction loaded)
* Instruction Address Register (program counter)

#### RAM

Random Access memory

#### Clock

In charge of control the fetch-decode-execute cycle.




## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Intruction Set Table

| OP CODE 4 bit  | Instruction |Description  | Adress or Regs |
| ------------- | ------------- | ------------- | -------------|
| 0000  | OUTPUT  | Wires OUTPUT register directly to RAM address location (writes to console)  | 4-bit RAM address | 
| 0001  | LD_A  | Reads RAM location into register A | 4-bit RAM address |
| 0010  | LD_B | Reads RAM location into register B  | 4-bit RAM address | 
| 0011  | AND  | Performs AND between 2-bit registers ID | 2 bit register ID |
| 0100  | ILD_A  | Immediate Read constant into register A | 4-bit constant | 
| 0101  | STR_A  | Write from Register A into RAM location  | 4-bit RAM address |
| 1010  | STR_B  | Write from Register B into RAM location  | 4-bit RAM address | 
| 1011  | OR  | Performs OR between 2-bit registers ID  | 2 bit register ID |
| 1000 | ILD_B  | Immediate Read constant into register B  | 4-bit RAM address | 
| 1001  | ADD  | Add two registers, store result into second register  | 2 bit registers ID |
| 0110  | SUB  | Subtract two registers, store result into second register | 2 bit register ID | 
| 0111  | JMP | update Inst. Addr. Reg to new address | 4-bit code address|
| 1100 | JMP_N  | IF ALU result was negative , update Inst. Addr. Reg to new address  | 4-bit memory address | 
| 1101  | LD_RD  | Reads a Random Number into a register  | 4-bit RAM address |
| 1110 | NOT  | Returns the opposite of a given value | 4-bit RAM address | 
| 1111  | HALT  | Program done. Halt computer  | NA |

This are the instructions that our CPU simulator can execute with a given OPcode.

### Prerequisites

What things you need to run the code and how to install them 

> If you have Docker, skip this step.

You should have python installed in your computer.

If not, go to this webpage and follow the instructions to install python. 

```
https://www.python.org/downloads/
```

Now, with python installed, follow the following instructions...

In your terminal, type and run this line:

```
pip install random
```

This librarie will be required for our code to run properly.

### Docker

If you have Docker installed in your computer, you just need to run this lines in your terminal.


```
docker pull fernando7/ic:0.2

docker run -it --rm fernando7/ic:0.2
```

This will run the program automatically, you should be able to watch how the instructions are being executed :).

## Running the code

When you finish installing the prerequisites, now you can run the program!

Execute the following line in your terminal:

```
python IC.py
```

And that's it! you should be able to watch our cool CPU simulator
being awesome ;)

## Test the CPU by your own 

If you want to execute more instructions, or try different type of operations with the registers, all you have to do is modify any of the following .code files: 

```
instructions.code 

ins2.code

ins3.code

ins4.code

ins4.code

ins5.code
```

> Remember our CPU is 4 bits, so you have to keep that in mind when you try any operation.  


## Built With

* [Python](https://docs.python.org/3/) - The program lenguage we used
* [Docker](https://docs.docker.com) - Container plataform

## Contributors

* **Fernando Gonzalez** - *Developer* - [GitHub](https://github.com/Fernando0107)
* **Diego Quan** - *Developer* - [GitHub](https://github.com/dquan101)
* **Adriana Mundo** - *Developer* - [GitHub]()

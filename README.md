# CPU

This is a CPU (Control Process Unit) simulator implemented in python.

##Introduction 

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

### Prerequisites

What things you need to run the code and how to install them 

> If you have Docker, skip this step.

You should have python installed in your computer.

If not, go to this webpage and follow the instructions to install python. 

```
https://www.python.org/downloads/
```

Now, with python installed, follow the following instructions...


In your terminal, type and run this lines:

```
pip install time 
pip install sys
pip install random
```

This libraries will be required for our code to run properly.

### Docker

If you have Docker installed in your computer, you just need to run this line in your terminal.


```
docker run -it --rm fernando7/ic:0.1
```

This will run the program automatically, you should be able to watch how the instructions are being executed.

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Python](https://docs.python.org/3/) - The program lenguage we used
* [Docker](https://docs.docker.com) - Container plataform

## Contributors

* **Fernando Gonzalez** - *Developer* - [GitHub](https://github.com/Fernando0107)
* **Diego Quan** - *Developer* - [GitHub](https://github.com/dquan101)
* **Andriana Mundo** - *Developer* - [GitHub](https://github.com/dquan101)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

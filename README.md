# This is a 20-bit MIPS CPU Design

## Project Overview
This repository contains the implementation of a **20-bit MIPS CPU** designed as part of the **CSE332: Computer Architecture and Organization** course at **North South University (NSU)** under the guidance of **TNF faculty**.

The CPU is designed using **Logisim** and supports **single-cycle execution**. It implements a set of instructions, as detailed in the control signals table below.

The **CSE_332_Group_11_20_bit_CPU(final).circ** file contains the **ALU.circ** we named the ALU circuit as **main**, **20 bit SRL**, **20 bit SLT**, **20 bit SLL**, **ALU control unit**, **control_unit** this is the main control unit of the cpu,
**20_bit_cpu**, **20_bit_reg**, **PC** program counter, **nop** subcircuit for the *NOP* operation

---

## Features
- **20-bit instruction set architecture**
- **Single-cycle CPU design**
- Supports various instructions including arithmetic, logical, memory access, and branching operations
- Implements data memory, registers, and ALU operations
- Includes branch instructions such as **BEQ** and **BNE**

---

## Instruction Set and Control Signals

| Instructions | RegDst | ALUSrc | Memto-Reg | RegWrite | MemRead | MemWrite | Branch | Jump | ALUOp | Opcode |
|--------------|--------|--------|-----------|----------|---------|----------|--------|------|--------|--------|
| Nop          | 0      | 0      | 0         | 0        | 0       | 0        | 0      | 0    | xx     | 000    |
| NOR          | 1      | 0      | 0         | 1        | 0       | 0        | 0      | 0    | 10     | 000    |
| BEQ          | 0      | 0      | 0         | 0        | 0       | 0        | 1      | 0    | 00     | 001    |
| OR           | 1      | 0      | 0         | 1        | 0       | 0        | 0      | 0    | 10     | 000    |
| ADD          | 1      | 0      | 0         | 1        | 0       | 0        | 0      | 0    | 10     | 000    |
| BNE          | 0      | 0      | 0         | 0        | 0       | 0        | 1      | 0    | ××     | 010    |
| SRL          | 1      | 0      | 0         | 1        | 0       | 0        | 0      | 0    | 10     | 000    |
| SW           | 0      | 1      | 0         | 0        | 0       | 1        | 0      | 0    | 01     | 011    |
| SLT          | 1      | 0      | 0         | 1        | 0       | 0        | 0      | 0    | 10     | 000    |
| SLL          | 1      | 0      | 0         | 1        | 0       | 0        | 0      | 0    | 10     | 000    |
| SUB          | 1      | 0      | 0         | 1        | 0       | 0        | 0      | 0    | 10     | 000    |
| JMP          | 0      | 0      | 0         | 0        | 0       | 0        | 0      | 1    | xx     | 100    |
| AND          | 1      | 0      | 0         | 1        | 0       | 0        | 0      | 0    | 10     | 000    |
| LW           | 0      | 1      | 1         | 1        | 1       | 0        | 0      | 0    | 01     | 101    |
| ADDi         | 0      | 1      | 0         | 1        | 0       | 0        | 0      | 0    | 01     | 110    |

---

## Demo Video
To see the CPU in action, check out the ![Demo of Logisim CPU Design](assets/20_BITS_CPU.gif) that demonstrates the working of the CPU and its instruction set.

---

## Assembly Code Format
Below is a sample format for assembly code:
```
ADD R1, R2, R3    // Adds register X2 and X3, stores result in X1
BEQ R4, R5, branch address // Branch to the address where you want to go if X4 equals X5, for this example the branch address is 2
LW R6, R0 7      // Load word from memory address 7 in R6 
SW R8, R0, 8      // Store word in R8 to memory address 8
```

---

## Getting Started
1. Download and install **Logisim** **version: 2.7.1**.
2. Clone this repository.
3. Open the **CSE_332_Group_11_20_bit_CPU(final).circ** file using Logisim.
4. Load the test cases or create your own assembly programs to simulate.
5. If you want to see the every step in details you can open the **CSE_332_Group_11_20_bit_CPU(debug).circ** file using logisim

---

## Contributions
Contributions are welcome! Feel free to fork this repository, submit pull requests, or report issues.

---


---

## Acknowledgments
Special thanks to **TNF Faculty** of **NSU** for assigning this project and guiding us through the implementation.


# A simulation of the logic behind the Minecraft Computer

import csv
import os
import assembler
# --- File Reading ---

# Reading Instruction Set

instr_dict = {}
regf = [0] * 8
# ram = [0] * 256

BASE_DIR = os.getcwd()

try:
    
    with open(BASE_DIR + '/output/out_1.txt') as f:
        bcode = [line.rstrip("\n") for line in f.readlines()]
        
    with open(BASE_DIR +'/instruction_set.csv', newline='') as csvfile:
        instr_set = [row for row in csv.reader(csvfile)]
        for row in instr_set:
            instr_dict[row[1]] = row[0], row[2], row[3]   
                  
except Exception as e:
    print(f"File error: {e}")
    exit()

def NOP(bits) -> None:
    return

def ADD(bits) -> None:
    regf[int(bits[:4], 2)] = regf[int(bits[5:8], 2)] + regf[int(bits[9:12], 2)]

def SUB(bits) -> None:
    regf[int(bits[:4], 2)] = regf[int(bits[5:8], 2)] - regf[int(bits[9:12], 2)]

def LDI(bits) -> None:
    regf[int(bits[:4], 2)] = int(bits[5:12], 2)

def INC(bits) -> None:
    regf[int(bits[:4], 2)] += 1

def DEC(bits) -> None:
    regf[int(bits[:4], 2)] -= 1


def run_simulation() -> list:
    
    funcs = {
        "NOP":NOP,
        "ADD":ADD,
        "SUB":SUB,
        "LDI":LDI
    }
    
    history = [None] * len(bcode)
    
    for i in range(len(bcode)):
        opcode_bits = bcode[i][0:4] # ADD, SUB, NOP, etc... in binary
        operands_bits = bcode[i][4:] # Main register
        if opcode_bits in instr_dict: 
            opcode = instr_dict[opcode_bits][0]
            funcs[opcode](operands_bits) # execute the opcode function with the operand
            history[i] = [opcode, bcode[i],regf.copy()]
    return history

if __name__ == "__main__":
    list(map(lambda row: print(row), run_simulation()))
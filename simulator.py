
# A simulation of the logic behind the Minecraft Computer
# 

import pygame as pg
import csv

# --- File Reading ---

# Reading Instruction Set

instr_dict = {}
p =f"mc_assembler/"

try:
    with open(p + 'output/out_1.txt') as f:
        bcode = [line.rstrip("\n") for line in f.readlines()]
    
    with open(p +'instruction_set.csv', newline='') as csvfile:
        instr_set = [row for row in csv.reader(csvfile)]
        for row in instr_set:
            instr_dict[row[1]] = row[0], row[2], row[3]
            
except Exception as e:
    print(f"File error: {e}")
    
#--- Display Settings ---
SCREEN_WID, SCREEN_HGT = 600, 800
screen = pg.display.set_mode((SCREEN_WID, SCREEN_HGT))
pg.display.set_caption("Computer Simulator")

regf = []
for i in range(8):
    regf.append(0)

ram = [] 
for i in range(256):
    ram.append(0)


def NOP(bits) -> None:
    return

def ADD(bits) -> None:
    regf[int(bits[:4], 2)] += regf[int(bits[5:8], 2)]

def SUB(bits) -> None:
    regf[int(bits[:4], 2)] -= regf[int(bits[5:8], 2)]

def LDI(bits) -> None:
    regf[int(bits[:4], 2)] = int(bits[5:12], 2)

def INC(bits) -> None:
    regf[int(bits[:4], 2)] += 1

def DEC(bits) -> None:
    regf[int(bits[:4], 2)] -= 1


def main():

    funcs = {
        "NOP":NOP,
        "ADD":ADD,
        "SUB":SUB,
        "LDI":LDI

            }
    
    for line in bcode:
        opcode = line[0:4]
        operands = line[4:]

        if opcode in instr_dict:
            funcs[instr_dict[opcode][0]](operands)
            # pass
            # eval(f"{instr_dict[opcode][0]}(operands)")

# def display():

    # quit_pg = True

    # while not quit_pg:
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             quit_pg = True

    #     draw_scene()
    #     pg.display.update()
    #     pg.display.flip()

if __name__ == "__main__":
    # display()
    main()

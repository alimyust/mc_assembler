
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
            instr_dict[row[0]] = row[1:]
            
except Exception as e:
    print(f"File error: {e}")
    
#--- Display Settings ---
SCREEN_WID, SCREEN_HGT = 600, 800
screen = pg.display.set_mode((SCREEN_WID, SCREEN_HGT))
pg.display.set_caption("Computer Simulator")

register_file = []
for i in range(8):
    register_file.append(0)

ram = [] 
for i in range(256):
    ram.append(0)

def ADD(bits:int) -> int:
    pass

def main():
    print(instr_dict)
    # for line in bcode:
    #     if line[0:4] == 
    
    pass

# def display():

    quit_pg = True

    while not quit_pg:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_pg = True

        draw_scene()
        pg.display.update()
        pg.display.flip()

if __name__ == "__main__":
    # display()
    main()

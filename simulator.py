
# A simulation of the logic behind the Minecraft Computer
# 

import pygame as pg

#--- Display Settings ---
SCREEN_WID, SCREEN_HGT = 600, 800
screen = pg.display.set_mode((SCREEN_WID, SCREEN_HGT))
pg.display.set_caption("Computer Simulator")

register_file = {} 
for i in range(8):
    register_file.update({"r" + str(i):0})

ram = {} 
for i in range(256):
    ram.update({"r" + str(i):0})

def draw_scene():
    pg.draw.rect(screen, (125,125,125), pg.Rect(0,0,SCREEN_WID,SCREEN_HGT))

    #Registerfile
    reg_file_rect = pg.Rect(0,0,100,80)
    for i in range(len(register_file)):
        pg.draw.rect(screen, (40,160,160), pg.Rect(40, 40 + i*70, 100, 60))



def main():

    quit_pg = False

    while not quit_pg:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_pg = True

        draw_scene()
        pg.display.update()
        pg.display.flip()

if __name__ == "__main__":
    main()


import pygame as pg
import os
import simulator_core


pg.init()
SCREEN_WID, SCREEN_HGT = 600, 800
SCREEN = pg.display.set_mode((SCREEN_WID, SCREEN_HGT))

pg.display.set_caption("Computer Simulator")
font = pg.font.SysFont("Courier", 24, bold=True)

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (125,125,125)


def display_registerfile(history, step) -> None:
    x_start, y_start, box_width, box_height = 10, 10, 100, 40
    x_spacing = box_width + 20
    y_spacing = box_height + 20
    border_dim = 5

    regf = history[step][2]
    text_color = BLACK
    rect_color = WHITE
    border_col = BLACK
    
    for i in range(8):
        for col in range(2):
            reg_index = i + col * 8
            text = font.render(f"r{reg_index}: {regf[reg_index]}", True, text_color)

            rect_x = x_start + col * x_spacing
            rect_y = y_start + i * y_spacing
            rect = pg.Rect(rect_x, rect_y, box_width, box_height)
            
            border_rect = pg.Rect(rect_x - border_dim, rect_y + border_dim,
                                  box_width + 2 * border_dim, box_height + 2 *border_dim)
            
            pg.draw.rect(SCREEN, border_col, border_rect)
            pg.draw.rect(SCREEN, rect_color, rect)
            SCREEN.blit(text, (rect.x + 5, rect.y + 5)) 

def draw_scene(history, step) -> None:

    display_registerfile(history, step)

def display():
    history = simulator_core.run_simulation()
    list(map(lambda row: print(row), history))

    step = 2
    quit_pg = False
    while not quit_pg:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_pg = True
        pg.draw.rect(SCREEN, GRAY, (0, 0, SCREEN_WID, SCREEN_HGT))
        draw_scene(history, step)
        pg.display.update()
        pg.display.flip()
        
        
if __name__ == "__main__":
    display()

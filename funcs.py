from config import SCREEN_SIZE 
CENTER_X = SCREEN_SIZE[0] // 2
CENTER_Y = SCREEN_SIZE[1] // 2


def to_screen_coords(math_x, math_y): 
    screen_x = CENTER_X + math_x 
    screen_y = CENTER_Y - math_y
    return (screen_x, screen_y) 

def to_math_coords(screen_x, screen_y): 
    math_x = screen_x - CENTER_X 
    math_y = screen_y - CENTER_Y
    return (math_x, math_y)
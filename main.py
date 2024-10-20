import pgzrun
from random import randint

WIDTH= 800
HEIGHT= 500

satellites= []
lines= []
next_satellite= 0
number_of_satellite= 8

def create_satellites():
    for count in range(0, number_of_satellite):
        satellite= Actor("satellite")
        satellite.pos= randint(40, WIDTH-40), randint(40, HEIGHT-40)
        satellites.append(satellite)



def draw():
    screen.blit('background',(0,0))
    number=1
    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number=number+1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

def on_mouse_down(pos):
    global next_satellite
    global lines
    if next_satellite < number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite= next_satellite+ 1
    else:
        lines= []
        next_satellite= 0


create_satellites()
pgzrun.go()
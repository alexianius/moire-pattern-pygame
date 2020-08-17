import pygame as pg
import math

pg.init()
pg.display.set_caption('Moire pattern')
dim = (sirina, visina) = (720, 720)
prozor = pg.display.set_mode(dim)

animacija = 0
br_animacija = 7

d = 9 #debljina linija
a = 28 #stranica kvadrata

a2 = 0. #stranica kvadrata druge mreze
xk = 0. #polozaj kruga
ugao = 0. #ugao rotacije

pg.font.init()
font = pg.font.SysFont(None, 60)
tekst = []
for i in range(br_animacija):
    tekst.append(font.render(str(i+1) + '/' + str(br_animacija), False, pg.Color('grey')))


def reset():
    global a2, ugao, xk
    a2 = a*0.95
    xk = visina*1.5
    ugao = -0.1

def crtaj1(): #2 kvadratne mreze od kojih se jedna povecava
    prozor.fill(pg.Color('white'))
    x = 0
    y = 0
    while(x<sirina):
        pg.draw.line(prozor, pg.Color('black'),(x,0),(x,visina),d)
        x += a
        if(animacija==1):
            pg.draw.line(prozor, pg.Color('black'),(0,y),(sirina,y),d)
            y += a
    x = 0
    y = 0
    while(x<sirina):
        pg.draw.line(prozor, pg.Color('black'),(x,0),(x,visina),d)
        x += a2
        if(animacija==1):
            pg.draw.line(prozor, pg.Color('black'),(0,y),(sirina,y),d)
            y += a2

def crtaj2(): #2 mreze od kojih se jedna rotira
    prozor.fill(pg.Color('white'))
    (x, y) = (sirina//2, visina//2)
    xr = math.tan(ugao) * y
    yr = math.tan(ugao) * x
    for i in range(x//a + 1):
        pg.draw.line(prozor, pg.Color('black'), (x-i*a,0), (x-i*a,visina), d)
        pg.draw.line(prozor, pg.Color('black'), (x+i*a,0), (x+i*a,visina), d)
        if(animacija==3):
            pg.draw.line(prozor, pg.Color('black'), (0,y-i*a), (sirina,y-i*a), d)
            pg.draw.line(prozor, pg.Color('black'), (0,y+i*a), (sirina,y+i*a), d)
    ar = 1/math.cos(ugao) * a
    for i in range(int(math.sqrt(2)*x/a) + 1):
        pg.draw.line(prozor, pg.Color('black'), (x-xr-i*ar,0), (x+xr-i*ar,visina), d)
        pg.draw.line(prozor, pg.Color('black'), (x-xr+i*ar,0), (x+xr+i*ar,visina), d)
        if(animacija==3):
            pg.draw.line(prozor, pg.Color('black'), (0,y+yr-i*ar), (sirina,y-yr-i*ar), d)
            pg.draw.line(prozor, pg.Color('black'), (0,y+yr+i*ar), (sirina,y-yr+i*ar), d)

def crtaj3(): #2 grupe koncentricnih krugova
    prozor.fill(pg.Color('white'))
    r = 12
    while( r <= visina/2 - 20 ):
        pg.draw.circle(prozor, pg.Color('black'), (sirina//2, visina//2), r, 5)
        pg.draw.circle(prozor, pg.Color('black'), (int(xk), visina//2), r, 5)
        r+=12

def crtaj4():
    prozor.fill(pg.Color('white'))
    r = 11
    while( r <= visina/2 - 20 ):
        pg.draw.circle(prozor, pg.Color('black'), (sirina//2, visina//2), r, 5)
        r+=11
    r = 12
    while( r <= visina/2 - 20 ):
        pg.draw.circle(prozor, pg.Color('black'), (int(xk), visina//2), r, 5)
        r+=12

def crtaj5():
    prozor.fill(pg.Color('white'))
    r = visina/2 - 20
    centar = (x, y) = (sirina//2, visina//2)
    for i in range(0,360,3):
        fi = math.radians(i)
        pg.draw.line(
            prozor,
            pg.Color('black'),
            centar,
            (x + math.cos(fi)*r, y + math.sin(fi)*r),
            4)
        pg.draw.line(
            prozor,
            pg.Color('black'),
            (xk,y),
            (xk + math.cos(fi)*r, y + math.sin(fi)*r),
            4)


def frejm():
    global a2, ugao, xk
    if animacija < 2:
        crtaj1()
        a2 += 0.01
        if(a2 >= a*2):
            a2 = a
    elif animacija < 4:
        crtaj2()
        ugao += 0.001
        if(ugao >= math.pi/4):
            ugao = -math.pi/4
    elif animacija >= 4 and animacija <= 7:
        if(animacija == 4):
            crtaj3()
        elif(animacija == 5):
            crtaj4()
        else:
            crtaj5()
        xk -= 0.7
        if(xk <= -sirina/2):
            xk = visina * 1.5
    prozor.blit(tekst[animacija], (0,0))
    pg.display.update()



sat = pg.time.Clock() 
kraj = kraj1 = False

reset()

while not(kraj):

    frejm()
    
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True
        elif dogadjaj.type == pg.KEYDOWN:
            if dogadjaj.key == pg.K_LEFT:
                if animacija > 0:
                    animacija -= 1
                    reset()
            elif dogadjaj.key == pg.K_RIGHT:
                if animacija < br_animacija-1:
                    animacija += 1
                    reset()

    sat.tick(60)
pg.quit()

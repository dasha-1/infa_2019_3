from graph import*
import math


def el(x, y, r, g, b):
    a = []
    n = 500
    for i in range(n):
        a.append((x +120*math.cos(2*math.pi*i/n), y+30*math.sin(2*math.pi*i/n)))
        penColor(r, g, b)
        polygon(a)

def dom(x,y,r,g,b):
    brushColor(r,g,b)
    rectangle(20+x, 100+y, 220+x, 450+y)
    polygon([(10+x, 100+y), (30+x, 80+y), (210+x, 80+y), (230+x, 100+y)])
    brushColor("#ec8520")
    rectangle(30+x, 120+y, 50+x, 160+y)
    rectangle(70+x, 120+y, 90+x, 160+y)
    rectangle(130+x, 120+y, 150+x, 160+y)
    rectangle(170+x, 120+y, 190+x, 160+y)
    rectangle(30+x, 180+y, 50+x, 200+y)
    rectangle(70+x, 180+y, 90+x, 200+y)
    rectangle(130+x, 180+y, 150+x, 200+y)
    rectangle(170+x, 180+y, 190+x, 200+y)
    brushColor("#f9c56c")
    rectangle(180+x, 350, 210+x, 400+y)
    brushColor(49, 0, 98)
    rectangle(40+x, 350, 70+x, 400+y)
    rectangle(90+x, 350, 120+x, 400+y)

def ghost(x,y,r,g,b,size):
    brushColor(r,g,b)
    a =  polygon([((350+x)*size,( 400+y)*size), ((355+x)*size, (410+y)*size), ((360+x)*size, (405+y)*size), ((365+x)*size,( 410+y)*size), ((370+x)*size,( 407+y)*size),
((375+x)*size, 403+y*size), (380+x*size, 400+y*size), (385+x*size, 403+y*size), (390+x*size, 400+y*size), (395+x*size, 407+y*size),
 ((400+x)*size,( 405+y)*size), ((405+x)*size,(407+y)*size),((400+x)*size,(420+y)*size),((395+x)*size,( 390+y)*size),( (393+x)*size,( 393+y)*size), ((390+x)*size, (390+y)*size),
 ((385+x)*size, (387+y)*size),((380+x)*size, (385+y)*size), ((376+x)*size, (380+y)*size), ((373+x)*size, (376+y)*size), ((370+x)*size,( 360+y)*size),
 (368+x*size, 345+y*size),
 ((365+x)*size, (343+y)*size), ((360+x)*size, (340+y)*size), ((357+x)*size, (343+y)*size), ((351+x)*size, (357+y)*size), ((350+x)*size,( 400+y)*size)])
    return a
    

      
windowSize(500, 600)
canvasSize(800, 800)
brushColor(101, 67, 33)
rectangle(0, 300, 500, 800)
brushColor("#c7fcec")
rectangle(0, 0, 500, 300)

dom(0,0,0,0,0)
brushColor(176, 196, 222)
a= ghost(-100,-100,33,232,33,1)
penColor(255,255,254)
brushColor(255,255,254)
circle(460,50,40)
el(370,170,0,255,255)
el(350,70,10,243,30)
el(250,50,20,255,255)
penColor(0,0,0)
brushColor(0,0,0)
c=circle(257,250,1)
s=circle(264,250,1)


def update():
    moveObjectBy(a, 1, 1)
    moveObjectBy(c,1,1)
    moveObjectBy(s,1,1)
    l=0
    changeFillColor(a,"grey")
    l=l+1
    if xCoord(a)>=500:
        close()
   


onTimer(update,50)

run()

from graph import*
import math
windowSize(500, 600)
canvasSize(800, 800)
brushColor(101, 67, 33)
rectangle(0, 300, 500, 800)
brushColor("#c7fcec")
rectangle(0, 0, 500, 300)
brushColor(0, 0, 0)
rectangle(20, 100, 220, 450)
polygon([(10, 100), (30, 80), (210, 80), (230, 100)])
brushColor("#ec8520")
rectangle(30, 120, 50, 160)
rectangle(70, 120, 90, 160)
rectangle(130, 120, 150, 160)
rectangle(170, 120, 190, 160)
rectangle(30, 180, 50, 200)
rectangle(70, 180, 90, 200)
rectangle(130, 180, 150, 200)
rectangle(170, 180, 190, 200)
brushColor("#f9c56c")
rectangle(180, 350, 210, 400)
brushColor(49, 0, 98)
rectangle(40, 350, 70, 400)
rectangle(90, 350, 120, 400)
brushColor(176, 196, 222)
polygon([(350, 400), (355, 410), (360, 405), (365, 410), (370, 407), (375, 403), (380, 400), (385, 403), (390, 400), (395, 407),
 (400, 405), (405,407),(400,420),(395, 390), (393, 393), (390, 390), (385, 387),(380, 385), (376, 380), (373, 376), (370, 360), (368, 345),
 (365, 343), (360, 340), (357, 343), (351, 357), (350, 400)])
penColor(255,255,254)
brushColor(255,255,254)
circle(460,50,40)
n = 500
a=[]
for i in range(n):
    x= 250
    y=50
    a.append((x+150*math.cos(2*math.pi*i/n), y+30*math.sin(2*math.pi*i/n)))
    penColor(95, 158, 160)
    polygon(a)
n = 500
a=[]
for i in range(n):
    x= 350
    y=70
    a.append((x+150*math.cos(2*math.pi*i/n), y+30*math.sin(2*math.pi*i/n)))
    penColor(176,196,222)
    polygon(a)
n = 500
a=[]
for i in range(n):
    x= 370
    y=170
    a.append((x+120*math.cos(2*math.pi*i/n), y+30*math.sin(2*math.pi*i/n)))
    penColor(25,25,112)
    polygon(a)
penColor(0,0,0)
brushColor(0,0,0)
circle(357,350,1)
circle(364,350,1)
run()
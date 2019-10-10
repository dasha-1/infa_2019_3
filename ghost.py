import math
from graph import brushColor, polygon, penColor, rectangle, circle, moveObjectBy,
                  changeFillColor, windowSize, canvasSize, onTimer, run, randColor, xCoord


def el(x, y, r, g, b):
    a = []
    n = 500
    for i in range(n):
        a.append((x + 120 * math.cos(2 * math.pi * i / n),
                  y + 30 * math.sin(2 * math.pi * i / n)))
        penColor(r, g, b)
        polygon(a)


def dom(x, y, r, g, b):
    brushColor(r, g, b)
    rectangle(20 + x, 100 + y, 220 + x, 450 + y)
    polygon([(10 + x, 100 + y), (30 + x, 80 + y),
             (210 + x, 80 + y), (230 + x, 100 + y)])
    brushColor("#ec8520")
    rectangle(30 + x, 120 + y, 50 + x, 160 + y)
    rectangle(70 + x, 120 + y, 90 + x, 160 + y)
    rectangle(130 + x, 120 + y, 150 + x, 160 + y)
    rectangle(170 + x, 120 + y, 190 + x, 160 + y)
    rectangle(30 + x, 180 + y, 50 + x, 200 + y)
    rectangle(70 + x, 180 + y, 90 + x, 200 + y)
    rectangle(130 + x, 180 + y, 150 + x, 200 + y)
    rectangle(170 + x, 180 + y, 190 + x, 200 + y)
    brushColor("#f9c56c")
    rectangle(180 + x, 350, 210 + x, 400 + y)
    brushColor(49, 0, 98)
    rectangle(40 + x, 350, 70 + x, 400 + y)
    rectangle(90 + x, 350, 120 + x, 400 + y)


def ghost(x, y, r, g, b):
    brushColor(r, g, b)
    a = polygon([(350 + x, 400 + y), (355 + x, 410 + y),
                 (360 + x, 405 + y), (365 + x, 410 + y),
                 (370 + x, 407 + y),
                 (375 + x, 403 + y), (380 + x, 400 + y), (385 + x, 403 + y),
                 (390 + x, 400 + y), (395 + x, 407 + y),
                 (400 + x, 405 + y), (405 + x, 407 + y),
                 (400 + x, 420 + y), (395 + x, 390 + y),
                 (393 + x, 393 + y), (390 + x, 390 + y),
                 (385 + x, 387 + y), (380 + x, 385 + y),
                 (376 + x, 380 + y), (373 + x, 376 + y),
                 (370 + x, 360 + y), (368 + x, 345 + y),
                 (365 + x, 343 + y), (360 + x, 340 + y),
                 (357 + x, 343 + y), (351 + x, 357 + y),
                 (350 + x, 400 + y)])
    return a


windowSize(500, 600)
canvasSize(800, 800)
brushColor(101, 67, 33)
rectangle(0, 300, 500, 800)
brushColor("#c7fcec")
rectangle(0, 0, 500, 300)

dom(0, 0, 0, 0, 0)
brushColor(176, 196, 222)
a = ghost(-100, -100, 33, 232, 33)
penColor(255, 255, 254)
brushColor(255, 255, 254)
circle(460, 50, 40)
el(370, 170, 0, 255, 255)
el(350, 70, 10, 243, 30)
el(250, 50, 20, 255, 255)
penColor(0, 0, 0)
brushColor(0, 0, 0)
c = circle(257, 250, 1)
s = circle(264, 250, 1)


def update():
    moveObjectBy(a, 1, 1)
    moveObjectBy(c, 1, 1)
    moveObjectBy(s, 1, 1)
    changeFillColor(a, randColor())
    if xCoord(a) >= 500:
        close()


onTimer(update, 50)

run()

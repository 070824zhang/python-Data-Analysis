import math
from turtle import *
def heart_a(t):
    return 16*math.sin(t)**3
def heart_b(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

speed(1000)
bgcolor("black")
for i in range(1000):
    t = i*0.1
    goto(heart_a(t) * 20, heart_b(t) * 20)
    for j in range(5):
        color("#f73487")
        begin_fill()
done()
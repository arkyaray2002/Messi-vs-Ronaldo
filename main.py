from sketchpy import canvas
import Messi as lm10
import Ronaldo as cr7
import time

Turtle = canvas.sketch(x_offset=290, y_offset=320)

lm10.DrawMessi(Turtle)
cr7.DrawRonaldo(Turtle)

Turtle.draw_fn("v", co=(213, 61, 75), mode=0)
Turtle.draw_fn("s", co=(213, 61, 75), mode=0)


time.sleep(5)
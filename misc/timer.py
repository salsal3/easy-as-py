# Creating a Simple Timer in Python and Using it with Programs in turtle
# https://www.codetoday.co.uk/post/creating-a-simple-timer-in-python-and-using-it-with-programs-in-turtle

import time
import turtle

window = turtle.Screen()
window.tracer(0)

player = turtle.Turtle()
timer_text = turtle.Turtle()

minutes = 0
seconds = 3

start = time.time()
while time.time() - start < 60 * minutes + seconds:
    player.forward(1)
    player.left(1)
    timer_text.clear()
    timer_text.write(int(time.time() - start), font=('Courier', 30))
    
    window.update()
#Glowscript 2.9
#Rhett Kliger's edit
from vpython import color, cylinder, vector, label, arrow, scene
scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-.5, -.3, -1)

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

xaxis = cylinder(color=vector(1, 0, 0), pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.3)  # Makes x axis
xlabel = label(pos=vector(11, 0, 0), text="X", color=color.red, opacity=0, height=30, box=0)
yaxis = cylinder(color=color.green, pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.3)  # Makes y axis
ylabel = label(pos=vector(0, 11, 0), text="Y", color=color.green, opacity=0, height=30, box=0)
zaxis = cylinder(color=color.blue, pos=vector(0, 0, 0), axis=vector(0,0,10), radius=0.3)  # Makes z axis
xlabel = label(pos=vector(0, 0, 11), text="Z", color=color.blue, opacity=0, height=30, box=0)
# Numbers for vector 2-22-99 my birthdate, make the vector yellow
r = arrow(pos=vector(0, 0, 0), axis=vector(2, 22, 99), color=color.yellow, shaftwidth=0.5)
R = label(pos=vector(0, 0, 0), text='r = 2x + 22y + 99z', xoffset=20, yoffset=50, space=30, height=16, border=4, font='sans')


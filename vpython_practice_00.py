#from vpython import box
#box() # Creates a box to be opened in the browser
# It can be rotated by right click
# Zoom in and out by clicking on the box and holding alt key
# You can move the box by clicking on the box and holding shift key

#from vpython import box, vector, color
#box(pos=vector(0, 0, 1), size=vector(0.3, 0.4, 0.5), color=color.blue)
#box()
  # Creates a blue box of given size location and color
  #  Notice that pos, size, and color are optional arguments sent to the box function.
  #  The position (pos) and size are VPython vector objects (we had to import vector from VPython), and color is another VPython object.
  #  Position is the center of the box in cartesian coordinates (x is to the right, y is up, and z is outward). Size is the dimensions of the box in those same directions.

# Try creating a sphere of radius 0.5 and color red
from vpython import sphere, vector, color
ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=vector(1, 0, 0))
ball()
# The above code makes a red sphere

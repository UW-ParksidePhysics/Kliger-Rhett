# Draw three fields that should represent the gravitational constants of the Earth, Mars, and the Moon.
from vpython import *

#Set up balls and characteristics
box1 = box(pos=vector(0, 0, 0), size=vector(100, 1, 100), color=color.green, opacity=0.5)
ball1 = sphere(pos=vector(50, 0, 50), radius=1, color=color.blue, make_trail=True)
box2 = box(pos=vector(200, 0, 0), size=vector(100, 1, 100), color=vector(0.5, 0.5, 0.5), opacity=0.5)
ball2 = sphere(pos=vector(250, 0, 50), radius=1, color=color.yellow)
box3 = box(pos=vector(400, 0, 0), size=vector(100, 1, 100), color=color.red, opacity=0.5)
ball3 = sphere(pos=vector(450, 0, 50), radius=1, color=color.magenta)

#Set up initial conditions
balliv = vector(-1, 0.1, -1) # Constant velocity
acceleration1 = vector(0, -9.8, 0)  # Gravity Earth
acceleration2 = vector(0, -1.6, 0)  # Gravity Moon
acceleration3 = vector(0, -3.7, 0)  # Gravity Mars


# Time evolution parameters
animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.01
stop_time = 100

time = 0.
while time < stop_time:
    rate(rate_of_animation)
    x = ball1.pos.x + balliv.x * time_step + 0.5*acceleration1.x*time_step**2  # The ball1 position on x
    y = ball1.pos.y + balliv.y * time_step + 0.5*acceleration1.y*time_step**2  # The ball1 position on the y
    z = ball1.pos.z + balliv.z * time_step + 0.5*acceleration1.z*time_step**2  # The ball1 position on the z
    ball1.pos = vector(x, y, z)
    x = ball2.pos.x + balliv.x * time_step + 0.5 * acceleration2.x * time_step ** 2  # The ball2 position on x
    y = ball2.pos.y + balliv.y * time_step + 0.5 * acceleration2.y * time_step ** 2  # The ball2 position on the y
    z = ball2.pos.z + balliv.z * time_step + 0.5 * acceleration2.z * time_step ** 2  # The ball2 position on the z
    ball2.pos = vector(x, y, z)
    x = ball3.pos.x + balliv.x * time_step + 0.5 * acceleration3.x * time_step ** 2  # The ball3 position on x
    y = ball3.pos.y + balliv.y * time_step + 0.5 * acceleration3.y * time_step ** 2  # The ball3 position on the y
    z = ball3.pos.z + balliv.z * time_step + 0.5 * acceleration3.z * time_step ** 2  # The ball3 position on the z
    ball3.pos = vector(x, y, z)
    time += time_step






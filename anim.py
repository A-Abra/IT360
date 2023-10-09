import glfw
from math import *
from OpenGL.GL import *
import random


# Callback for mouse button events
def mouse_button_callback(window, button, action, mods):
    x, y = glfw.get_cursor_pos(window)
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        print(x, y)
        print("Left mouse button pressed!")
    elif button == glfw.MOUSE_BUTTON_LEFT and action == glfw.RELEASE:
        print("Left mouse button released!")
    elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS:
        print("Right mouse button pressed!")
    elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.RELEASE:
        print("Right mouse button released!")

# Callback for keyboard events


def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE:
            print("Escape key pressed!")
            glfw.set_window_should_close(window, True)
        elif key == glfw.KEY_A:
            print("A key pressed!")
        elif key == glfw.KEY_B:
            print("B key pressed!")
        # ... add more keys as needed


# Initialize the library
if not glfw.init():
    exit()

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(1000, 1000, "Crowd", None, None)
if not window:
    glfw.terminate()
    exit()

# Make the window's context current
glfw.make_context_current(window)

# Set callbacks
glfw.set_mouse_button_callback(window, mouse_button_callback)
glfw.set_key_callback(window, key_callback)

x_nums = []
y_nums = []
for i in range(50):
    x_num = random.uniform(-1,1)
    y_num = random.uniform(-1,1)
    x_nums.append(x_num)
    y_nums.append(y_num)

x_movs = []
y_movs = []

for i in range(50):
    x_mov = random.uniform(-0.005, 0.005)
    y_mov = random.uniform(-0.005, 0.005)
    x_movs.append(x_mov)
    y_movs.append(y_mov)

# Main loop
while not glfw.window_should_close(window):
    # Clear the screen with black color
    # glClearColor(1.0, 1.0, 1.0, 1.0)

    width, height = glfw.get_window_size(window)
    glViewport(0, 0, width, height)

    # Set color to lightly salted lays chips blue
    glClearColor(0.870, 0.905, 0.937, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    for i in range(50):
        xloc = x_nums[i]
        yloc = y_nums[i]

        xloc += x_movs[i]
        yloc += y_movs[i]

        if(xloc > 1):
            xloc=-1
        if(yloc > 1):
            yloc=-1
        if(xloc < -1):
            xloc=1
        if(yloc < -1):
            yloc=1    

        x_nums[i] = xloc
        y_nums[i] = yloc

    for i in range(50):
        xloc = x_nums[i]
        yloc = y_nums[i]
        sides = 32
        pi=3.14
        radius = 1/50
        glBegin(GL_POLYGON)
        glColor3f(0.807, 0.0, 0.0)
        for i in range(100):
            x = radius*cos(i*2*pi/sides)+xloc
            y = radius*sin(i*2*pi/sides)+yloc
            glVertex2f(x,y)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0.0, 0.0, 0.0)
        for i in range(100):
            x = radius*cos(i*2*pi/sides)+xloc
            y = radius*sin(i*2*pi/sides)+yloc
            glVertex2f(x,y)
        glEnd()

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

# Terminate GLFW
glfw.terminate()

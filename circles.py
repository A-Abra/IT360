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
window = glfw.create_window(1000, 1000, "Two Circles", None, None)
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

# Main loop
while not glfw.window_should_close(window):
    # Clear the screen with black color
    # glClearColor(1.0, 1.0, 1.0, 1.0)

    width, height = glfw.get_window_size(window)
    glViewport(0, 0, width, height)

    # Set color to lightly salted lays chips blue
    glClearColor(0.870, 0.905, 0.937, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    for i in range(2):
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

        glLineWidth(2)
        glBegin(GL_LINE_STRIP)
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

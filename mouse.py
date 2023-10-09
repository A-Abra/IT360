import glfw
from math import *
from OpenGL.GL import *

def distance(x1, y1, x2, y2, width, height):
    # Normalize the coordinates to the range [-1, 1]
    normalized_x1 = (2 * x1 / width) - 1
    normalized_y1 = 1 - (2 * y1 / height)
    normalized_x2 = (2 * x2 / width) - 1
    normalized_y2 = 1 - (2 * y2 / height)

    return sqrt((normalized_x1 - normalized_x2)**2 + (normalized_y1 - normalized_y2)**2)

def isInCircle(circle_x, circle_y, ray_start_x, ray_start_y, circle_radius):
    dx = circle_x - ray_start_x
    dy = circle_y - ray_start_y
    distance = dx * dx + dy * dy
    if distance <= circle_radius * circle_radius:
        return True
    else:
        return False

# Callback for mouse button events
def mouse_button_callback(window, button, action, mods):
    x, y = glfw.get_cursor_pos(window)

    distance_to_circleR = distance(x, y, circleR_x, circleR_y, 1000, 1000)
    distance_to_circleB = distance(x, y, circleB_x, circleB_y, 1000, 1000)

    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        print(x, y)
        print("Left mouse button pressed!")
        print(str(distance_to_circleB) + " BLK DIST")
        print(str(distance_to_circleR) + " RED DIST")

        if isInCircle(circleR_x, circleR_y, x, y, 0.047):
            print("Mouse is within the red circle!")

        # Check if the mouse is within the black circle
        if isInCircle(circleB_x, circleB_y, x, y, 0.05):
            print("Mouse is within the black circle!")

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

# Initial positions of the two circles
circleR_x, circleR_y = 0.2, 0.2
circleB_x, circleB_y = 0.2, 0.2

# Main loop
while not glfw.window_should_close(window):
    # Clear the screen with a light blue color
    glClearColor(0.870, 0.905, 0.937, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    
    sides = 32
    radius = 0.05

    # Draw black first
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 0.0)
    for i in range(sides):
        angle = 2 * pi * i / sides
        x = radius * cos(angle) + circleB_x
        y = radius * sin(angle) + circleB_y
        glVertex2f(x, y)
    glEnd()

    # Draw red on top
    radius = 0.047
    glBegin(GL_POLYGON)
    glColor3f(0.807, 0.0, 0.0)
    for i in range(sides):
        angle = 2 * pi * i / sides
        x = radius * cos(angle) + circleR_x
        y = radius * sin(angle) + circleR_y
        glVertex2f(x, y)
    glEnd()

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

# Terminate GLFW
glfw.terminate()
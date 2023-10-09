import glfw
import math
from OpenGL.GL import *


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
window = glfw.create_window(1000, 1000, "Red Balls", None, None)
if not window:
    glfw.terminate()
    exit()

# Make the window's context current
glfw.make_context_current(window)

# Set callbacks
glfw.set_mouse_button_callback(window, mouse_button_callback)
glfw.set_key_callback(window, key_callback)

# Main loop
while not glfw.window_should_close(window):
    # Clear the screen with black color
    # glClearColor(1.0, 1.0, 1.0, 1.0)

    width, height = glfw.get_window_size(window)
    glViewport(0, 0, width, height)

    # Set color to lightly salted lays chips blue
    glClearColor(0.870, 0.905, 0.937, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    asp_ratio = width / height  # tried to fix circle size with ratio

    # Draw a circle radius 1
    x = float(0)
    y = float(0)
    PINum = 3.14159265358979323846
    radius = 1/50
    bRad = 1/45
    triangleAmnt = int(1000)
    twicePi = float(2.0*PINum)  # not multiplying results in half circle
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 0.0)  # black circle color
    glVertex2f(x, y)
    for i in range(triangleAmnt + 1):
        glVertex2f(
            x + (bRad * math.cos(i * twicePi / triangleAmnt)),
            y + (bRad * math.sin(i * twicePi / triangleAmnt))
        )
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.807, 0.0, 0.0)  # red circle color
    glVertex2f(x, y)
    for i in range(triangleAmnt + 1):
        glVertex2f(
            x + (radius * math.cos(i * twicePi / triangleAmnt)),
            y + (radius * math.sin(i * twicePi / triangleAmnt))
        )
    glEnd()

    a = float(0.2)
    b = float(0.2)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 0.0)  # black circle color
    glVertex2f(a, b)
    for i in range(triangleAmnt + 1):
        glVertex2f(
            a + (bRad * math.cos(i * twicePi / triangleAmnt)),
            b + (bRad * math.sin(i * twicePi / triangleAmnt))
        )
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.807, 0.0, 0.0)  # red circle color
    glVertex2f(a, b)
    for i in range(triangleAmnt + 1):
        glVertex2f(
            a + (radius * math.cos(i * twicePi / triangleAmnt)),
            b + (radius * math.sin(i * twicePi / triangleAmnt))
        )
    glEnd()

    # Draw a white square
    # glColor3f(1.0, 1.0, 1.0)  # Set color to white
    # glBegin(GL_QUADS)
    # glVertex2f(-0.5, -0.5)
    # glVertex2f(0.5, -0.5)
    # glVertex2f(0.5, 0.5)
    # glVertex2f(-0.5, 0.5)
    # glEnd()

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

# Terminate GLFW
glfw.terminate()

import glfw
import math
import random
from OpenGL.GL import *

num_balls = 300
radius = 0.02
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

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

def calculate_avoidance_force(x1, y1, x2, y2):
    max_avoidance_distance = 0.1
    discDistance = distance(x1, y1, x2, y2)
    if discDistance < max_avoidance_distance:
        # calculate avoidance force
        force_x = (x1 - x2) / discDistance
        force_y = (y1 - y2) / discDistance
        return (force_x, force_y)
    else:
        return (0.0, 0.0)
    
# fps function
frame_count = 0
last_time = glfw.get_time()
average_fps, total_frames = 0, 0
def fpscounter():
    global frame_count, last_time, average_fps, total_frames
    current_time = glfw.get_time()
    frame_count += 1
    total_frames += 1

    if current_time - last_time >= 1.0:
        average_fps = (average_fps * (total_frames - 1) + frame_count) / total_frames
        # Print FPS and reset counters
        print(f"FPS: {frame_count} | Average FPS: {average_fps:.2f}")
        frame_count = 0
        last_time = current_time

# Initialize the library
if not glfw.init():
    exit()
# Create a windowed mode window and its OpenGL context
window = glfw.create_window(1000, 1000, "Crowd Avoid", None, None)
if not window:
    glfw.terminate()
    exit()
# Make the window's context current
glfw.make_context_current(window)
# Set callbacks
glfw.set_mouse_button_callback(window, mouse_button_callback)
glfw.set_key_callback(window, key_callback)

xCoordinates, yCoordinates = [], []
velocityX, velocityY = [], []

for i in range(num_balls):
    xCircleCoord = -1 + 2 * random.random()
    yCircleCoord = -1 + 2 * random.random()
    xCoordinates.append(xCircleCoord)
    yCoordinates.append(yCircleCoord)

for i in range(num_balls):
    xCircleDirection = -0.001 + 0.002 * random.random()
    yCircleDirection = -0.001 + 0.002 * random.random()
    velocityX.append(xCircleDirection)
    velocityY.append(yCircleDirection)

TIME_STEP = 0.01

while not glfw.window_should_close(window):
    width, height = glfw.get_window_size(window)
    glViewport(0, 0, width, height)
    # Set background to lightly salted lays chips blue
    glClearColor(0.870, 0.905, 0.937, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    for i in range(num_balls):

        locationX = xCoordinates[i]
        locationY = yCoordinates[i]
        locationX += velocityX[i]
        locationY += velocityY[i]
        # transport to other side
        if(locationX > 1):
            locationX = -1
        if(locationY > 1):
            locationY = -1
        if(locationX < -1):
            locationX = 1
        if(locationY < -1):
            locationY = 1
        # movement to circles
        xCoordinates[i] = locationX
        yCoordinates[i] = locationY

    numSides = 40
    pi=3.14159265358979323846
    avoidForces = []

    # Build Spatial Hash
    spatialHash= {}
    cell_size = 6*radius
    for i in range(num_balls):
        X = round(xCoordinates[i]/cell_size)*cell_size
        Y = round(yCoordinates[i]/cell_size)*cell_size
        key = str(X)+","+str(Y)
        try:
            spatialHash[key]+=[i]
        except:
            spatialHash.update({key:[i]})
    
    ###########################################################################################
    # Running without this code gives ~30fps, the goal is to use sHash to get as close to that as possible. (or at least better than 10)
    for key in spatialHash:
        for i in spatialHash[key]:
            avoidance_force_x = 0.0
            avoidance_force_y = 0.0

            for j in spatialHash[key]:
                if i != j:
                    force_x, force_y = calculate_avoidance_force(xCoordinates[i], yCoordinates[i], xCoordinates[j], yCoordinates[j])
                    avoidance_force_x += force_x
                    avoidance_force_y += force_y
            # update velocity/position for avoidance forces
            velocityX[i] += avoidance_force_x * 0.00001
            velocityY[i] += avoidance_force_y * 0.00001
            xCoordinates[i] += velocityX[i] * TIME_STEP
            yCoordinates[i] += velocityY[i] * TIME_STEP

            avoidForces.append((avoidance_force_x, avoidance_force_y))

    # IT HITS 27 FPS LETS GOOOOOOOOOO
    ###########################################################################################

    # for loop to draw num_balls circles
    for i in range(num_balls):
        locationX = xCoordinates[i]
        locationY = yCoordinates[i]
        avoidance_force_x, avoidance_force_y = avoidForces[i]

        glBegin(GL_POLYGON)
        glColor3f(0.807, 0.0, 0.0)
        for i in range(numSides+1):
            twicePi = 2 * pi * i / numSides
            x = radius * math.cos(twicePi) + locationX
            y = radius * math.sin(twicePi) + locationY
            glVertex2f(x,y)
        glEnd()

        glLineWidth(2)
        glBegin(GL_LINE_STRIP)
        glColor3f(0.0, 0.0, 0.0)
        for i in range(numSides+1):
            twicePi = 2 * pi * i / numSides
            x = radius * math.cos(twicePi) + locationX
            y = radius * math.sin(twicePi) + locationY
            glVertex2f(x,y)
        glEnd()

    fpscounter()
    # Swap front and back buffers
    glfw.swap_buffers(window)
    # Poll for and process events
    glfw.poll_events()
# Terminate GLFW
glfw.terminate()

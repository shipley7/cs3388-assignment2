from OpenGL.GL import *
import glfw
import sys
import random

# just to make sure the correct number of arguments are put in
if (len(sys.argv) != 4):
    sys.exit("Wrong number of arguments, try again")

glfw.init()
window = glfw.create_window(int(sys.argv[2]), int(sys.argv[3]), "Chaos Game", None, None)  # making window as requested
glfw.make_context_current(window)

# used to set the viewing volume as requested
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-1.1, 1.1, -1.1, 1.1, -1, 1)

glClearColor(1.0, 1.0, 1.0, 1.0) # setting background color to white
glClear(GL_COLOR_BUFFER_BIT)

cornerCoordinates = [0,0]   # list used to hold the current coordinates of a corner
pointCoordinates = [0,0]    # list used to hold the current coordinates of a point

previousCorner = random.randint(1,4)    # we select an integer which picks the starting corner

if (previousCorner == 1):   # bottom left corner
    cornerCoordinates[0] = -1.0
    cornerCoordinates[1] = -1.0
elif (previousCorner == 2): # bottom right corner
    cornerCoordinates[0] = 1.0
    cornerCoordinates[1] = -1.0
elif (previousCorner == 3): # top left corner
    cornerCoordinates[0] = -1.0
    cornerCoordinates[1] = 1.0
elif (previousCorner == 4): # top right corner
    cornerCoordinates[0] = 1.0
    cornerCoordinates[1] = 1.0

pointCoordinates[0] = random.uniform(-1.0,1.0)  # getting an x-coordinate within the range of -1.0 to 1.0
pointCoordinates[1] = random.uniform(-1.0,1.0)  # getting a y-coordinate within the range of -1.0 to 1.0

# just in case the float returned is exactly -1.0 or 1.0 (needs to be in between)
while (pointCoordinates[0] == -1.0 or pointCoordinates[0] == 1.0):
    pointCoordinates[0] = random.uniform(-1.0,1.0)

# just in case the float returned is exactly -1.0 or 1.0 (needs to be in between)
while (pointCoordinates[1] == -1.0 or pointCoordinates[1] == 1.0):
    pointCoordinates[1] = random.uniform(-1.0,1.0)

glColor3f(0,0,0)    # setting color to black
glPointSize(2.0)    # using requested point size
glBegin(GL_POINTS)  # begin outside for loop to save time

# loop to plot all of the points
for x in range (1, int(sys.argv[1]) + 1):
    newCornerGenerator = random.randint(1,3)    # randomly select a new corner
    if (previousCorner == 1):   # ci-1 was bottom left corner
        if (newCornerGenerator == 1):   # bottom left corner
            cornerCoordinates[0] = -1.0
            cornerCoordinates[1] = -1.0
            previousCorner = 1  
        elif (newCornerGenerator == 2): # bottom right corner
            cornerCoordinates[0] = 1.0
            cornerCoordinates[1] = -1.0
            previousCorner = 2
        elif (newCornerGenerator == 3): # top left corner
            cornerCoordinates[0] = -1.0
            cornerCoordinates[1] = 1.0
            previousCorner = 3
    elif (previousCorner == 2): # ci-1 was bottom right corner
        if (newCornerGenerator == 1):   # bottom left corner
            cornerCoordinates[0] = -1.0
            cornerCoordinates[1] = -1.0
            previousCorner = 1
        elif (newCornerGenerator == 2): # bottom right corner
            cornerCoordinates[0] = 1.0
            cornerCoordinates[1] = -1.0
            previousCorner = 2
        elif (newCornerGenerator == 3): # top right corner
            cornerCoordinates[0] = 1.0
            cornerCoordinates[1] = 1.0
            previousCorner = 4
    elif (previousCorner == 3): # ci-1 was top left corner
        if (newCornerGenerator == 1):   # bottom left corner
            cornerCoordinates[0] = -1.0
            cornerCoordinates[1] = -1.0
            previousCorner = 1
        elif (newCornerGenerator == 2): # top left corner
            cornerCoordinates[0] = -1.0
            cornerCoordinates[1] = 1.0
            previousCorner = 3
        elif (newCornerGenerator == 3): # top right corner
            cornerCoordinates[0] = 1.0
            cornerCoordinates[1] = 1.0
            previousCorner = 4
    elif (previousCorner == 4): # ci-1 was top right corner
        if (newCornerGenerator == 1):   # bottom right corner
            cornerCoordinates[0] = 1.0
            cornerCoordinates[1] = -1.0
            previousCorner = 2
        elif (newCornerGenerator == 2): # top left corner
            cornerCoordinates[0] = -1.0
            cornerCoordinates[1] = 1.0
            previousCorner = 3
        elif (newCornerGenerator == 3): # top right corner
            cornerCoordinates[0] = 1.0
            cornerCoordinates[1] = 1.0
            previousCorner = 4
        
    # in every case above, ci becomes ci-1

    pointCoordinates[0] = (pointCoordinates[0] + cornerCoordinates[0]) / 2.0    # new x-coordinate of point is midpoint of corner and point
    pointCoordinates[1] = (pointCoordinates[1] + cornerCoordinates[1]) / 2.0    # new y-coordinate of point is midpoint of corner and point

    # this is where we actually plot the points
    glVertex2f(pointCoordinates[0], pointCoordinates[1])

glEnd() # end outside the loop for plotting to save some time
glfw.swap_buffers(window)   # calling swap_buffers before entering the loop

# everything is outside the loop as requested
while not glfw.window_should_close(window):
    glfw.poll_events()

glfw.terminate()

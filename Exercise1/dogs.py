from OpenGL.GL import *
import glfw
import numpy as np

# reading the txt file
with open("dog.txt", "r") as file:
    dataString = file.read()  # read the data
    vertices = [float(x) for x in dataString.split()] # convert the read data into a list of floats

glfw.init()
window = glfw.create_window(600, 600, "Dogs", None, None)  # making window as requested
glfw.make_context_current(window)

# used to set the viewing volume as requested
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, 60, 0, 60, -1, 1)

glClearColor(1.0, 1.0, 1.0, 1.0) # setting background color to white

angleOfRotation = 0 # needed to rotate 1 degree

while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)    # coloring the view

    # just in case but I don't think this should affect anything
    if (angleOfRotation >= 360):
        angleOfRotation = 0
    
    # we will have 8 angles to deal with and they increase by 45 degrees each time
    for currentAngle in range(0, 360, 45):
        x = 30 + 25 * np.cos(np.radians(currentAngle)) # x-coordinate of the circle (centre 30 + radius of 25)
        y = 30 + 25 * np.sin(np.radians(currentAngle)) # y-coordinate of the circle (centre 30 + radius of 25)

        glMatrixMode(GL_MODELVIEW)  # as seen in lecture 5
        glLoadIdentity()    # as seen in lecture 5
        glTranslatef(x, y, 0)   # translating image on the circle
        glRotatef(angleOfRotation, 0, 0, 1) # rotating image
        glColor3f(0, 0, 0)  #set color to black
        glBegin(GL_LINE_STRIP)  #using immediate mode to draw the dog
        
        # use a for loop to draw the image
        for i in range(0, len(vertices), 2):
            glVertex2f(vertices[i], vertices[i+1])  # use the ith point for x and ith + 1 point for y as instructed
        
        glEnd() # done

    angleOfRotation += 1    # increase the angle by one degree so it rotates

    glfw.swap_buffers(window)

glfw.terminate()
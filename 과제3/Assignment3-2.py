import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gCamAng = 0.


def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([1., 0., 0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 1., 0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 0., 1.]))
    glEnd()


def drawBox(red=0, green=0, blue=0):
    glColor3ub(red, green, blue)
    glBegin(GL_QUADS)
    glVertex3fv(np.array([1, 1, 0.]))
    glVertex3fv(np.array([-1, 1, 0.]))
    glVertex3fv(np.array([-1, -1, 0.]))
    glVertex3fv(np.array([1, -1, 0.]))
    glEnd()


def render(camAng, count):
    glClear(GL_COLOR_BUFFER_BIT |
            GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    # set the current matrix to the identity matrix
    glLoadIdentity()
    # use orthogonal projection (multiply the current matrix by "projection" matrix - we'll see details later)
    glOrtho(-1, 1, -1, 1, -1, 1)
    # rotate "camera" position (multiply the current matrix by "camera" matrix - we'll see details later)
    gluLookAt(.1*np.sin(camAng), .1, .1*np.cos(camAng), 0, 0, 0, 0, 1, 0)

    drawFrame()

    # blue base transformation
    glPushMatrix()
    glTranslatef(-.5+(count % 360)*.003, 0, 0)

    # blue base drawing
    glPushMatrix()
    drawFrame()
    glScalef(.2, .2, .2)
    drawBox(blue=255)
    glPopMatrix()

    # red arm transformation
    glPushMatrix()
    glRotatef(count % 360, 0, 0, 1)
    glTranslatef(.5, 0, .01)

    # red arm drawing
    glPushMatrix()
    drawFrame()
    glScalef(.5, .1, .1)
    drawBox(red=255)
    glPopMatrix()

    # green arm transformation
    glPushMatrix()
    glTranslatef(.5, 0, .01)
    glRotatef(count % 360, 0, 0, 1)

    # green arm drawing
    glPushMatrix()
    drawFrame()
    glScalef(.2, .2, .2)
    drawBox(green=255)
    glPopMatrix()

    glPopMatrix()
    glPopMatrix()
    glPopMatrix()


def key_callback(window, key, scancode, action, mods):
    global gCamAng
    # rotate the camera when 1 or 3 key is pressed or repeated
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)


def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "2D Trans", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.swap_interval(2)

    count = 0
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(gCamAng, count)
        glfw.swap_buffers(window)
        count += 1

    glfw.terminate()


if __name__ == "__main__":
    main()

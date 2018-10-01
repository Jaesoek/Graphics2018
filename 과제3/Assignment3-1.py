import glfw
from OpenGL.GL import *
import numpy as np

gComposedM = np.identity(3)


def key_callback(window, key, scancode, action, mods):
    global gComposedM
    newMatrix = np.identity(3)

    # translate -0.1 in x direction(global)
    if key == glfw.KEY_Q and action == glfw.PRESS:
        th = np.radians(10)
        newMatrix[:-1, :-1] = np.array([[np.cos(th), -np.sin(th)],
                                       [np.sin(th), np.cos(th)]])
        gComposedM = newMatrix @ gComposedM
    # translate 0.1 in x direction(global)
    elif key == glfw.KEY_E and action == glfw.PRESS:
    # rotate 10 degree counterclockwise(local)
    elif key == glfw.KEY_A and action == glfw.PRESS:
    # rotate 10 degree clockwise(local)
    elif key == glfw.KEY_D and action == glfw.PRESS:
    # reset triangle with identity matrix
    elif key == glfw.KEY_1 and action == glfw.PRESS:
        gComposedM = np.identity(3)


def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0., 0.]))
    glVertex2fv(np.array([1., 0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0., 0.]))
    glVertex2fv(np.array([0., 1.]))
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv((T@np.array([0., 0.5, 1.])[:-1])
    glVertex2fv((T@np.array([0., 0., 1.])[:-1])
    glVertex2fv((T@np.array([0.5, 0., 1.])[:-1])
    glEnd()


def main():
    if not glfw.init():
        return
    window=glfw.create_window(640, 640, "2D Trans", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)

    glfw.make_context_current(window)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(gComposedM)
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()

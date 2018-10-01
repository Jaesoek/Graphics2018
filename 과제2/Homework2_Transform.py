import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gComposedM = np.identity(3)

def key_callback(window, key, scancode, action, mods) :
    global gComposedM
    newMatrix = np.identity(3)

    # scale 0.9 in x    
    if key == glfw.KEY_W and action == glfw.PRESS:        
        newMatrix[:-1,:-1] = np.array([[0.9, 0.],[0., 1.]])
        gComposedM = newMatrix @ gComposedM
    # scale 1.1 in x    
    elif key == glfw.KEY_E and action == glfw.PRESS:
        newMatrix[:-1,:-1] = np.array([[1.1, 0.],[0., 1.]])
        gComposedM = newMatrix @ gComposedM
    # rotate 10 degree counterclockwise
    elif key == glfw.KEY_S and action == glfw.PRESS:
        th = np.radians(10)
        newMatrix[:-1,:-1] = np.array([[np.cos(th), -np.sin(th)],
                                       [np.sin(th), np.cos(th)]])
        gComposedM = newMatrix @ gComposedM
    # rotate 10 degree clockwise
    elif key == glfw.KEY_D and action == glfw.PRESS:
        th = np.radians(-10)
        newMatrix[:-1,:-1] = np.array([[np.cos(th), -np.sin(th)],
                                       [np.sin(th), np.cos(th)]])
        gComposedM = newMatrix @ gComposedM
    # shear -0.1 in x direction
    elif key == glfw.KEY_X and action == glfw.PRESS:
        newMatrix[:-1,:-1] = np.array([[1., -0.1],[0., 1.]])
        gComposedM = newMatrix @ gComposedM
    # shear 0.1 in x direction
    elif key == glfw.KEY_C and action == glfw.PRESS:
        newMatrix[:-1,:-1] = np.array([[1., 0.1],[0., 1.]])
        gComposedM = newMatrix @ gComposedM
    # reflection across x axis
    elif key == glfw.KEY_R and action == glfw.PRESS:
        newMatrix[:-1,:-1] = np.array([[1., 0.],[0., -1.]])
        gComposedM = newMatrix @ gComposedM
    # reset triangle with identity matrix
    elif key == glfw.KEY_1 and action == glfw.PRESS:
        gComposedM = np.identity(3)
        

def render(T):
    glClear(GL_COLOR_BUFFER_BIT |
            GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_LINES)
    glColor3ub(255,0,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0,255,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3ub(255,255,255)
    glVertex2fv((T @ np.array([0.,0.5,1.]))[:-1])
    glVertex2fv((T @ np.array([0.,0.,1.]))[:-1])
    glVertex2fv((T @ np.array([0.5,0.,1.]))[:-1])
    glEnd()


def main():
    if not glfw.init():
        return
    window = glfw.create_window(640,640,"2D Trans", None, None)
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

if __name__ =="__main__":
    main()


    

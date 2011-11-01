from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClearColor(0.5, 0.5, 0.5, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON);
    glColor3d(1.0, 0.0, 0.0);
    glVertex2d(-0.9, -0.9);
    glColor3d(1.0, 0.0, 0.0);
    glVertex2d(0.9, -0.9);
    glColor3d(0.0, 1.0, 0.0);
    glVertex2d(0.9, 0.9);
    glColor3d(0.0, 1.0, 0.0);
    glVertex2d(-0.9, 0.9);
    glEnd();
    glFlush()
    glutSwapBuffers()

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(320,240)
    glutCreateWindow("TEXTAREA")
    glutDisplayFunc(display)

init()
glutMainLoop()

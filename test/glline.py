from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClearColor(0.5, 0.5, 0.5, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3d(1.0, 0.0, 0.0);
    glBegin(GL_LINE_LOOP);
    glVertex2d(-0.9, -0.9);
    glVertex2d(0.9, -0.9);
    glVertex2d(0.9, 0.9);
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

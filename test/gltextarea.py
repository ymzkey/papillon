from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    pass

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(320,240)
    glutCreateWindow("TEXTAREA")
    glutDisplayFunc(display)

init()
glutMainLoop()

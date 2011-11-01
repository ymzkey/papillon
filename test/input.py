import threading
import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *

class Control(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def gl_init(self):
        def display():
            r = random.random
            glClearColor(0.5, 0.5, 0.5, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glBegin(GL_POLYGON);
            glColor3d(r(), r(), r());
            glVertex2d(-0.9, -0.9);
            glColor3d(r(), r(), r());
            glVertex2d(0.9, -0.9);
            glColor3d(r(), r(), r());
            glVertex2d(0.9, 0.9);
            glColor3d(r(), r(), r());
            glVertex2d(-0.9, 0.9);
            glEnd();
            glFlush()
            glutSwapBuffers()

        def key(key,x,y):
            glRasterPos3f(0,0,0);
            font = GLUT_BITMAP_TIMES_ROMAN_24
            glutBitmapCharacter(font, 1)
            glutPostRedisplay()

        def idle():
            time.sleep(1.0/6.0)
            glutPostRedisplay()

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(320,240)
        glutCreateWindow("1")
        glutDisplayFunc(display)
        glutKeyboardFunc(key);
        glutIdleFunc(idle)


    def run(self):
        self.gl_init()
        glutMainLoop()

cnt = Control()
cnt.start()

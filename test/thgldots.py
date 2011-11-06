import threading
import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *

class Genelaator(threading.Thread):
    def __init__(self,l):
        threading.Thread.__init__(self)
        self.l = l

    def run(self):
        while True:
            rand = (lambda: (random.randint(0,100) - 50.0)/100)

            x = rand()
            y = rand()
            self.l.append((x,y))
            while len(self.l) >= 20:
                self.l.pop(0)

class Printer(threading.Thread):
    def __init__(self,l):
        threading.Thread.__init__(self)
        self.l = l

    def gl_init(self):
        def putDot():
            glPointSize(5)
            glColor3d(1, .3, .3);
            glBegin(GL_POINTS)
            for dot in self.l:
                print dot[0],dot[1]
                glVertex2d(dot[0],dot[1])
            glEnd()

        def display():
            r = random.random
            glClearColor(0.5, 0.5, 0.5, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glBegin(GL_LINE_LOOP);
            glColor3d(r(), r(), r());
            glVertex2d(-0.9, -0.9);
            glColor3d(r(), r(), r());
            glVertex2d(0.9, -0.9);
            glColor3d(r(), r(), r());
            glVertex2d(0.9, 0.9);
            glColor3d(r(), r(), r());
            glVertex2d(-0.9, 0.9);
            glEnd()
            putDot()
            glFlush()
            glutSwapBuffers()

        def key(key,x,y):
            glutPostRedisplay()

        def idle():
            glutPostRedisplay()


        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(320,240)
        glutCreateWindow("dots")
        glutDisplayFunc(display)
        glutKeyboardFunc(key);
        glutIdleFunc(idle)


    def run(self):
        self.gl_init()
        glutMainLoop()

l = []
prt = Printer(l)
gen = Genelaator(l)
gen.start()
prt.start()


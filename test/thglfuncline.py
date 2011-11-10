import threading
import random
import math
import time
from OpenGL.GL import *
from OpenGL.GLUT import *

class Genelaator(threading.Thread):
    def __init__(self,l):
        threading.Thread.__init__(self)
        self.l = l
        self.i = 0

    def run(self):
        while True:
            seed = self.i / 100.0
            self.i = self.i + 1
            x = -0.5 + seed
            y = (seed*seed) % 2.0
            self.l.append((x,y))
            while len(self.l) > 200:
                self.l.pop(0)

            time.sleep(1.0/60.0)

class Printer(threading.Thread):
    def __init__(self,l):
        threading.Thread.__init__(self)
        self.l = l

    def gl_init(self):
        def putDot():
            glPointSize(10)
            glColor3d(1, .3, .3);
            glBegin(GL_LINES)
            if len(self.l) > 0:
                doto = self.l[0]
            ind = 0
            for dot in self.l:
                x1 =ind/100.0 + -1
                x2 =(ind+1)/100.0 + -1
                glVertex2d(x1,doto[1])
                glVertex2d(x2,dot[1])
                doto = dot
                ind = ind+1
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
            time.sleep(1.0/60.0)

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


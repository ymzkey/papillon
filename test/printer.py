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

            units = []
            for i in range(0,10):
                x = rand()
                y = rand()
                unit = {"x":x,"fitness":y}
                units.append(unit)
            self.l.append(units)
            while len(self.l) >= 20:
                self.l.pop(0)

class Printer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def gl_init(self):
        def putDot():
            glPointSize(4)
            glColor3d(1.0,0.0,0.0)
            if len(self.queue) > 0:
                units = self.queue.pop(0)
                glBegin(GL_POINTS)
                for unit in units:
                    x = unit["x"] * 10
                    y = unit["fitness"] * 10
                    glVertex2d(x,y)
                glEnd()

        def display():
            glClearColor(0.5, 0.5, 0.5, 0.0)
            glColor3d(1,0.1,1.0);
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glBegin(GL_LINE_LOOP);
            glVertex2d(-0.9, -0.9);
            glVertex2d(0.9, -0.9);
            glVertex2d(0.9, 0.9);
            glVertex2d(-0.9, 0.9);
            glEnd()
            putDot()
            glFlush()
            glutSwapBuffers()

        def key(key,x,y):
            glutPostRedisplay()

        def idle():
            time.sleep(10.0/60.0)
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

if __name__ == "__main__":
    l = []
    prt = Printer(l)
    gen = Genelaator(l)
    gen.start()
    prt.start()

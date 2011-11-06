class Fin():
    def __init__(self):
        self.fin = 'fin'
        
    def first(self):
        pass

    def second(self):
        pass
    
    def third(self):
        pass

    def run(self):
        self.first()
        self.second()
        self.third()


class Finfin(Fin):
    def __init__(self):
        Fin.__init__(self)
        self.finfin = 'finfin'

    def first(self):
        'f'

    def second(self):
        print self.fin

    def third(self):
        print self.finfin

ff = Finfin()
ff.run()

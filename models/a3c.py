from models.a2c import a2c

class a3c(a2c):
    def __init__(self):
        a2c.__init__(self)
    def getName(self):
        return self.__class__.__name__

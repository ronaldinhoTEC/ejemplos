# CLASSMETHOD

class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes
    def __repr__(self):
        return f'Pastel({self.ingredientes !r})'

    @classmethod
    def pastel_chocolate(cls):
        return cls(['harina','lechemin','chocolate'])
    @classmethod
    def pastel_vainilla(cls):
        return cls(['harina','lechemin','vainilla'])

print(Pastel.pastel_chocolate())

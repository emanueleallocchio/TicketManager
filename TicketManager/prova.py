

class Animale:

    def __init__(self, tipo):
        self.tipo = tipo





class CambiaAnimale:   

    def __init__(self, animale):
        self.animale = animale

    def cambio_tipo (self, nuovo_tipo):
        self.animale.tipo = nuovo_tipo




#tipo = "pesce"

#animale1 = Animale(tipo = tipo)


#cambiatore = CambiaAnimale(animale1)

#print(animale1.tipo)

#cambiatore.cambio_tipo("cane")

#print(animale1.tipo)

#print(tipo)

animale = Animale(tipo="pesce")

print(animale.tipo)



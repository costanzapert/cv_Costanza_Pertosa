# Classe base
class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print(f"{self.nome} fa suono generico.")

    # Classe derivata (eredita da Animale)
class Cane(Animale):

    def parla(self):
        print(f"{self.nome} abbaia!")

animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla() # Output: AnimaleGenerico fa suono generico.
cane.parla() # Output: Fido abbaia!
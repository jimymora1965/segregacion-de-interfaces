from abc import ABC, abstractmethod

class Mamifero(ABC):
    @abstractmethod
    def mamifero(self):
        pass

class Herbivoro(ABC):
    @abstractmethod
    def herbivoro(self):
        pass

class Omnivoro(ABC):
    @abstractmethod
    def omnivoro(self):
        pass

class Leon(Mamifero):
    def mamifero(self):
        print("El león toma leche")

class Vaca(Herbivoro):
    def herbivoro(self):
        print("La vaca es un animal herbívoro")

class Cerdo(Omnivoro):
    def omnivoro(self):
        print("Los cerdos son omnívoros")

leon = Leon()
leon.mamifero()
vaca = Vaca()
vaca.herbivoro()
cerdo = Cerdo()
cerdo.omnivoro()
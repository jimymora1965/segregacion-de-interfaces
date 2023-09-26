# Con la segregacion de interfaces, podemos utilizar metodos en diferentes clases para que puedan ser usados.
# por ejemplo un trabajador come, trabaja, duerme. Un robot solo trabaja. Entonces debemos segregar la interfaz
# para que pueda utilizarse la clase principal en todas las clases hijas. Se segrega la interfaz en interfaces
#  mas pequeñas para poderlas utilizar dependiendo la clase. un humano come, duerme, trabaja.un robot solo trabaja.

from abc import ABC, abstractclassmethod

class Trabajador(ABC):

    @abstractclassmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Comedor, Durmiente, Trabajador):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")

humano = Humano()
humano.comer()
robot = Robot()
robot.trabajar()




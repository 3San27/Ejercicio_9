class Car:
    def __init__(self, marcacoche, modelocoche, combustible, cilindrada, wheel):
        self.marca = marcacoche
        self.modelo = modelocoche
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.wheel = wheel
        self.pos_x = 0
        self.pos_y = 0

    def move_to(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


    def move_incr(self, x, y):
        self.pos_x = self.pos_x + x
        self.pos_y += y

    def get_pos(self):
        return self.pos_x, self.pos_y

class Wheel:
    def __init__(self, ancho, rodadura, diametro):
        self.ancho = ancho
        self.rodadura = rodadura
        self.diametro = diametro
        self.presion = 0

    def set_pressure(self, presion):
        self.presion = presion

    def print_info(self):
        print("Dimensiones de la rueda: ", self.ancho, "/",  self.rodadura, "R", self.diametro)
        print("Presión de las rueda: ", self.presion, "bar")
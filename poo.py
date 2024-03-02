class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

    def encender(self):
        if not self.encendido:
            print("El carro esta encendido")
            self.encendido = True
        else:
            print("El carro ya esta encendido")

    def apagar (self):
        if self.encendido:
            print("El carro esta apagado")
        else:
            print("El carro ya esta apagado")

#Crear una instancia e la Carro
carrodeJulian = Carro("Camaro", 2022, "Negro")

print(carrodeJulian.marca).
from modelo import Vehiculos, Trenes


print("Recuerde que los primeros tres ingresos son de automoviles y los ultimos dos son de trenes")

class VerVehiculo():

    def imprimir(self):
        self.ObjetoVehiculo1 = Vehiculos()
        self.ObjetoVehiculo2 = Vehiculos()
        self.ObjetoVehiculo3 = Vehiculos()

        self.ObjetoTren1 = Trenes()
        self.ObjetoTren2 = Trenes()
        
        self.ObjetoVehiculo1.Registro()
        self.ObjetoVehiculo2.Registro()
        self.ObjetoVehiculo3.Registro()

        self.ObjetoTren1.Registro()
        self.ObjetoTren2.Registro()

        print(f'El primer vehiculo tiene estas caracteristicas: color: {self.ObjetoVehiculo1.color}, matricula: {self.ObjetoVehiculo1.matricula}, velocidad maxima: {self.ObjetoVehiculo1.velocidadmaxima}')

        print(f'El segundo vehiculo tiene estas caracteristicas: color: {self.ObjetoVehiculo2.color}, matricula {self.ObjetoVehiculo2.matricula}, velocidad maxima: {self.ObjetoVehiculo2.velocidadmaxima}')
        
        print(f'El tercer vehiculo tiene estas caracteristicas: color: {self.ObjetoVehiculo3.color}, matricula: {self.ObjetoVehiculo3.matricula}, velocidad maxima: {self.ObjetoVehiculo3.velocidadmaxima}')

        print(f'El primer tren tiene estas caracteristicas: color: {self.ObjetoTren1.color}, matricula: {self.ObjetoTren1.matricula}, velocidad maxima: {self.ObjetoTren1.velocidadmaxima}, peso: {self.ObjetoTren1.peso}, toneladas')

        print(f'El segundo tren tiene estas caracteristicas: color: {self.ObjetoTren2.color}, matricula: {self.ObjetoTren2.matricula}, velocidad maxima: {self.ObjetoTren2.velocidadmaxima}, peso: {self.ObjetoTren2.peso}, toneladas')

ObjVer = VerVehiculo()
ObjVer.imprimir()

class Vehiculos():
    def __init__(self, color = None, matricula = None, velocidadmaxima = None): #con None decimos que algo puede ser nulo, es decir, que puede faltar
         self.color = color
         self.matricula = matricula
         self.velocidadmaxima = velocidadmaxima

    def Registro(self):
            self.color = input("ingresar el color : ")
            self.matricula = input("ingrese la matricula: ")
            self.velocidadmaxima = int(input("ingrese la velocidad maxima: "))

class Trenes(Vehiculos):
      def __init__(self, color = None, matricula = None, velocidadmaxima = None, peso = None):
          super().__init__(color, matricula, velocidadmaxima) #con super accedemos a la otra clase desde la llamada clase hija
          self.peso = peso
     
      def Registro(self):
           super().Registro()
           self.peso = int(input("ingrese el peso: "))
          

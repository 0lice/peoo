class Circulo:
    def __init__(self, raio, pi):
        self.r = raio
        self.pi = pi

    @property
    def circunferencia(self):
        return 2 * self.pi * self.r
    
    @property
    def area(self):
        return self.pi * self.r ** 2


c = Circulo(5, 3.1)
print(f'a circunferência do seu círculo é {c.circunferencia}')
print(f'a área do seu círculo é {c.area}')

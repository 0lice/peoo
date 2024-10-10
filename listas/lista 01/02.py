class Viagem:
    def __init__(self, km, horas, minutos):
        self.d = km
        self.h = horas
        self.m = minutos

    @property
    def v_media(self):
        t = self.m / 60
        return self.d / t
    
v = Viagem(10, 2, 30)
print(f'a velocidade média da viagem é {v.v_media} km/h.')

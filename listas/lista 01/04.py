class Ingresso:
    def __init__(self, dia, horario):
        self.d = dia
        self.h = horario

    @property
    def valor(self):
        v = 0
        d1 = ['segunda', 'terça', 'quinta']
        d2 = ['quarta']
        d3 = ['sexta', 'sábado', 'domingo']
        if self.d in d1:
            v = 16
        elif self.d in d2:
            v = 8
        elif self.d in d3:
            v = 20
        if self.h <= 24 and self.h >= 17:
                v *= 2

        return f'o valor do seu ingresso será de R$ {v:.2f}'

i = Ingresso('segunda', 15)
print(i.valor)

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.fabricante = None

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


golf_gti = Carro('Golf GTI')
ea888 = Motor('EA888')
vw = Fabricante('Volkswagen')
golf_gti.motor = ea888.nome
golf_gti.fabricante = vw.nome
ea888.fabricante = vw.nome

print(f'o {golf_gti.nome} é fabricado pela {golf_gti.fabricante} com o \
{golf_gti.motor}!')
print(f'O {ea888.nome} é fabricado pela {ea888.fabricante} ')

print(f'o {golf_gti.nome} é fabricado pela {golf_gti.fabricante} com o \
{golf_gti.motor}!')
print(f'O {ea888.nome} é fabricado pela {ea888.fabricante} ')

print(f'o {golf_gti.nome} é fabricado pela {golf_gti.fabricante} com o \
{golf_gti.motor}!')
print(f'O {ea888.nome} é fabricado pela {ea888.fabricante} ')

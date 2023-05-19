# Parašyti klasę "Namas", kuri turėtų savybę "plotas" ir "verte". Padaryti taip, kad savybė "verte" koreguojama
# tik įvedus skaičių. Programoje naudoti dekoratorių @property.
class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.verte = verte
        self.__verte = verte

    def set_verte(self, nauja_verte):
        if nauja_verte < 0:
            print("verte negali buti neigiama")
        else: self.__verte = nauja_verte
    def get_verte(self):
        return self.__verte


jono_namas = Namas(30, 10000)
print(jono_namas.get_verte())

jono_namas.set_verte(-300000)
print(jono_namas.get_verte())
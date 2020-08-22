from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""
import random


class Constants(BaseConstants):
    name_in_url = 'sgg'
    players_per_group = None
    num_rounds = 1
    p1_1_fila = ["$2.000","$2.200","$2.600","$2.900","$3.500","$4.200","$5.300","$7.100","$10.800", "$21.800"]
    p2_1_fila = ["$2.000","$2.400","$3.000","$3.700","$4.700","$6.000","$8.000","$11.300","$18.000","$38.000"]
    p3_1_fila = ["$2.000","$3.300","$5.000","$7.100","$10.000","$14.000","$20.000","$30.000","$50.000","$110.000"]
    p4_1_fila = ["$2.000","$4.400","$7.500","$11.400","$16.700","$24.000","$35.000","$53.300","$90.000","$200.000"]
    probabilidad = [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]


class Subsession(BaseSubsession):
    def creating_session(self):
        for j in self.get_players():
            j.pregunta_pago = random.randint(1,4)
    
    def set_pago_jugadores(self):
        for j in self.get_players():
            j.set_pago()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sgg_p1 = models.StringField()
    sgg_p2 = models.StringField()
    sgg_p3 = models.StringField()
    sgg_p4 = models.StringField()
    pregunta_pago = models.IntegerField()

    def set_pago(self):
        print(self.__dict__)
        fila_pregunta_pago = int(getattr(self, "sgg_p"+str(self.pregunta_pago)))
        if random.random() < Constants.probabilidad[fila_pregunta_pago-1] :
            self.payoff = c(getattr(Constants,"p{}_1_fila".format(self.pregunta_pago))[fila_pregunta_pago-1].replace("$","").replace(".",""))
        else:
            self.payoff = c(0)


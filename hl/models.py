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
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hl'
    players_per_group = None
    num_rounds = 2
    pago_tarea1 = {"A":[c(26000),c(21000)],"B":[c(50000),c(1000)]}
    pago_tarea2 = {"A":[c(35000),c(14000)],"B":[c(63000),c(1000)]}


class Subsession(BaseSubsession):
    def creating_session(self):
        for j in self.get_players():
            j.tarea_inicial = random.randint(1,2)
            j.tarea_pago = random.randint(1,2)
            j.pregunta_pago = random.randint(1,10)
    
    def set_pago_jugadores(self):
        for j in self.get_players():
            j.set_pago()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        tarea_inicial = models.IntegerField()
        tarea_pago = models.IntegerField()
        pregunta_pago = models.IntegerField()
        for i in range(2):
            for j in range(10):
                # Holt&Laury_tarea#_pregunta#
                setattr(self,"hl_t{i}_p{j}".format(i=i+1,j=j+1), models.StringField()) #A/B
    
    def set_pago(self):
        if random.random() < self.pregunta_pago/10 :
            self.payoff = getattr(Constants,"pago_tarea{}".format(self.tarea_pago))[
                getattr(self, "hl_t{i}_p{j}".format(i=self.tarea_pago, j= self.pregunta_pago))
                ][0]
        else:
            self.payoff = getattr(Constants,"pago_tarea{}".format(self.tarea_pago))[
                getattr(self, "hl_t{i}_p{j}".format(i=self.tarea_pago, j= self.pregunta_pago))
                ][1]


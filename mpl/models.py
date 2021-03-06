from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import json
import numpy as np


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mpl'
    players_per_group = None
    num_rounds = 1
    semanas = 5
    pagos = {
        "p1" : [[50000, 0], [0,50000 ]] ,
        "p2" : [[45000, 0], [0,50000 ]],
        "p3" : [[40000, 0], [0,50000 ]],
        "p4" : [[35000, 0], [0,50000 ]],
        "p5" : [[30000, 0], [0,50000 ]],
        "p6" : [[25000, 0], [0,50000 ]],
        "p7" : [[45000, 0], [0,50000 ]],
        "p8" : [[40000, 0], [0,50000 ]],
        "p9" : [[35000, 0], [0,50000 ]],
        "p10": [[30000, 0], [0,50000 ]],
        "p11": [[25000, 0], [0,50000 ]],
        "p12": [[20000, 0], [0,50000 ]],
        "p13": [[50000, 0], [0,50000 ]],
        "p14": [[45000, 0], [0,50000 ]],
        "p15": [[40000, 0], [0,50000 ]],
        "p16": [[35000, 0], [0,50000 ]],
        "p17": [[30000, 0], [0,50000 ]],
        "p18": [[25000, 0], [0,50000 ]],
        "p19": [[45000, 0], [0,50000 ]],
        "p20": [[40000, 0], [0,50000 ]],
        "p21": [[35000, 0], [0,50000 ]],
        "p22": [[30000, 0], [0,50000 ]],
        "p23": [[25000, 0], [0,50000 ]],
        "p24": [[20000, 0], [0,50000 ]]
  }


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.pregunta_pago = random.randint(1,24)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    mpl_p1 = models.StringField()
    mpl_p2 = models.StringField()
    mpl_p3 = models.StringField()
    mpl_p4 = models.StringField()
    mpl_p5 = models.StringField()
    mpl_p6 = models.StringField()
    mpl_p7 = models.StringField()
    mpl_p8 = models.StringField()
    mpl_p9 = models.StringField()
    mpl_p10 = models.StringField()
    mpl_p11 = models.StringField()
    mpl_p12 = models.StringField()
    mpl_p13 = models.StringField()
    mpl_p14 = models.StringField()
    mpl_p15 = models.StringField()
    mpl_p16 = models.StringField()
    mpl_p17 = models.StringField()
    mpl_p18 = models.StringField()
    mpl_p19 = models.StringField()
    mpl_p20 = models.StringField()
    mpl_p21 = models.StringField()
    mpl_p22 = models.StringField()
    mpl_p23 = models.StringField()
    mpl_p24 = models.StringField()
    pregunta_pago = models.IntegerField()
    pago_hoy = models.CurrencyField(initial=0)
    pago_5 = models.CurrencyField(initial=0)
    pago_10 = models.CurrencyField(initial=0)
    pago_15 = models.CurrencyField(initial=0)

    def set_pago(self):
        if self.pregunta_pago < 7:
            self.pago_hoy = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"mpl_p"+str(self.pregunta_pago)))-1][0])
            self.pago_5 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"mpl_p"+str(self.pregunta_pago)))-1][1])
        elif self.pregunta_pago < 13:
            self.pago_hoy = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"mpl_p"+str(self.pregunta_pago)))-1][0])
            self.pago_10 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"mpl_p"+str(self.pregunta_pago)))-1][1])
        elif self.pregunta_pago < 19:
            self.pago_5 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"mpl_p"+str(self.pregunta_pago)))-1][0])
            self.pago_10 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"mpl_p"+str(self.pregunta_pago)))-1][1])
        else:
            self.pago_5 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"mpl_p"+str(self.pregunta_pago)))-1][0])
            self.pago_15 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"mpl_p"+str(self.pregunta_pago)))-1][1])



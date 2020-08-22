from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'CTB'
    players_per_group = None
    num_rounds = 1
    semanas = 5
    pagos = {
        "p1" : [[50000, 0], [40000, 10000], [30000, 20000], [20000, 30000], [10000, 40000], [0, 50000]] ,
        "p2" : [[45000, 0], [36000, 10000], [27000, 20000], [18000,30000],	[9000 , 40000], [0,50000 ]],
        "p3" : [[40000, 0], [32000, 10000], [24000, 20000], [16000,30000],	[8000 , 40000], [0,50000 ]],
        "p4" : [[35000, 0], [28000, 10000], [21000, 20000], [14000,30000],	[7000 , 40000], [0,50000 ]],
        "p5" : [[30000, 0], [24000, 10000], [18000, 20000], [12000,30000],	[6000 , 40000], [0,50000 ]],
        "p6" : [[25000, 0], [20000, 10000], [15000, 20000], [10000,30000],	[5000 , 40000], [0,50000 ]],
        "p7" : [[45000, 0], [36000, 10000], [27000, 20000], [18000,30000],	[9000 , 40000], [0,50000 ]],
        "p8" : [[40000, 0], [32000, 10000], [24000, 20000], [16000,30000],	[8000 , 40000], [0,50000 ]],
        "p9" : [[35000, 0], [28000, 10000], [21000, 20000], [14000,30000],	[7000 , 40000], [0,50000 ]],
        "p10": [[30000, 0], [24000, 10000], [18000, 20000], [12000,30000],	[6000 , 40000], [0,50000 ]],
        "p11": [[25000, 0], [20000, 10000], [15000, 20000], [10000,30000],	[5000 , 40000], [0,50000 ]],
        "p12": [[20000, 0], [16000, 10000], [12000, 20000], [8000 ,30000], [4000 , 40000], [0,50000 ]],
        "p13": [[50000, 0], [40000, 10000], [30000, 20000], [20000,30000],	[10000,	40000], [0, 50000]],
        "p14": [[45000, 0], [36000, 10000], [27000, 20000], [18000,30000],	[9000 , 40000], [0,50000 ]],
        "p15": [[40000, 0], [32000, 10000], [24000, 20000], [16000,30000],	[8000 , 40000], [0,50000 ]],
        "p16": [[35000, 0], [28000, 10000], [21000, 20000], [14000,30000],	[7000 , 40000], [0,50000 ]],
        "p17": [[30000, 0], [24000, 10000], [18000, 20000], [12000,30000],	[6000 , 40000], [0,50000 ]],
        "p18": [[25000, 0], [20000, 10000], [15000, 20000], [10000,30000],	[5000 , 40000], [0,50000 ]],
        "p19": [[45000, 0], [36000, 10000], [27000, 20000], [18000,30000],	[9000 , 40000], [0,50000 ]],
        "p20": [[40000, 0], [32000, 10000], [24000, 20000], [16000,30000],	[8000 , 40000], [0,50000 ]],
        "p21": [[35000, 0], [28000, 10000], [21000, 20000], [14000,30000],	[7000 , 40000], [0,50000 ]],
        "p22": [[30000, 0], [24000, 10000], [18000, 20000], [12000,30000],	[6000 , 40000], [0,50000 ]],
        "p23": [[25000, 0], [20000, 10000], [15000, 20000], [10000,30000],	[5000 , 40000], [0,50000 ]],
        "p24": [[20000, 0], [16000, 10000], [12000, 20000], [8000 ,30000], [4000, 40000], [0, 50000 ]]
  }


class Subsession(BaseSubsession):
    def creating_session(self):
        for j in self.get_players():
            j.pregunta_pago = random.randint(1,24)
    
    def set_pago_jugadores(self):
        for j in self.get_players():
            j.set_pago()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ctb_p1 = models.StringField()
    ctb_p2 = models.StringField()
    ctb_p3 = models.StringField()
    ctb_p4 = models.StringField()
    ctb_p5 = models.StringField()
    ctb_p6 = models.StringField()
    ctb_p7 = models.StringField()
    ctb_p8 = models.StringField()
    ctb_p9 = models.StringField()
    ctb_p10 = models.StringField()
    ctb_p11 = models.StringField()
    ctb_p12 = models.StringField()
    ctb_p13 = models.StringField()
    ctb_p14 = models.StringField()
    ctb_p15 = models.StringField()
    ctb_p16 = models.StringField()
    ctb_p17 = models.StringField()
    ctb_p18 = models.StringField()
    ctb_p19 = models.StringField()
    ctb_p20 = models.StringField()
    ctb_p21 = models.StringField()
    ctb_p22 = models.StringField()
    ctb_p23 = models.StringField()
    ctb_p24 = models.StringField()
    pregunta_pago = models.IntegerField()
    pregunta_actual = models.IntegerField(initial=0)
    pago_hoy = models.CurrencyField(initial=0)
    pago_5 = models.CurrencyField(initial=0)
    pago_10 = models.CurrencyField(initial=0)
    pago_15 = models.CurrencyField(initial=0)

    def get_pregunta_actual(self):
        self.pregunta_actual+=1
        return self.pregunta_actual
    
    def set_pago(self):
        if self.pregunta_pago < 7:
            self.pago_hoy = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"ctb_p"+str(self.pregunta_pago)))][0])
            self.pago_5 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"ctb_p"+str(self.pregunta_pago)))][1])
        elif self.pregunta_pago < 13:
            self.pago_hoy = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"ctb_p"+str(self.pregunta_pago)))][0])
            self.pago_10 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"ctb_p"+str(self.pregunta_pago)))][1])
        elif self.pregunta_pago < 19:
            self.pago_5 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"ctb_p"+str(self.pregunta_pago)))][0])
            self.pago_10 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"ctb_p"+str(self.pregunta_pago)))][1])
        else:
            self.pago_5 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"ctb_p"+str(self.pregunta_pago)))][0])
            self.pago_15 = c(Constants.pagos["p"+str(self.pregunta_pago)][int(getattr(self,"ctb_p"+str(self.pregunta_pago)))][1])

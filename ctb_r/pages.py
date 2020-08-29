import random
import json

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Bienvenido(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instrucciones(Page):
    def is_displayed(self):
        return self.round_number == 1

class Pregunta_1(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p1']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 1

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_2(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p2']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 2

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_3(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p3']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 3

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_4(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p4']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 4

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_5(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p5']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 5

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_6(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p6']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 6

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_7(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p7']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 7

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_8(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p8']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 8

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_9(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p9']

    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 9

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }
class Pregunta_10(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p10']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 10

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
            "pregunta": self.round_number,
        }

class Pregunta_11(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p11']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 11

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_12(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p12']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 12

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_13(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p13']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 13

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_14(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p14']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 14

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_15(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p15']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 15

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_16(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p16']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 16

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_17(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p17']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 17

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_18(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p18']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 18

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_19(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p19']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 19

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_20(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p20']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 20

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_21(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p21']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 21

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_22(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p22']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 22

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_23(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p23']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 23

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Pregunta_24(Page):
    form_model = 'player'
    form_fields = ['ctb_r_p24']
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 24

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])
        if(self.round_number == Constants.num_rounds):
            self.player.set_pago()

    def vars_for_template(self):
        return {
                "pregunta": self.round_number,
            }

class Resultados(Page):
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 1

    def vars_for_template(self):
        if self.player.pregunta_pago < 7:
            return {
                "pago_hoy" : "$"+format(int(str(self.player.pago_hoy).split(",")[0]),',d'),
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_10" : False,
                "pago_15" : False,
                "pregunta_pago" : json.loads(self.participant.vars['orden_preguntas']).index(self.player.pregunta_pago) + 1,
                "fila_pago" : getattr(self.player, "ctb_r_p"+str(self.player.pregunta_pago))
                
            }
        elif self.player.pregunta_pago < 13:
            return {
                "pago_hoy" : "$"+format(int(str(self.player.pago_hoy).split(",")[0]),',d'),
                "pago_10" : "$"+format(int(str(self.player.pago_10).split(",")[0]),',d'),
                "pago_5" : False,
                "pago_15" : False,
                "pregunta_pago" : json.loads(self.participant.vars['orden_preguntas']).index(self.player.pregunta_pago) + 1,
                "fila_pago" : getattr(self.player, "ctb_r_p"+str(self.player.pregunta_pago))
                
            }
        elif self.player.pregunta_pago < 19:
            return {
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_10" : "$"+format(int(str(self.player.pago_10).split(",")[0]),',d'),
                "pago_15" : False,
                "pago_hoy" : False,
                "pregunta_pago" : json.loads(self.participant.vars['orden_preguntas']).index(self.player.pregunta_pago) + 1,
                "fila_pago" : getattr(self.player, "ctb_r_p"+str(self.player.pregunta_pago))
                
            }
        else:
            return {
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_15" : "$"+format(int(str(self.player.pago_15).split(",")[0]), ',d'),
                "pago_hoy" : False,
                "pago_10" : False,
                "pregunta_pago" : json.loads(self.participant.vars['orden_preguntas']).index(self.player.pregunta_pago) + 1,
                "fila_pago" : getattr(self.player, "ctb_r_p"+str(self.player.pregunta_pago))
                
            }

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class Gracias(Page):
     def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [Instrucciones]

preguntas = [
    Pregunta_1,
    Pregunta_2,
    Pregunta_3,
    Pregunta_4,
    Pregunta_5,
    Pregunta_6,
    Pregunta_7,
    Pregunta_8,
    Pregunta_9,
    Pregunta_10,
    Pregunta_11,
    Pregunta_12,
    Pregunta_13,
    Pregunta_14,
    Pregunta_15,
    Pregunta_16,
    Pregunta_17,
    Pregunta_18,
    Pregunta_19,
    Pregunta_20,
    Pregunta_21,
    Pregunta_22,
    Pregunta_23,
    Pregunta_24
]

# random.shuffle(preguntas)

for p in preguntas:
    page_sequence.append(p)

# page_sequence.append(Calculos)
page_sequence.append(Resultados)
page_sequence.append(Gracias)
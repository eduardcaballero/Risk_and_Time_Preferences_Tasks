import random

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instrucciones(Page):
    pass

class Pregunta_1(Page):
    form_model = 'player'
    form_fields = ['ctb_p1']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_2(Page):
    form_model = 'player'
    form_fields = ['ctb_p2']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_3(Page):
    form_model = 'player'
    form_fields = ['ctb_p3']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_4(Page):
    form_model = 'player'
    form_fields = ['ctb_p4']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_5(Page):
    form_model = 'player'
    form_fields = ['ctb_p5']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_6(Page):
    form_model = 'player'
    form_fields = ['ctb_p6']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_7(Page):
    form_model = 'player'
    form_fields = ['ctb_p7']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_8(Page):
    form_model = 'player'
    form_fields = ['ctb_p8']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_9(Page):
    form_model = 'player'
    form_fields = ['ctb_p9']

    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }
class Pregunta_10(Page):
    form_model = 'player'
    form_fields = ['ctb_p10']
    def vars_for_template(self):
        return {
            "pregunta": self.player.get_pregunta_actual(),
        }

class Pregunta_11(Page):
    form_model = 'player'
    form_fields = ['ctb_p11']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_12(Page):
    form_model = 'player'
    form_fields = ['ctb_p12']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_13(Page):
    form_model = 'player'
    form_fields = ['ctb_p13']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_14(Page):
    form_model = 'player'
    form_fields = ['ctb_p14']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_15(Page):
    form_model = 'player'
    form_fields = ['ctb_p15']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_16(Page):
    form_model = 'player'
    form_fields = ['ctb_p16']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_17(Page):
    form_model = 'player'
    form_fields = ['ctb_p17']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_18(Page):
    form_model = 'player'
    form_fields = ['ctb_p18']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_19(Page):
    form_model = 'player'
    form_fields = ['ctb_p19']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_20(Page):
    form_model = 'player'
    form_fields = ['ctb_p20']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_21(Page):
    form_model = 'player'
    form_fields = ['ctb_p21']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_22(Page):
    form_model = 'player'
    form_fields = ['ctb_p22']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_23(Page):
    form_model = 'player'
    form_fields = ['ctb_p23']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Pregunta_24(Page):
    form_model = 'player'
    form_fields = ['ctb_p24']
    def vars_for_template(self):
        return {
                "pregunta": self.player.get_pregunta_actual(),
            }

class Calculos(WaitPage):
    def after_all_players_arrive(self):
        self.subsession.set_pago_jugadores()

    def is_displayed(self):
        return self.round_number == 1

class Gracias(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

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

random.shuffle(preguntas)

for p in preguntas:
    page_sequence.append(p)

page_sequence.append(Calculos)
page_sequence.append(Gracias)
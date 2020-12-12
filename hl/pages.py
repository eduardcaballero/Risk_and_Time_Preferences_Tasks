from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones(Page):
    def is_displayed(self):
        return self.round_number == 1

class Tarea1(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["hl_t1_p{}".format(i+1) for i in range(10)]

    def is_displayed(self):
        return (self.player.tarea_inicial == 1 and self.round_number == 1) or (self.player.tarea_inicial != 1 and self.round_number != 1)

class Tarea2(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["hl_t2_p{}".format(i+1) for i in range(10)]

    def is_displayed(self):
        return (self.player.tarea_inicial == 2 and self.round_number == 1) or (self.player.tarea_inicial != 2 and self.round_number != 1)

class Calculos(WaitPage):
    # def after_all_players_arrive(self):
    #     self.subsession.set_pago_jugadores()

    def is_displayed(self):
        return self.round_number == 2

class Resultados(Page):
    # def before_next_page(self):

    def is_displayed(self):
        self.subsession.set_pago_jugadores()
        self.participant.vars['hl_pago'] = {
            "pago": self.player.payoff, 
            "tarea_pago": self.player.tarea_pago, 
            "pregunta_pago": self.player.pregunta_pago
        }
        results = True
        if 'order' in self.participant.vars:
            results = False
        return self.round_number == 2 and results
    
    def vars_for_template(self):
        return {
            "pago": format(int(str(self.player.payoff).split(",")[0]), ',d'),
            "tarea_pago": self.player.tarea_pago, 
            "pregunta_pago": self.player.pregunta_pago
        }


# page_sequence = [Instrucciones, Tarea1, Tarea2, Calculos, Resultados]
page_sequence = [Instrucciones, Tarea1, Tarea2, Resultados]


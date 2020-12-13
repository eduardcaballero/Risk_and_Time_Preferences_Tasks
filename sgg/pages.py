from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones(Page):
    def is_displayed(self):
        app = True
        if 'order2' in self.participant.vars:
            if self.participant.vars['order2'] != 1:
                app = False
        return self.round_number == 1 and app

class Pregunta(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["sgg_p1"]

    def vars_for_template(self):
        return {
            "pregunta" : 1,
            }
    def is_displayed(self):
        app = True
        if 'order2' in self.participant.vars:
            if self.participant.vars['order2'] != 1:
                app = False
        return self.round_number == 1 and app

class Pregunta2(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["sgg_p2"]

    def vars_for_template(self):
        return {
            "pregunta" : 2,
            }
    def is_displayed(self):
        app = True
        if 'order2' in self.participant.vars:
            if self.participant.vars['order2'] != 1:
                app = False
        return self.round_number == 1 and app

class Pregunta3(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["sgg_p3"]

    def vars_for_template(self):
        return {
            "pregunta" : 3,
            }
    def is_displayed(self):
        app = True
        if 'order2' in self.participant.vars:
            if self.participant.vars['order2'] != 1:
                app = False
        return self.round_number == 1 and app

class Pregunta4(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["sgg_p4"]

    def vars_for_template(self):
        return {
            "pregunta" : 4,
            }
    def is_displayed(self):
        app = True
        if 'order2' in self.participant.vars:
            if self.participant.vars['order2'] != 1:
                app = False
        return self.round_number == 1 and app

# class Calculos(WaitPage):
    # def after_all_players_arrive(self):
    #     self.subsession.set_pago_jugadores()

    # def is_displayed(self):
    #     app = True
    #     self.subsession.set_pago_jugadores()
    #     if 'order2' in self.participant.vars:
    #         if self.participant.vars['order2'] != 1:
    #             app = False
    #     return self.round_number == 1 and app

class Resultados(Page):
    def vars_for_template(self):
        self.player.set_pago()
        return {
            "pago" : self.player.payoff,
            "pregunta" : self.player.pregunta_pago,
            "valor" : str(self.player.payoff).split(",")[0]
        }

    def is_displayed(self):
        self.participant.vars['sgg_pago'] = {
            "app" : "sgg",
            "pago" : self.player.payoff,
            "pregunta" : self.player.pregunta_pago,
            "valor" : str(self.player.payoff).split(",")[0]
        }
        app = True
        results = True
        if 'order2' in self.participant.vars:
            if self.participant.vars['order2'] != 1:
                app = False
            else:
                self.player.set_pago()
                results = False
        return self.round_number == 1 and app and results


page_sequence = [Instrucciones, Pregunta, Pregunta2, Pregunta3, Pregunta4, Resultados]

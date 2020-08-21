from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones(Page):
    def is_displayed(self):
        return self.round_number == 1

class Pregunta(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["sgg_p1"]

    def is_displayed(self):
        return self.round_number == 1

class Pregunta2(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["sgg_p2"]

    def is_displayed(self):
        return self.round_number == 1

class Pregunta3(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["sgg_p3"]

    def is_displayed(self):
        return self.round_number == 1

class Pregunta4(Page):
    # timeout_seconds = 90
    form_model = "player"
    form_fields = ["sgg_p4"]

    def is_displayed(self):
        return self.round_number == 1
# class Calculos(WaitPage):
#     def after_all_players_arrive(self):
#         self.subsession.set_pago_jugadores()

class Resultados(Page):
    def is_displayed(self):
        return self.round_number == 2



class Results(Page):
    pass


page_sequence = [Instrucciones, Pregunta, Pregunta2, Pregunta3, Pregunta4, Resultados]

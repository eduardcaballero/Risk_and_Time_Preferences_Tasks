from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Resultados(Page):
    def vars_for_template(self):
        return self.participant.vars['ctb_pago']
        


page_sequence = [Resultados]

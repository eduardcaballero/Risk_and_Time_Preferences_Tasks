from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Contrato(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Comparacion(Page):
    pass


page_sequence = [Contrato, Comparacion]

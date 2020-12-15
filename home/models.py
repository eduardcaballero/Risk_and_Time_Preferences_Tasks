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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'home'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consentimiento = models.BooleanField(
    choices=[
        [True, 'Acepto (declaro que comprendo la información anterior y mis derechos y compromisos durante este experimento. También entiendo que puedo dejar el experimento en cualquier momento renunciando a recibir el dinero ganado en el experimento)'],
        [False,'No Acepto'],
    ], label="ACEPTACIÓN")

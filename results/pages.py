from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import string    


class questions(Page):
    form_model = 'player'
    form_fields = ['p_risk','p1', 'p2', 'p3','p4', 'p5', 'p6','p7'] 

class thanks(Page):
    def vars_for_template(self): 
        return {
            "identificador" : self.participant.vars['identificador'],
            "round_payoff_total" : self.participant.vars['payoff_total'],
            "payoff_complete" : self.participant.vars['payoff_complete'],
            "round_payoff" : self.participant.vars['round_payoff']
            # "pago_total" : "$"+format(int(str(self.player.pago.to_real_world_currency(self.session)).split(",")[0]),',d')
        }

page_sequence = [questions, thanks]

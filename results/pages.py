from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import string    


class questions(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    form_model = 'player'
    form_fields = ['p_risk','p1', 'p2', 'p3','p4', 'p5', 'p6','p7'] 

class thanks(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self): 
        return {
            'identificador': self.player.in_round(1).identificador,
            self.player.round_payoff = self.participant.vars['round_payoff']- 1,
            self.player.round_payoff_total = self.participant.vars['payoff_total'],
            self.player.payoff_complete = self.participant.vars['payoff_complete'],
            # "pago_total" : "$"+format(int(str(self.player.pago.to_real_world_currency(self.session)).split(",")[0]),',d')
        }
        
page_sequence = [questions, thanks]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import string    


class questions(Page):
    form_model = 'player'
    form_fields = ['p_risk','p_sex', 'p_age', 'p_student', 'p_job', 'p_educ', 'p_educ1', 'p_ocupation', 'p_health', 'p_inc', 'p_pc', 'p_mouse'] 

class thanks(Page):
    def vars_for_template(self): 
        return {
            "identificador" : self.participant.vars['identificador'],
            "payoff_total" : "$"+format(int(str(self.participant.vars['payoff_total']).split(",")[0]),',d'),
            "payoff_complete" : "$"+format(int(str(self.participant.vars['payoff_complete']+(self.player.participant.vars["icl_pago"]*100)).split(",")[0]),',d'),
            "round_payoff" : self.participant.vars['round_payoff']
        }
        
page_sequence = [questions, thanks]

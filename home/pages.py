from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import string

class MyPage(Page):
     def before_next_page(self):
        # sequence 0 = [ctb,hl,mpl,bret], sequence 1 = [mpl_2,hl,ctb_2,bret]
        # self.participant.vars['app'] = True
        self.participant.vars['order'] = random.randint(0,1)
        cod = str(random.choice(string.ascii_lowercase)).upper()+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
        self.player.codigo = cod
        # print(self.participant.__dict__)
        # if self.participant.vars['app']:
        sequence = []
        if self.participant.vars['order']:
                sequence = ['mpl_2','hl','ctb_2','bret']
        else:
                sequence = ['ctb','hl','mpl','bret']
        self.participant.vars['app_to_pay'] = sequence[random.randint(0,3)]

class Consentimiento(Page):
    form_model = 'player'
    form_fields = ['consentimiento'] 


page_sequence = [Consentimiento, MyPage]

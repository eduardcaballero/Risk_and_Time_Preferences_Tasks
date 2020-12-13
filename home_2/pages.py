from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class MyPage(Page):
     def before_next_page(self):
        # sequence 0 = [ctb,hl,mpl,bret], sequence 1 = [mpl_2,hl,ctb_2,bret]
        self.participant.vars['app'] = False
        self.participant.vars['order'] = random.randint(0,1)
        self.participant.vars['order2'] = random.randint(0,1)
        # print(self.participant.__dict__)
        sequence = []
        if self.participant.vars['order']:
                if self.participant.vars['order2']:
                        sequence = ['mpl_2','hl','ctb_2','sgg','dm']
                else:
                        sequence = ['mpl_2','hl','ctb_2','bret','dm']
        else:
                if self.participant.vars['order2']:
                        sequence = ['ctb','hl','mpl','sgg','dm']
                else:
                        sequence = ['ctb','hl','mpl','bret','dm']
        self.participant.vars['app_to_pay'] = sequence[random.randint(0,4)]


page_sequence = [MyPage]


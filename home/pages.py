from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class MyPage(Page):
     def before_next_page(self):
        # sequence 0 = [ctb,hl,mpl,bret], sequence 1 = [mpl_2,hl,ctb_2,bret]
        self.participant.vars['order'] = random.randint(0,1)
        self.participant.vars['order2'] = random.randint(0,1)


page_sequence = [MyPage]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Resultados(Page):
    def vars_for_template(self):
        # sequence 0 = [ctb,hl,mpl,bret,dm], sequence 1 = [mpl_2,hl,ctb_2,bret,dm]
        # sequence 2 = [ctb,hl,mpl,sgg,dm], sequence 3 = [mpl_2,hl,ctb_2,sgg,dm]
        sequence = []
        print(self.participant.__dict__)
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
        app_to_pay = sequence[random.randint(0,4)]
        if app_to_pay == "ctb":
            return self.participant.vars['ctb_pago']
        elif app_to_pay == "ctb_2":
            return self.participant.vars['ctb2_pago']
        elif app_to_pay == "mpl":
            return self.participant.vars['mpl_pago']
        elif app_to_pay == "mpl_2":
            return self.participant.vars['mpl2_pago']
        elif app_to_pay == "hl":
            return self.participant.vars['hl_pago']
        elif app_to_pay == "bret":
            return self.participant.vars['bret_pago']
        elif app_to_pay == "sgg":
            return self.participant.vars['sgg_pago']
        else:
            return self.participant.vars['dm_pago']




        

page_sequence = [Resultados]

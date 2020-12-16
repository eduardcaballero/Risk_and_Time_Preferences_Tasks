from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Resultados(Page):
    def vars_for_template(self):
        # sequence 0 = [ctb,hl,mpl,bret,dm], sequence 1 = [mpl_2,hl,ctb_2,bret,dm]
        # sequence 2 = [ctb,hl,mpl,sgg,dm], sequence 3 = [mpl_2,hl,ctb_2,sgg,dm]
        self.player.app_pago = self.participant.vars['app_to_pay']
        if self.participant.vars['app_to_pay'] == "ctb":
            if self.participant.vars['ctb_pago']['pago_hoy']:
                self.player.pago = str(int(self.participant.vars['ctb_pago']['pago_hoy'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['ctb_pago']['pago_5']:
                self.player.pago_5 = str(int(self.participant.vars['ctb_pago']['pago_5'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['ctb_pago']['pago_10']:
                self.player.pago_10 = str(int(self.participant.vars['ctb_pago']['pago_10'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['ctb_pago']['pago_15']:
                self.player.pago_15 = str(int(self.participant.vars['ctb_pago']['pago_15'].split("$")[1].replace(',', ''))+5000)
            return self.participant.vars['ctb_pago']
        elif self.participant.vars['app_to_pay'] == "ctb_2":
            if self.participant.vars['ctb2_pago']['pago_hoy']:
                self.player.pago = str(int(self.participant.vars['ctb2_pago']['pago_hoy'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['ctb2_pago']['pago_5']:
                self.player.pago_5 = str(int(self.participant.vars['ctb2_pago']['pago_5'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['ctb2_pago']['pago_10']:
                self.player.pago_10 = str(int(self.participant.vars['ctb2_pago']['pago_10'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['ctb2_pago']['pago_15']:
                self.player.pago_15 = str(int(self.participant.vars['ctb2_pago']['pago_15'].split("$")[1].replace(',', ''))+5000)
            return self.participant.vars['ctb2_pago']
        elif self.participant.vars['app_to_pay'] == "mpl":
            if self.participant.vars['mpl_pago']['pago_hoy']:
                self.player.pago = str(int(self.participant.vars['mpl_pago']['pago_hoy'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['mpl_pago']['pago_5']:
                self.player.pago_5 = str(int(self.participant.vars['mpl_pago']['pago_5'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['mpl_pago']['pago_10']:
                self.player.pago_10 = str(int(self.participant.vars['mpl_pago']['pago_10'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['mpl_pago']['pago_15']:
                self.player.pago_15 = str(int(self.participant.vars['mpl_pago']['pago_15'].split("$")[1].replace(',', ''))+5000)
            return self.participant.vars['mpl_pago']
        elif self.participant.vars['app_to_pay'] == "mpl_2":
            if self.participant.vars['mpl2_pago']['pago_hoy']:
                self.player.pago = str(int(self.participant.vars['mpl2_pago']['pago_hoy'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['mpl2_pago']['pago_5']:
                self.player.pago_5 = str(int(self.participant.vars['mpl2_pago']['pago_5'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['mpl2_pago']['pago_10']:
                self.player.pago_10 = str(int(self.participant.vars['mpl2_pago']['pago_10'].split("$")[1].replace(',', ''))+5000)
            if self.participant.vars['mpl2_pago']['pago_15']:
                self.player.pago_15 = str(int(self.participant.vars['mpl2_pago']['pago_15'].split("$")[1].replace(',', ''))+5000)
            return self.participant.vars['mpl2_pago']
        elif self.participant.vars['app_to_pay'] == "hl":
            self.player.pago = str(int(self.participant.vars['hl_pago']['pago'].split("$")[1].replace(',', ''))+10000)
            return self.participant.vars['hl_pago']
        elif self.participant.vars['app_to_pay'] == "bret":
            self.player.pago = str(int(self.participant.vars['bret_pago']['total_payoff'].split("$")[1].replace(',', '').replace(',', ''))+10000)
            return self.participant.vars['bret_pago']
        elif self.participant.vars['app_to_pay'] == "sgg":
            
            return self.participant.vars['sgg_pago']
        else:
            return self.participant.vars['dm_pago']

class Formulario(Page):
    form_model = 'player'
    form_fields = ['p1', 'p2', 'p3','p4', 'p5', 'p6','p7', 'p8', 'p9','p10', 'p11', 'p12'] 

class Fin(Page):
    pass

        

page_sequence = [Resultados, Formulario, Fin]

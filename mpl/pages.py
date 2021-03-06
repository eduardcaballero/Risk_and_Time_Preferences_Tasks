import random
import json

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Bienvenido(Page):
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

class Instrucciones(Page):
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

class Instrucciones_1a6(Page):
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

class Instrucciones_7a12(Page):
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

class Instrucciones_13a18(Page):
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

class Instrucciones_19a24(Page):
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

class Pregunta_1(Page):
    form_model = 'player'
    form_fields = ['mpl_p1']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 1,
        }
class Pregunta_2(Page):
    form_model = 'player'
    form_fields = ['mpl_p2']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 2,
        }
class Pregunta_3(Page):
    form_model = 'player'
    form_fields = ['mpl_p3']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 3,
        }
class Pregunta_4(Page):
    form_model = 'player'
    form_fields = ['mpl_p4']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 4,
        }
class Pregunta_5(Page):
    form_model = 'player'
    form_fields = ['mpl_p5']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 5,
        }
class Pregunta_6(Page):
    form_model = 'player'
    form_fields = ['mpl_p6']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 6,
        }
class Pregunta_7(Page):
    form_model = 'player'
    form_fields = ['mpl_p7']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 7,
        }
class Pregunta_8(Page):
    form_model = 'player'
    form_fields = ['mpl_p8']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 8,
        }
class Pregunta_9(Page):
    form_model = 'player'
    form_fields = ['mpl_p9']

    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 9,
        }
class Pregunta_10(Page):
    form_model = 'player'
    form_fields = ['mpl_p10']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
            "pregunta": 10,
        }

class Pregunta_11(Page):
    form_model = 'player'
    form_fields = ['mpl_p11']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 11,
            }

class Pregunta_12(Page):
    form_model = 'player'
    form_fields = ['mpl_p12']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 12,
            }

class Pregunta_13(Page):
    form_model = 'player'
    form_fields = ['mpl_p13']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 13,
            }

class Pregunta_14(Page):
    form_model = 'player'
    form_fields = ['mpl_p14']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 14,
            }

class Pregunta_15(Page):
    form_model = 'player'
    form_fields = ['mpl_p15']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 15,
            }

class Pregunta_16(Page):
    form_model = 'player'
    form_fields = ['mpl_p16']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 16,
            }

class Pregunta_17(Page):
    form_model = 'player'
    form_fields = ['mpl_p17']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 17,
            }

class Pregunta_18(Page):
    form_model = 'player'
    form_fields = ['mpl_p18']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 18,
            }

class Pregunta_19(Page):
    form_model = 'player'
    form_fields = ['mpl_p19']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 19,
            }

class Pregunta_20(Page):
    form_model = 'player'
    form_fields = ['mpl_p20']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 20,
            }

class Pregunta_21(Page):
    form_model = 'player'
    form_fields = ['mpl_p21']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 21,
            }

class Pregunta_22(Page):
    form_model = 'player'
    form_fields = ['mpl_p22']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 22,
            }

class Pregunta_23(Page):
    form_model = 'player'
    form_fields = ['mpl_p23']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 23,
            }

class Pregunta_24(Page):
    form_model = 'player'
    form_fields = ['mpl_p24']
    def is_displayed(self):
        app = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                 app =False
        return self.round_number == 1 and app

    def vars_for_template(self):
        return {
                "pregunta": 24,
            }
    
    def before_next_page(self):
        self.player.set_pago()

class Resultados(Page):
        
        
    def is_displayed(self):
        app = True
        results = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                app = False
            else:
                self.player.set_pago()
                results = False
                
        if self.player.pregunta_pago < 7:
            self.participant.vars['mpl_pago'] = {
                "app" : "mpl",
                "pago_hoy" : "$"+format(int(str(self.player.pago_hoy).split(",")[0]),',d'),
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_10" : False,
                "pago_15" : False,
                "pregunta_pago" : self.player.pregunta_pago,
                "fila_pago" : getattr(self.player, "mpl_p"+str(self.player.pregunta_pago))
               
            }
            
        elif self.player.pregunta_pago < 13:
            self.participant.vars['mpl_pago'] = {
                "app" : "mpl",
                "pago_hoy" : "$"+format(int(str(self.player.pago_hoy).split(",")[0]),',d'),
                "pago_10" : "$"+format(int(str(self.player.pago_10).split(",")[0]),',d'),
                "pago_5" : False,
                "pago_15" : False,
                "pregunta_pago" : self.player.pregunta_pago,
                "fila_pago" : getattr(self.player, "mpl_p"+str(self.player.pregunta_pago))
               
            }
            
        elif self.player.pregunta_pago < 19:
            self.participant.vars['mpl_pago'] = {
                "app" : "mpl",
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_10" : "$"+format(int(str(self.player.pago_10).split(",")[0]),',d'),
                "pago_15" : False,
                "pago_hoy" : False,
                "pregunta_pago" : self.player.pregunta_pago,
                "fila_pago" : getattr(self.player, "mpl_p"+str(self.player.pregunta_pago))
                
            }
            
        else:
            self.participant.vars['mpl_pago'] = {
                "app" : "mpl",
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_15" : "$"+format(int(str(self.player.pago_15).split(",")[0]), ',d'),
                "pago_hoy" : False,
                "pago_10" : False,
                "pregunta_pago" : self.player.pregunta_pago,
                "fila_pago" : getattr(self.player, "mpl_p"+str(self.player.pregunta_pago))
                
            }
            
        
        return self.round_number == 1 and app and results

    def vars_for_template(self):
        if self.player.pregunta_pago < 7:
            return {
                "pago_hoy" : "$"+format(int(str(self.player.pago_hoy).split(",")[0]),',d'),
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_10" : False,
                "pago_15" : False,
                "pregunta_pago" : self.player.pregunta_pago,
                "fila_pago" : getattr(self.player, "mpl_p"+str(self.player.pregunta_pago))
                
            }
        elif self.player.pregunta_pago < 13:
            return {
                "pago_hoy" : "$"+format(int(str(self.player.pago_hoy).split(",")[0]),',d'),
                "pago_10" : "$"+format(int(str(self.player.pago_10).split(",")[0]),',d'),
                "pago_5" : False,
                "pago_15" : False,
                "pregunta_pago" : self.player.pregunta_pago,
                "fila_pago" : getattr(self.player, "mpl_p"+str(self.player.pregunta_pago))
                
            }
        elif self.player.pregunta_pago < 19:
            return {
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_10" : "$"+format(int(str(self.player.pago_10).split(",")[0]),',d'),
                "pago_15" : False,
                "pago_hoy" : False,
                "pregunta_pago" : self.player.pregunta_pago,
                "fila_pago" : getattr(self.player, "mpl_p"+str(self.player.pregunta_pago))
                
            }
        else:
            return {
                "pago_5" : "$"+format(int(str(self.player.pago_5).split(",")[0]), ',d'),
                "pago_15" : "$"+format(int(str(self.player.pago_15).split(",")[0]), ',d'),
                "pago_hoy" : False,
                "pago_10" : False,
                "pregunta_pago" : self.player.pregunta_pago,
                "fila_pago" : getattr(self.player, "mpl_p"+str(self.player.pregunta_pago))
                
            }

class Gracias(Page):
    def is_displayed(self):
        app = True
        results = True
        if 'order' in self.participant.vars:
            if self.participant.vars['order'] == 1:
                app =False
            else:
                results = False
        return self.round_number == 1 and app and results


page_sequence = [Instrucciones]

preguntas = [
    Instrucciones_1a6,
    Pregunta_1,
    Pregunta_2,
    Pregunta_3,
    Pregunta_4,
    Pregunta_5,
    Pregunta_6,
    Instrucciones_7a12,
    Pregunta_7,
    Pregunta_8,
    Pregunta_9,
    Pregunta_10,
    Pregunta_11,
    Pregunta_12,
    Instrucciones_13a18,
    Pregunta_13,
    Pregunta_14,
    Pregunta_15,
    Pregunta_16,
    Pregunta_17,
    Pregunta_18,
    Instrucciones_19a24,
    Pregunta_19,
    Pregunta_20,
    Pregunta_21,
    Pregunta_22,
    Pregunta_23,
    Pregunta_24
]


for p in preguntas:
    page_sequence.append(p)

page_sequence.append(Resultados)
page_sequence.append(Gracias)
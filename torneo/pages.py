from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class bienvenida(Page):
    def is_displayed(self):
        return self.round_number == 1


class instrucciones_practica(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            "meritocracia" : self.session.config["meritocracia"]
        }

class instrucciones_tarea(Page):
    def is_displayed(self):
        return self.round_number == 1

class instrucciones_torneo(Page):
    def is_displayed(self):
        return self.round_number == 2

    def vars_for_template(self): 
        return {
            "observabilidad" : self.session.config["observabilidad"]
        }

class tarea_practica(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['palabras', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(5)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {'legend_list': legend_list,
                'task_list': task_list,
                'task_width': task_width,
                }
           
class tarea_torneo(Page):
    def is_displayed(self):
        return self.round_number > 1

    form_model = 'player'
    form_fields = ['palabras', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(5)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {'legend_list': legend_list,
                'task_list': task_list,
                'task_width': task_width,
                "pago_A": "$"+format(int(str(Constants.pago_B).split(",")[0]), ',d'),
                "pago_B": "$"+format(int(str(Constants.pago_B).split(",")[0]), ',d'),
                "contrato_A": self.player.contrato_A}

class calculos(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.set_ranking()
        self.subsession.set_ranking_grupos()
        self.subsession.set_posiciones_jugadores()

class resultados_practica(Page):
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return {
            "palabras": self.player.palabras,
            "ronda": self.round_number - 1,
        }

class resultados_torneo(Page):
    def is_displayed(self):
        return self.round_number > 1
    def vars_for_template(self):
        return {
            "ronda": self.round_number - 1, #Restar 1 al número de rondas. Ronda 0 = Práctica
            "palabras" : self.player.palabras,
            "pago_ronda": "$"+format(int(str(self.player.pago_ronda).split(",")[0]),',d'),
            "posicion_grupo": self.player.posicion_grupo,
            "contrato_A": self.player.contrato_A,
            "posicion_contrato": self.player.posicion_contrato,
            "probabilidad_contrato_A": "{0:.0f}%".format(self.player.probabilidad_contrato_A*100)
        }

class asignacion(Page):
    def is_displayed(self):
        return self.round_number < Constants.num_rounds
    def vars_for_template(self): 
        return {
            "ronda": self.round_number,
            "contrato_A_torneo" : self.player.contrato_A_torneo,
        }

class espera_grupos(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'creating_groups'
    def is_displayed(self):
        return self.round_number < Constants.num_rounds

class espera_pago_total(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.set_pago_jugadores()
    def is_displayed(self):
        return self.round_number == Constants.num_rounds 
		
class pago_total(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self): 
        return {
            "ronda_pagar" :  Constants.ronda_pagar - 1,
            "pago_total" : "$"+format(int(str(self.player.pago.to_real_world_currency(self.session)).split(",")[0]),',d')
        }
    
class gracias(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class ruleta(Page):
    timeout_seconds = 12000
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [
	bienvenida, 
	instrucciones_practica,
    instrucciones_tarea,
    instrucciones_torneo,
	tarea_practica,
    tarea_torneo,
    calculos,
    resultados_practica,
    resultados_torneo,
    asignacion,
    espera_grupos,
    espera_pago_total,
	pago_total,
    gracias,
]

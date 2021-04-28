from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_count'] 

class welcome(Page):
    def is_displayed(self):
        return self.round_number == 1
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self): 
        return {
            "consent" : self.player.consent,
            "consent_count" : self.player.consent_count,
        }
class instructions_practice(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            "merit" : self.session.config["merit"]
        }

class instructions_task(Page):
    def is_displayed(self):
        return self.round_number == 1

class instructions_tournament(Page):
    def is_displayed(self):
        return self.round_number == 2

    def vars_for_template(self): 
        return {
            "discrimination" : self.session.config["discrimination"]
        }

class task_practice(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['tasks', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(5)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {'legend_list': legend_list,
                "round": self.round_number - 1, #Restar 1 al número de rondas. Ronda 0 = Práctica
                'task_list': task_list,
                'task_width': task_width,
                }
           
class task_tournament(Page):
    def is_displayed(self):
        return self.round_number > 1

    form_model = 'player'
    form_fields = ['tasks', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(5)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {'legend_list': legend_list,
                "round": self.round_number - 1, #Restar 1 al número de rondas. Ronda 0 = Práctica
                'task_list': task_list,
                'task_width': task_width,
                "payoff_A": "$"+format(int(str(Constants.payoff_A).split(",")[0]), ',d'),
                "payoff_B": "$"+format(int(str(Constants.payoff_B).split(",")[0]), ',d'),
                "contract_A": self.player.contract_A}

class calculations(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.set_ranking()
        self.subsession.set_ranking_groups()
        self.subsession.set_positions_players()
        self.subsession.set_contract_A_players()
        
                
class results_practice(Page):
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return {
            "tasks": self.player.tasks,
            "round": self.round_number - 1,
        }

class results_tournament(Page):
    def is_displayed(self):
        return self.round_number > 1
    def vars_for_template(self):
        return {
            "round": self.round_number - 1, #Restar 1 al número de rondas. Ronda 0 = Práctica
            "tasks" : self.player.tasks,
            "payoff_round": "$"+format(int(str(self.player.payoff_round).split(",")[0]),',d'),
            "position_group": self.player.position_group,
            "contract_A": self.player.contract_A,
            "position_contract": self.player.position_contract,
            "likelihood_contract_A": "{0:.0f}%".format(self.player.likelihood_contract_A*100)
        }

class allocation(Page):
    def is_displayed(self):
        return self.round_number < Constants.num_rounds
    def vars_for_template(self): 
        return {
            "round": self.round_number,
            "contract_A_tournament" : self.player.contract_A_tournament,
        }

class wait_groups(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'creating_groups'
    def is_displayed(self):
        return self.round_number < Constants.num_rounds

class wait_payoff_total(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.set_payoff_players()
    def is_displayed(self):
        return self.round_number == Constants.num_rounds 
		
class payoff_total(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self): 
        return {
            "round_payoff" :  Constants.round_payoff - 1,
            "payoff_total" :  self.player.pago
            # "pago_total" : "$"+format(int(str(self.player.pago.to_real_world_currency(self.session)).split(",")[0]),',d')
        }
    
class thanks(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class ruleta(Page):
    timeout_seconds = 12000
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [
    consent,
	welcome, 
	instructions_practice,
    instructions_task,
    instructions_tournament,
	task_practice,
    task_tournament,
    calculations,
    results_practice,
    results_tournament,
    allocation,
    wait_groups,
    wait_payoff_total,
	payoff_total,
    thanks,
]

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'results'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    p1 = models.IntegerField(
    choices=[
        [1, 'Hombre'],
        [2, 'Mujer'],
        [3, 'Otro'],
    ], label="¿Con qué género se identifica?")
    p2 = models.IntegerField(label="Edad")
    p3 = models.IntegerField(
    choices=[
        [1,'Estudiante'],
        [2,'Desempleado'],
        [3,'Empleado a jornada completa'],
        [4,'Empleado a tiempo parcial'],
        [5,'Trabajador independiente'],
        [6,'Trabajador no remunerado (por ejemplo: ama de casa, empresa familiar)'],
        [7,'Retirado/pensionado'],
        [8,'Otro'],
        [9,'No sabe']
    ], label="¿Cuál es su situación laboral actual?")
    p4 = models.IntegerField(
    choices=[
        [1,'Ninguno'],
        [2,'Primaria incompleta'],
        [3,'Primaria'],
        [4,'Bachillerato'],
        [5,'Técnico o Tecnólogo'],
        [6,'Pregrado'],
        [7,'Posgrado (Especialización, Maestría, Doctorado)']
    ], label="¿Cuál es el nivel educativo más alto que ha completado?")
    p5 = models.StringField(label="Escriba el nombre de su profesión/ocupación")
    p6 = models.IntegerField(
    choices=[
        [1,'Subsidiado'],
        [2,'Contributivo (incluye regímenes especiales)']
    ], label="A qué régimen de seguridad social en salud pertenece")
    p7 = models.IntegerField(
    choices=[
        [1,'Menos del Salario Mínimo Mensual (SMMLV)'],
        [2,'Entre 1 SMMLV - $ 1.500.000'],
        [3,'Entre $ 1.500.000 - $ 2.000.000'],
        [4,'Entre $ 2.000.000 - $ 4.000.000'],
        [5,'Mayor a $ 4.000.000'],
    ], label="¿Cuál es el rango de su ingreso mensual?")
    p_risk = models.IntegerField(widget=widgets.RadioSelectHorizontal, 
                                 label="", 
                                 choices=[  [0, "0"],
                                            [1, "1"],
                                            [2, "2"],
                                            [3, "3"],
                                            [4, "4"],
                                            [5, "5"],
                                            [6, "6"],
                                            [7, "7"],
                                            [8, "8"],
                                            [9, "9"],
                                            [10, "10"]])

    
    
    p11 = models.StringField(label="¿Qué entiende usted como probabilidad?")
    p12 = models.StringField(label="¿Hubo algo que no entendiera en alguna de las actividades? Si es así, ¿qué no entendió? (Recuerde que son 4 actividades)")
    p13 = models.StringField(label="¿Hubo algo que le pareciera confuso en alguna de las actividades? Si es así, ¿qué le pareció confuso?")
    p14 = models.StringField(label="¿Hubo algo que le pareciera difícil en alguna de las actividades? Si es así, ¿qué se le dificultó?")
    
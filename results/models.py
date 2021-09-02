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
    p_gender = models.IntegerField(
    choices=[
        [1, 'Hombre'],
        [2, 'Mujer'],
        [3, 'Otro'],
    ], label="¿Con qué género se identifica?")
    p_age = models.IntegerField(label="Edad")
    p_student = models.IntegerField(
    choices=[
        [1, 'Sí'],
        [2, 'No'],
    ], label="¿Es usted estudiante?")
    p = models.IntegerField(
    choices=[
        [1,'Solo estudio'],
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
        [2,'Primaria'],
        [3,'Bachillerato'],
        [4,'Técnico o Tecnólogo'],
        [5,'Pregrado'],
        [6,'Posgrado (Especialización, Maestría, Doctorado)']
    ], label="5. ¿Cuál es el nivel educativo más alto que cursó?")
    peduc1 = models.IntegerField(label="¿Cuántos años de educación completó en ese nivel?")
    peduc2 = models.StringField(label="Escriba el nombre de su profesión/ocupación")
    p7 = models.IntegerField(
    choices=[
        [1,'Subsidiado'],
        [2,'Contributivo (incluye regímenes especiales)']
    ], label="¿A qué régimen de seguridad social en salud pertenece?")
    p8 = models.IntegerField(
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

    p8 = models.IntegerField(
    choices=[
        [1,'Portátil'],
        [2,'Equipo de escritorio']
    ], label="¿Qué tipo de computador usó durante la actividad?")
    p9 = models.IntegerField(
    choices=[
        [1,'Sí (no incluye el mouse incorporado en el computador portátil).'],
        [2,'No']
    ], label="¿Durante la actividad usted utilizó un “mouse/ratón” no incorporado al equipo?") 
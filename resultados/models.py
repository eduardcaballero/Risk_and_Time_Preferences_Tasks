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
    name_in_url = 'resultados'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    p1 = models.StringField(label="¿Qué entiende usted como probabilidad?")
    p2 = models.StringField(label="¿Hubo algo que no entendiera en alguna de las actividades? Si es así, ¿qué no entendió?")
    p3 = models.StringField(label="¿Hubo algo que entendiera de forma errónea en alguna de las actividades? Si es así, ¿qué entendió erróneamente?")
    p4 = models.StringField(label="¿Hubo algo que le pareciera difícil en alguna de las actividades? Si es así, ¿qué se le dificultó?")
    p5 = models.IntegerField(
    choices=[
        [1, 'Hombre'],
        [2, 'Mujer'],
        [3, 'Otro'],
    ], label="¿Con qué género se identifica?")
    p6 = models.IntegerField(label="Edad")
    p7 = models.IntegerField(
    choices=[
        [1, 'Estudiante'],
        [2,'Desempleado'],
        [3,'Empleado a jornada completa'],
        [4,'Empleado a tiempo parcial'],
        [5,'Trabajador independiente'],
        [6,'Trabajador no remunerado (por ejemplo: ama de casa, empresa familiar)'],
        [7,'Retirado/pensionado'],
        [8,'Otro'],
        [9,'No sabe']
    ], label="¿Cuál es su situación laboral actual?")
    p8 = models.IntegerField(
    choices=[
        [1,'Ninguno'],
        [2,'Primaria incompleta'],
        [3,'Primaria'],
        [4,'Bachillerato'],
        [5,'Técnico o Tecnólogo'],
        [6,'Pregrado'],
        [7,'Posgrado (Especialización, Maestría, Doctorado)']
    ], label="¿Cuál es el nivel educativo más alto que ha completado?")
    p9 = models.StringField(label="Escriba el nombre de su profesión/ocupación")
    p10 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6], label="Estrato del inmueble en el que vive (estrato por el que paga servicios públicos)")
    p11 = models.IntegerField(
    choices=[
        [1,'Subsidiado'],
        [2,'Contributivo (incluye regímenes especiales)']
    ], label="A qué régimen de seguridad social en salud pertenece")
    p12 = models.IntegerField(
    choices=[
        [1,'Menos del Salario Mínimo Mensual (SMMLV)'],
        [2,'Entre 1 SMMLV - $ 1.500.000'],
        [3,'Entre $ 1.500.000 - $ 2.000.000'],
        [4,'Entre $ 2.000.000 - $ 4.000.000'],
        [5,'Mayor a $ 4.000.000'],
    ], label="¿Cuál es el rango de su ingreso mensual?")
    app_pago = models.StringField()
    pago =  models.CurrencyField(initial=0)
    pago_5 =  models.CurrencyField(initial=0)
    pago_10 =  models.CurrencyField(initial=0)
    pago_15 =  models.CurrencyField(initial=0)
    pago_total = models.CurrencyField(initial=0)


    def get_juego_pagar():
        secuence = ["sgg","hl"]
        app_pay = random.choice(secuence)
        pago = self.participants.vars["pago_"+app_pay]
        return app_pay, pago

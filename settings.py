from os import environ
import os

#environ.__setitem__('OTREE_PRODUCTION','1') ################
#if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
#    DEBUG = True
#else:
#    DEBUG = False

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': ""
    }

SESSION_CONFIGS = [
    {
        'name': 'dm',
        'display_name': "DM",
        'num_demo_participants': 50,
        'app_sequence': ['dm']
    },
    {
        'name': 'bret',
        'display_name': "BRET",
        'num_demo_participants': 50,
        'app_sequence': ['bret']
    },
    {
        'name': 'sgg',
        'display_name': "SGG",
        'num_demo_participants': 50,
        'app_sequence': ['sgg']
    },
    {
        'name': 'hl',
        'display_name': "HL",
        'num_demo_participants': 50,
        'app_sequence': ['hl']
    },
    {
        'name': 'ctb',
        'display_name': "CTB",
        'num_demo_participants': 50,
        'app_sequence': ['ctb'],
        'Rounds':None
    },
    {
        'name': 'ctb_2',
        'display_name': "CTB2",
        'num_demo_participants': 50,
        'app_sequence': ['ctb_2'],
        'Rounds':None
    },
    {
        'name': 'ctb_r',
        'display_name': "CTB Random",
        'num_demo_participants': 50,
        'app_sequence': ['ctb_r'],
        'Rounds':None
    },
    {
        'name': 'mpl',
        'display_name': "MPL",
        'num_demo_participants': 50,
        'app_sequence': ['mpl'],
        'Rounds':None
    },
    {
        'name': 'torneo',
        'display_name': 'Juego de encriptacion',
        'num_demo_participants': 4,
        'app_sequence': ['torneo','icl','results'],
        'discrimination': 0,
        'merit': False,
    },
    {
        'name': 'tarea',
        'display_name': 'Tarea',
        'num_demo_participants': 1,
        'app_sequence': ['tarea'],
    },
    {
        'name': 'app',
        'display_name': 'App',
        'num_demo_participants': 5, 
        # sequence 0 = [ctb,hl,mpl,bret], sequence 1 = [mpl_2,hl,ctb_2,bret]
        'app_sequence': ['home','ctb', 'mpl_2', 'hl', 'mpl', 'ctb_2', 'bret','resultados'],
    },
    {
        'name': 'app_2',
        'display_name': 'App 2',
        'num_demo_participants': 5,
        # sequence 0 = [ctb,hl,mpl,bret,dm], sequence 1 = [mpl_2,hl,ctb_2,bret,dm]
        # sequence 2 = [ctb,hl,mpl,sgg,dm], sequence 3 = [mpl_2,hl,ctb_2,sgg,dm]
        'app_sequence': ['home', 'ctb', 'mpl_2', 'hl', 'mpl', 'ctb_2', 'bret', 'sgg', 'dm', 'resultados'],
    },
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, 
    participation_fee=0.00, 
    doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEMO_PAGE_TITLE = "Risk and time preferences tasks"
DEMO_PAGE_INTRO_HTML = """"""

SECRET_KEY = '6k75xea8!xbc+)g%)zu&em-^(#*u38$5h1mu8o8t)7i4k5czsk'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree' , 'django_user_agents']

STATIC_URL = '/static/'

MIDDLEWARE_CLASSES = (
    # other middlewares...
    'django_user_agents.middleware.UserAgentMiddleware',
)


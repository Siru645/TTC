from otree.api import *


doc = """
otree project for my TTC paper 0428
"""


class Constants(BaseConstants):
    name_in_url = 'TTC_main'
    players_per_group = 4
    num_rounds = 1
    instructions_template = 'TTC_instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer): #rank the schools
    first_choice = models.StringField(
        choices=['A', 'B', 'C'],
        label = 'Your first choice'
    )
    second_choice = models.StringField(
        choices=['A', 'B', 'C'],
        label = 'Your second choice'
    )
    third_choice = models.StringField(
        choices=['A', 'B', 'C'],
        label = 'Your third choice'
    )

# FUNCTIONS



# PAGES
class Ranking(Page):
    form_model = 'player'
    form_fields = ['first_choice', 'second_choice', 'third_choice']


class ResultsWaitPage(WaitPage):
    pass
    #after_all_players_arrive =


class Results(Page):
    pass


page_sequence = [Ranking, ResultsWaitPage, Results]

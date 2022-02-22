# from otree.api import (
#     Page,
#     WaitPage,
#     models,
#     widgets,
#     BaseConstants,
#     BaseSubsession,
#     BaseGroup,
#     BasePlayer,
#     Currency as c,
#     currency_range,
# )

from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):  # no comma at the end of each constant
    name_in_url = 'my_pub_game'
    players_per_group = 2
    num_rounds = 2
    MPCR1 = 0.4
    MPCR2 = 0.6
    endowment = 100


class Subsession(BaseSubsession): # define object properties
    pass


class Group(BaseGroup):
    MPCR = models.FloatField(initial=-999)


class Player(BasePlayer):  # no space around the parameters
    contribution = models.IntegerField(
        min=0,
        max=Constants.endowment,
        label='How much will you contribute?'
    )


# Functions

def creating_session(subsession):  # creating_session is built in
    print('in creating session')
    # Establish a total earnings variable for each participant and initialize to 0 at the beginning
    for p in subsession.get_players():
        if subsession.round_number == 1:
            p.participant.vars['totalEarnings'] = 0

    # Assign varying MPCR in different rounds

    for g in subsession.get_groups():
        print('round', subsession.round_number)
        print('num_rounds/2', int(Constants.num_rounds / 2))
        if subsession.round_number <= int(Constants.num_rounds / 2):
            g.MPCR = Constants.MPCR1
        else:
            g.MPCR = Constants.MPCR2


def setPayoffs(g: Group):
    # First to calculate the total contributed by all group members
    total_contribution = 0
    for p in g.get_players():
        total_contribution += p.contribution
    # Second to calculate the earnings for each group member
    for p in g.get_players():
        print('payoff ', p.participant.payoff)
        print('endowment ', Constants.endowment)
        print('contribution ', p.contribution)
        print('total contribution ', total_contribution)
        print('MPCR ', g.MPCR)
        p.participant.payoff = float(Constants.endowment - p.contribution + total_contribution * g.MPCR)
        p.participant.vars['totalEarnings'] += p.participant.payoff


#  PAGES
class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'setPayoffs'  # setPayoffs is built in
    body_text = 'Please wait for everyone to make decisions.'

class Results(Page):
    pass


page_sequence = [Contribution, ResultsWaitPage, Results]

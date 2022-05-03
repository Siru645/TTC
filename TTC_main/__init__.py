from otree.api import *
import random

doc = """
otree project for my TTC paper 0428
"""

class Constants(BaseConstants):
    name_in_url = 'TTC_main'
    players_per_group = 4
    num_rounds = 3
    paymentA = 24
    paymentB = 16
    paymentC = 8
    timeout_seconds = 10
    choices = ['School A', 'School B', 'School C']


class Subsession(BaseSubsession):
    def creating_session(phase):
        if phase.round_number == 1: phase = 1
        if phase.round_number == 2: phase = 2
        if phase.round_number == 3: phase = 3


class Group(BaseGroup):
    pass


class Player(BasePlayer): #rank the schools
    ranking = models.StringField()

# class Message(ExtraModel):
#     group = models.Link(Group)
#     sender = models.Link(Player)
#     text = models.StringField()

# FUNCTIONS


# PAGES
class Instruction(Page):
    @staticmethod
    def is_displayed(subsession):
        return subsession.round_number == 1

class Phase1(Page):
    @staticmethod
    def is_displayed(subsession):
        return subsession.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['ranking']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random

        participant = player.participant

        # if it's the last round
        if player.round_number == Constants.num_rounds:
            random_round = random.randint(1, Constants.num_rounds)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            player.payoff = 24-(random_round-1)*8


class Phase2(Page):
    @staticmethod
    def is_displayed(subsession):
        return subsession.round_number == 2

class Decision2(Page):
    form_model = 'player'
    form_fields = ['ranking']

class Phase3(Page):
    @staticmethod
    def is_displayed(subsession):
        return subsession.round_number == 3
    def get_timeout_seconds(player):
        return Constants.timeout_seconds  # in seconds

class Decision3(Page):
    form_model = 'player'
    form_fields = ['ranking']

class Wait_phase(WaitPage):
    pass

class ResultWaitPage(WaitPage):
    wait_for_all_groups = True

class Results(Page):
    @staticmethod
    def is_displayed(subsession):
        return subsession.round_number == 3
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


# page_sequence = [Instruction, Phase1, Decision, Phase2, Decision, Wait_phase3, Phase3, Decision, Results]
page_sequence = [Instruction, Phase1, Phase2, Phase3, Decision, Wait_phase, Results]
#https://github.com/Siru645/TTC.git
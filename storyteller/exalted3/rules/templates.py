from __future__ import unicode_literals

from storyteller.exalted3.rules.pools import *
from storyteller.exalted3.rules.stats import *

from athanor.utils.text import dramatic_capitalize, partial_match, sanitize_string
from storyteller.exbase.models import Trait as TraitModel, TraitAnswer

def clean_string(value):
    return dramatic_capitalize(sanitize_string(value, strip_ansi=True, strip_mxp=True,
                                               strip_newlines=True, strip_indents=True))

ALL_STATS = ALL_ABILITIES + ALL_ATTRIBUTES + ALL_ADVANTAGES + ALL_STYLES


class Splat(object):
    owner = None
    key = '<Unknown'
    id = 0
    display = 'Splat'

    def __str__(self):
        return self.key

    def __int__(self):
        return self.id

    def __init__(self, owner):
        self.owner = owner


class Trait(object):
    owner = None
    key = '<Unknown'
    id = 0
    value = None
    choices = ()
    default = None

    def __str__(self):
        return self.key

    def __int__(self):
        return self.id

    def __init__(self, owner):
        self.owner = owner
        self.load()

    def get_model(self):
        if not self.value:
            self.value = self.default
        model, created = TraitModel.objects.get_or_create(persona=self.owner.persona, trait_id=self.id)
        return model

    def load(self):
        model = self.get_model()
        self.value = str(model.answer)

    def save(self):
        model = self.get_model()
        if model.answer.key == self.value:
            return
        new_answer, created = TraitAnswer.objects.get_or_create(key=self.value)
        model.answer = new_answer
        model.save(update_fields=['answer'])

    def set_value(self, choice):
        old_value = str(self.value)
        if len(self.choices):
            find_value = partial_match(choice, self.choices)
            if not find_value:
                raise ValueError("That is not a valid choice! Choose from: %s" % ", ".join(self.choices))
            self.value = find_value
        else:
            final_value = clean_string(choice)
            self.value = final_value

        if not old_value == self.value:
            self.save()


class Template(object):
    owner = None
    key = '<Unknown>'
    id = 0
    trait_choices = ()
    caste_choices = ()
    caste_default = None
    pools = list()
    willpower = 5
    stat_list = ALL_STATS

    def __str__(self):
        return self.key

    def __int__(self):
        return self.id

    def __init__(self, owner):
        self.owner = owner
        self.traits = list()
        self.traits_dict = dict()
        for trait_class in self.trait_choices:
            trait = trait_class(self.owner)
            self.traits.append(trait)
            self.traits_dict[trait.key] = trait


# Mortal

class Profession(Caste):
    display = 'Profession'


class Warrior(Profession):
    key = 'Warrior'
    id = 1


class Priest(Profession):
    key = 'Priest'
    id = 2


class Criminal(Profession):
    key = 'Criminal'
    id = 3


class Savant(Profession):
    key = 'Savant'
    id = 4


class Broker(Profession):
    key = 'Broker'
    id = 5


class Mortal(Template):
    key = 'Mortal'
    id = 1
    caste_choices = (Warrior, Priest, Criminal, Savant, Broker,)
    caste_default = Warrior
    willpower = 3
    pools = MORTAL_POOLS

# Solar

class Dawn(Caste):
    key = 'Dawn'
    id = 6


class Zenith(Caste):
    key = 'Zenith'
    id = 7


class Night(Caste):
    key = 'Night'
    id = 8


class Twilight(Caste):
    key = 'Twilight'
    id = 9


class Eclipse(Caste):
    key = 'Eclipse'
    id = 10


class Solar(Template):
    key = 'Solar'
    id = 2
    caste_choices = (Dawn, Zenith, Night, Twilight, Eclipse)
    caste_default = Dawn
    pools = SOLAR_POOLS

# Abyssal




class Abyssal(Template):
    key = 'Abyssal'
    id = 3
    caste_choices = (Dusk, Midnight, Day, Daybreak, Moonshadow)
    caste_default = Dusk
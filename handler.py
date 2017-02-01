from __future__ import unicode_literals

class Handler(object):
    """
    Not meant to be used directly. Parent Class for all StorytellerHandler Sections!
    """

    def __init__(self, owner):
        self.owner = owner
        self.character = owner.character
        self.persona = owner.persona
        self.handler = owner
        self.data = owner.data
        self.game = owner.game
        self.load()
        self.load_extra()

    def load(self):
        """
        Meant to be overloaded for each Handler.
        :return:
        """
        pass

    def load_extra(self):
        """
        A second overloadable so you don't have to super() if you inherit from the existing Handlers for things.
        :return:
        """
        pass

class StatHandler(Handler):
    """
    Object responsible for storing, sorting, readying and managing the Stats (Abilities, Attributes, Advantages,
    etc). Component of StorytellerHandler.
    """

    def load(self):
        self.owner.persona.stats.all().exclude(id__in=self.data.stats_dict.keys()).delete()
        stats = self.owner.persona.stats.all()
        if not stats or len(self.data.stats) != stats.count():
            self.load_defaults()
            stats = self.owner.persona.stats.all()
        all_stats = list()
        for row in stats:
            proto = self.data.stats_dict[row.stat_id]
            new_stat = proto.use(self, proto, row)
            all_stats.append(new_stat)
        self.stats = sorted(all_stats, key=lambda stat: stat.list_order)
        self.stats_name = {stat.name: stat for stat in self.stats}
        self.stats_dict = {stat.id: stat for stat in self.stats}

    @property
    def attributes(self):
        return [stat for stat in self.stats if stat.category == 'Attribute']

    @property
    def physical_attributes(self):
        return [stat for stat in self.attributes if stat.sub_category == 'Physical']

    @property
    def social_attributes(self):
        return [stat for stat in self.attributes if stat.sub_category == 'Social']

    @property
    def mental_attributes(self):
        return [stat for stat in self.attributes if stat.sub_category == 'Mental']

    def load_defaults(self):
        """
        This is called only if there is NO saved data for the character. It loads some default data for Attributes,
        Essence, Willpower, etc, using the .default properties of the Stats from GAME_DATA.

        :return:
        """
        stat_ids = set(self.data.stats_dict.keys())
        char_ids = set(self.owner.persona.stats.all().values_list('stat_id', flat=True))
        not_have = stat_ids.difference(char_ids)

        for id in not_have:
            stat = self.data.stats_dict[id]
            new = self.owner.persona.stats.create(stat_id=stat.id, rating=stat.default)


class SheetHandler(Handler):
    """
    Object responsible for manging Sheet Output.
    """
    def load(self):
        self.sections = sorted([sec(self) for sec in self.data.load_sheet], key=lambda ord: ord.list_order)

    def render(self, width=80):
        message = list()
        for sec in [sec for sec in self.sections if sec.display]:
            rendered = sec.render(width=width)
            if rendered:
                message.append(rendered)
        return '\n'.join(message)


class PoolHandler(Handler):
    """
    Object responsible for manging Pools.
    """
    pass


class ExtraHandler(Handler):

    def load(self):
        self.extras = [ex.use(self, ex, root=self) for ex in self.data.extras]
        self.extras_dict = {ex.id: ex for ex in self.extras}
        self.extras_name = {ex.name: ex for ex in self.extras}


class StorytellerHandler(object):
    """
    An instance of Storyteller is loaded onto every Character who'll be doing Storyteller stuff. This is the primary
    interface for all commands and database functions.
    """
    data = None
    stat_handler = StatHandler
    sheet_handler = SheetHandler
    pool_handler = PoolHandler
    extra_handler = ExtraHandler

    def __init__(self, owner):
        self.owner = owner
        self.character = owner
        self.game = self.data.game

        for prep in (self.prepare_template, self.prepare_stats, self.prepare_sheet, self.prepare_extras,
                     self.prepare_pools):
            prep()

    def prepare_template(self):
        pers = self.game.personas.filter(character=self.owner).first()
        if not pers:
            pers = self.game.personas.create(character=self.owner, key=self.owner.key)
        self.persona = pers
        tem = self.data.templates_dict[pers.template]
        self.template = tem.use(self, tem, pers)

    def prepare_stats(self):
        self.stats = self.stat_handler(self)

    def prepare_sheet(self):
        self.sheet = self.sheet_handler(self)

    def prepare_pools(self):
        self.pools = self.pool_handler(self)

    def prepare_extras(self):
        self.extras = self.extra_handler(self)
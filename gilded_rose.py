from collections import OrderedDict

def is_backstage_pass(item):
    return item.name.startswith("Backstage passes")

def is_legendary(item):
    return item.name == "Sulfuras, Hand of Ragnaros"

def is_conjured_item(item):
    return item.name.startswith("Conjured")

def never_age(item):
    pass

def increases_in_quality(item):
    return item.name == "Aged Brie"

def age_as_backstage_pass(item):

    item.sell_in -= 1

    if item.sell_in < 0:
        item.quality = 0
        return

    if item.sell_in >= 10:
        increment = 1
    elif item.sell_in >= 5:
        increment = 2
    else:
        increment = 3

    item.quality = next_quality(item.quality, - increment)


def next_quality(num, increment):
    return max(0, min(50, num - increment))

def age_normally(increment=1):
    def age(item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = next_quality(item.quality, 2 * increment)
        else:
            item.quality = next_quality(item.quality, increment)
    return age


rules = {
    is_legendary: never_age,
    is_backstage_pass: age_as_backstage_pass,
    increases_in_quality: age_normally(increment=-1),
    is_conjured_item: age_normally(increment=2)
}

class GildedRose:

    def __init__(self, items):
        self.items = items

    def get_rule(self, item):
        for match, ager in rules.items():
            if match(item):
                return ager
        return age_normally()

    def update_quality(self):

        for item in self.items:
            age = self.get_rule(item)
            age(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

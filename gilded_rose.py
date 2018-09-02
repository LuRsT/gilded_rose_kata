class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item = item_factory(item)
            item.update()


def item_factory(item):
    translator = {
        'Aged Brie': AgedBrieItem,
        'Sulfuras': SulfurasItem,
        'Backstage passes': BackstagePassesItem,
        'Conjured': ConjuredItem,
    }

    for type_name, class_ in translator.items():
        if type_name in item.name:
            return class_(item.name, item.sell_in, item.quality)

    return DefaultItem(item.name, item.sell_in, item.quality)


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AgedBrieItem(Item):

    def update(self):
        self.sell_in -= 1

        if self.quality == 50:
            return

        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1


class BackstagePassesItem(Item):

    def update(self):
        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2

        self.sell_in -= 1


class SulfurasItem(Item):

    def update(self):
        pass


class ConjuredItem(Item):

    def update(self):
        self.sell_in -= 1
        self.quality -= 2

        if self.sell_in < 0:
            self.quality -= 2

        if self.quality < 0:
            self.quality = 0


class DefaultItem(Item):

    def update(self):
        self.sell_in -= 1
        self.quality -= 1

        if self.sell_in <= 0:
            self.quality -= 1

        if self.quality < 0:
            self.quality = 0

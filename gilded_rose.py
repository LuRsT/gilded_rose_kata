class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if self.name != "Backstage passes to a TAFKAL80ETC concert":
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.name != "Backstage passes to a TAFKAL80ETC concert":
                if self.quality > 0:
                    if self.name != "Sulfuras, Hand of Ragnaros":
                        self.quality = self.quality - 1


class AgedBrie(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50


class Sulfuras(Item):
    def update_quality(self):
        self.quality = 80

class Backstage(Item):
    def update_quality(self):
        self.sell_in -= 1

        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in >= 10:
            self.quality += 1
        elif self.sell_in < 10 and self.sell_in >= 5:
            self.quality += 2
        elif self.sell_in < 5:
            self.quality += 3

        if self.quality > 50:
            self.quality = 50

class Conjured(Item):
    def update_quality(self):
        self.sell_in -= 1
        self.quality -= 2
        if self.sell_in <= 0:
            self.quality = 0


def create_item(name, sell_in, quality):
    match name:
        case "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        case s if s.startswith("Sulfuras"):
            return Sulfuras(name, sell_in, quality)
        case s if s.startswith("Backstage passes"):
            return Backstage(name, sell_in, quality)
        case s if s.startswith("Conjured"):
            return Conjured(name, sell_in, quality)
        case _:
            return Item(name, sell_in, quality)

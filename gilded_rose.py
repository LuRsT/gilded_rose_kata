class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASS:
                if item.quality > self.MIN_QUALITY:
                    if item.name != self.SULFURAS:
                        item.quality = item.quality - 1
            else:
                if item.quality < self.MAX_QUALITY:
                    item.quality = item.quality + 1
                    if item.name == self.BACKSTAGE_PASS:
                        if item.sell_in < 11:
                            if item.quality < self.MAX_QUALITY:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < self.MAX_QUALITY:
                                item.quality = item.quality + 1
            if item.name != self.SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != self.AGED_BRIE:
                    if item.name != self.BACKSTAGE_PASS:
                        if item.quality > self.MIN_QUALITY:
                            if item.name != self.SULFURAS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = self.MIN_QUALITY
                else:
                    if item.quality < self.MAX_QUALITY:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


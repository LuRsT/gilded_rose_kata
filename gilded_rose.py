class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    def _increase_quality(self, item, amount=1):
        item.quality = min(self.MAX_QUALITY, item.quality + amount)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(self.MIN_QUALITY, item.quality - amount)

    def update_quality(self):
        for item in self.items:
            if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASS:
                if item.quality > self.MIN_QUALITY:
                    if item.name != self.SULFURAS:
                        self._decrease_quality(item)
            else:
                if item.quality < self.MAX_QUALITY:
                    self._increase_quality(item)
                    if item.name == self.BACKSTAGE_PASS:
                        if item.sell_in < 11:
                            self._increase_quality(item)
                        if item.sell_in < 6:
                            self._increase_quality(item)
            if item.name != self.SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != self.AGED_BRIE:
                    if item.name != self.BACKSTAGE_PASS:
                        if item.quality > self.MIN_QUALITY:
                            if item.name != self.SULFURAS:
                                self._decrease_quality(item)
                    else:
                        item.quality = self.MIN_QUALITY
                else:
                    if item.quality < self.MAX_QUALITY:
                        self._increase_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


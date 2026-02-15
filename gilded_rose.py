class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality_for_items(self):
        for item in self.items:
            strategy = self.get_strategy(item.name)
            strategy(item)

    def get_strategy(self, item_name):
        if item_name == "Aged Brie":
            return self.aged_brie_strategy
        elif item_name.startswith("Backstage"):
            return self.backstage_strategy
        elif item_name.startswith("Sulfuras"):
            return self.sulfuras_strategy
        elif item_name.startswith("Conjured"):
            return self.conjured_strategy
        return self.default_strategy

    @staticmethod
    def default_strategy(item):
        item.sell_in -= 1
        item.quality -= 1

        if item.sell_in < 0:
            item.quality -= 1

        if item.quality <= 0:
            item.quality = 0

        if item.quality > 50:
            item.quality = 50

    @staticmethod
    def conjured_strategy(item):
        item.sell_in -= 1
        item.quality -= 2

        if item.sell_in < 0:
            item.quality -= 2

        if item.quality <= 0:
            item.quality = 0

        if item.quality > 50:
            item.quality = 50

    @staticmethod
    def aged_brie_strategy(item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality += 2
        else:
            item.quality += 1

        if item.quality > 50:
            item.quality = 50

    @staticmethod
    def backstage_strategy(item):
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in < 10:
            item.quality += 2
        else:
            item.quality += 1

        if item.quality > 50:
            item.quality = 50

    @staticmethod
    def sulfuras_strategy(item):
        item.quality = 80

    @staticmethod
    def original_strategy(item):
        if (
            item.name != "Aged Brie"
            and item.name != "Backstage passes to a TAFKAL80ETC concert"
        ):
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

    # Can't change this
    def update_quality(self):
        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

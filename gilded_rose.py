class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            is_backstage_pass = item.name == "Backstage passes to a TAFKAL80ETC concert"
            is_aged_brie = item.name == "Aged Brie"
            is_sulfuras = item.name == "Sulfuras, Hand of Ragnaros"
            is_conjured = item.name == 'Conjured'
            can_decrease_quality = item.quality > 0 and not is_sulfuras

            if not is_aged_brie and not is_backstage_pass:
                if can_decrease_quality:
                    item.quality -= 1
                if is_conjured:
                    item.quality -= 1
            elif is_backstage_pass:
                item.quality += 1

                if item.sell_in < 11:
                    item.quality += 1

                if item.sell_in < 6:
                    item.quality += 1
            else:
                item.quality += 1

            if not is_sulfuras:
                item.sell_in -= 1

            if item.sell_in < 0:
                if not is_aged_brie:
                    if not is_backstage_pass and can_decrease_quality:
                        item.quality -= 1
                        if is_conjured:
                            item.quality -= 1
                    elif not is_sulfuras:
                        item.quality = item.quality - item.quality
                else:
                    item.quality += 1

            if item.quality < 0:
                item.quality = 0

            if item.quality > 50 and not is_sulfuras:
                item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

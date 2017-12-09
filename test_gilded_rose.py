from gilded_rose import (
    Item,
    GildedRose,
    AgedBrieItem,
    item_factory,
    BackstagePassesItem,
    SulfurasItem,
    ConjuredItem,
    DefaultItem,
)


class TestGildedRose:

    def test_aged_brie_after_one_day(self):
        item = Item('Aged Brie', 1, 1)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.name == 'Aged Brie'
        assert item.quality == 2
        assert item.sell_in == 0

    def test_aged_brie_after_two_days_expired(self):
        item = Item('Aged Brie', 1, 1)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()
        gilded_rose.update_quality()

        assert item.name == 'Aged Brie'
        assert item.quality == 4
        assert item.sell_in == -1


class TestFactory:

    def test_aged_brie(self):
        item = Item('Aged Brie item', 0, 0)

        specialized_item = item_factory(item)

        assert isinstance(specialized_item, AgedBrieItem)
        assert specialized_item.quality == item.quality
        assert specialized_item.name == item.name
        assert specialized_item.sell_in == item.sell_in

    def test_backstage_passes(self):
        item = Item('Backstage passes to a concert', 0, 0)

        specialized_item = item_factory(item)

        assert isinstance(specialized_item, BackstagePassesItem)
        assert specialized_item.quality == item.quality
        assert specialized_item.name == item.name
        assert specialized_item.sell_in == item.sell_in

    def test_conjured(self):
        item = Item('Conjured Item', 0, 0)

        specialized_item = item_factory(item)

        assert isinstance(specialized_item, ConjuredItem)
        assert specialized_item.quality == item.quality
        assert specialized_item.name == item.name
        assert specialized_item.sell_in == item.sell_in

    def test_sulfuras(self):
        item = Item('Sulfuras', 0, 0)

        specialized_item = item_factory(item)

        assert isinstance(specialized_item, SulfurasItem)
        assert specialized_item.quality == item.quality
        assert specialized_item.name == item.name
        assert specialized_item.sell_in == item.sell_in

    def test_default(self):
        item = Item('Something else', 0, 0)

        specialized_item = item_factory(item)

        assert isinstance(specialized_item, DefaultItem)
        assert specialized_item.quality == item.quality
        assert specialized_item.name == item.name
        assert specialized_item.sell_in == item.sell_in

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


class TestAgedBrie:

    def test_after_one_day(self):
        item = AgedBrieItem('Aged Brie', 1, 1)

        item.update()

        assert item.quality == 2
        assert item.sell_in == 0

    def test_after_expired(self):
        item = AgedBrieItem('Aged Brie', 0, 1)

        item.update()
        item.update()

        assert item.quality == 5
        assert item.sell_in == -2

    def test_after_one_day_max_quality(self):
        item = AgedBrieItem('Aged Brie', 1, 50)

        item.update()

        assert item.quality == 50
        assert item.sell_in == 0


class TestSulfuras:

    def test_after_one_day(self):
        item = SulfurasItem('Sulfuras', 1, 1)

        item.update()

        assert item.quality == 1
        assert item.sell_in == 1

    def test_after_expired(self):
        item = SulfurasItem('Sulfuras', 0, 1)

        item.update()
        item.update()

        item.quality == 1
        item.sell_in == 0


class TestBackstagePasses:

    def test_after_one_day(self):
        item = BackstagePassesItem('Pass', 1, 1)

        item.update()

        assert item.quality == 4
        assert item.sell_in == 0

    def test_after_expired(self):
        item = BackstagePassesItem('Pass', 0, 5)

        item.update()

        assert item.quality == 0
        assert item.sell_in == -1

    def test_after_10_days(self):
        item = BackstagePassesItem('Pass', 10, 1)

        item.update()

        assert item.quality == 3
        assert item.sell_in == 9

    def test_after_5_days(self):
        item = BackstagePassesItem('Pass', 5, 1)

        item.update()

        assert item.quality == 4
        assert item.sell_in == 4


class TestDefaultItem:

    def test_after_one_day(self):
        item = DefaultItem('Item', 1, 1)

        item.update()

        assert item.quality == 0
        assert item.sell_in == 0

    def test_after_expired(self):
        item = DefaultItem('Item', 0, 20)

        item.update()

        assert item.quality == 18
        assert item.sell_in == -1

    def test_with_low_quality(self):
        item = DefaultItem('Item', 2, 0)

        item.update()

        assert item.quality == 0
        assert item.sell_in == 1


class TestConjuredItem:

    def test_after_one_day(self):
        item = ConjuredItem('Conjured', 1, 3)

        item.update()

        assert item.quality == 1
        assert item.sell_in == 0

    def test_after_expired(self):
        item = ConjuredItem('Item', 0, 20)

        item.update()

        assert item.quality == 16
        assert item.sell_in == -1

    def test_with_low_quality(self):
        item = ConjuredItem('Item', 2, 0)

        item.update()

        assert item.quality == 0
        assert item.sell_in == 1


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

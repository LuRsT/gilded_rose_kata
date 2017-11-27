import unittest

from gilded_rose import Item, GildedRose


class TestAgedBrie:

    def test_aged_brie_with_high_quality_after_one_day(self):
        item = Item('Aged Brie', 4, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.sell_in == 3
        assert item.quality == 50

    def test_aged_brie_after_one_day(self):
        item = Item('Aged Brie', 4, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.sell_in == 3
        assert item.quality == 11

    def test_aged_brie_after_expiring(self):
        item = Item('Aged Brie', 1, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()
        gilded_rose.update_quality()

        assert item.sell_in == -1
        assert item.quality == 13


class TestSulfuras:

    def test_sulfuras_after_one_day(self):
        item = Item('Sulfuras, Hand of Ragnaros', 4, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.sell_in == 4
        assert item.quality == 10

    def test_sulfuras_after_expiring(self):
        item = Item('Sulfuras, Hand of Ragnaros', -1, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.sell_in == -1
        assert item.quality == 10


class TestBackstagePasses:

    def test_backstagepasses_high_quality_after_one_day(self):
        item = Item('Backstage passes to a TAFKAL80ETC concert', 4, 50)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.sell_in == 3
        assert item.quality == 50

    def test_backstagepasses_after_one_day(self):
        item = Item('Backstage passes to a TAFKAL80ETC concert', 4, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.sell_in == 3
        assert item.quality == 13

    def test_backstagepasses_after_expiring(self):
        item = Item('Backstage passes to a TAFKAL80ETC concert', 1, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()
        gilded_rose.update_quality()

        assert item.sell_in == -1
        assert item.quality == 0

    def test_backstagepasses_after_one_day_more_than_5_days_left(self):
        item = Item('Backstage passes to a TAFKAL80ETC concert', 8, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.sell_in == 7
        assert item.quality == 12


class TestGenericItem:

    def test_genericitem_after_one_day(self):
        item = Item('Generic', 5, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.sell_in == 4
        assert item.quality == 9

    def test_genericitem_after_expiring(self):
        item = Item('Generic', 1, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()
        gilded_rose.update_quality()

        assert item.sell_in == -1
        assert item.quality == 7

    # WTF
    def test_genericitem_after_expiring_with_quality_one(self):
        item = Item('Generic', -1, 1)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.sell_in == -2
        assert item.quality == 0

    def test_genericitem_after_expiring_more(self):
        item = Item('Generic', 1, 10)
        gilded_rose = GildedRose([item])

        for _ in range(10):
            gilded_rose.update_quality()

        assert item.sell_in == -9
        assert item.quality == 0


class TestConjured:

    def test_conjured_after_one_day(self):
        item = Item('Conjured', 10, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()

        assert item.sell_in == 9
        assert item.quality == 8

    def test_conjured_after_expiring(self):
        item = Item('Conjured', 1, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()
        gilded_rose.update_quality()

        assert item.sell_in == -1
        assert item.quality == 4

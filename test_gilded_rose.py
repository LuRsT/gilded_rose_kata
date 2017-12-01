from gilded_rose import Item, GildedRose


class TestGildedRose:

    def test_items_degrade_in_quality_as_time_passes(self):
        item = Item('foo', 25, 5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.quality == 4
        assert item.sell_in == 24

    def test_when_the_sell_by_date_has_passed_items_degrade_more_quickly(self):
        item = Item('foo', 0, 5)

        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.quality == 3
        assert item.sell_in == -1

    def test_the_quality_of_an_item_is_never_negative(self):
        item = Item('foo', 0, 0)

        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.quality == 0

    def test_aged_brie_increases_in_quality(self):
        item = Item('Aged Brie', 5, 5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.quality == 6
        assert item.sell_in == 4

    def test_the_quality_of_an_item_is_never_more_than_50(self):
        item = Item('Aged Brie', 5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.quality == 50

    def test_sulfuras_never_changes(self):
        item = Item('Sulfuras, Hand of Ragnaros', 0, 5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.quality == 5

    def test_backstage_passes_increase_in_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 11

    def test_backstage_passes_increase_by_2_when_there_are_ten_days_or_fewer(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        assert item.quality == 14

    def test_backstage_passes_increase_by_3_when_there_are_five_days_or_fewer(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        assert item.quality == 16

    def test_backstage_passes_drop_to_zero_after_the_sell_by_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 10)
        gilded_rose = GildedRose([item])

        gilded_rose.update_quality()
        assert item.quality == 13

        gilded_rose.update_quality()
        assert item.quality == 0

    def test_conjured_items_degrade_twice_as_quickly(self):
        item = Item("Conjured sausage", 100, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.quality == 8


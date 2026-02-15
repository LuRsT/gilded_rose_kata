import pytest

from gilded_rose import GildedRose, Item


class TestGenericItem:
    item_name = "foo"

    def test_sell_in_below_0(self):
        # Create item
        item = Item(self.item_name, 0, 0)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality_for_items()

        # Item sell_in should decrease by one
        assert item.sell_in == -1

        # Name should remain
        assert item.name == "foo"

        # Quality should remain zero
        assert item.quality == 0

    def test_two_quality_updates(self):
        # Create item
        item = Item(self.item_name, 1, 10)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality_for_items()

        # Item sell_in should decrease by one
        assert item.sell_in == 0

        # Quality should degrade -1
        assert item.quality == 9

        # Make another day go by
        gilded_rose.update_quality_for_items()

        # Item attributes should remain
        assert item.name == "foo"

        # Quality should degrade -2 (sell-in negative)
        assert item.sell_in == -1
        assert item.quality == 7


class TestAgedBrie:
    item_name = "Aged Brie"

    def test_sell_in_below_0(self):
        # Create item
        item = Item(self.item_name, 0, 0)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality_for_items()

        # Item sell_in should decrease by one
        assert item.sell_in == -1

        # Quality should increase
        assert item.quality == 2

    def test_two_quality_updates(self):
        # Create item
        item = Item(self.item_name, 1, 10)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality_for_items()

        # Item sell_in should decrease by one
        assert item.sell_in == 0

        # Quality should increase
        assert item.quality == 11

        # Make another day go by
        gilded_rose.update_quality_for_items()

        # Item attributes should remain
        assert item.name == self.item_name

        # Quality should increase +2 (sell-in negative)
        assert item.sell_in == -1
        assert item.quality == 13

    def test_quality_of_fifty(self):
        # Create item
        item = Item(self.item_name, 1, 50)
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality_for_items()

        # Quality should remain 50
        assert item.quality == 50


class TestSulfuras:
    item_name = "Sulfuras, Hand of Ragnaros"

    def test_sell_in_below_0(self):
        # Create item
        item = Item(self.item_name, 0, 0)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality_for_items()

        # Item sell_in should remain
        assert item.sell_in == 0

        # Quality should remain
        assert item.quality == 80

    def test_two_quality_updates(self):
        # Create item
        item = Item(self.item_name, 1, 10)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality_for_items()

        # Item sell_in should remain
        assert item.sell_in == 1

        # Quality should remain
        assert item.quality == 80

        # Make another day go by
        gilded_rose.update_quality_for_items()

        assert item.sell_in == 1
        assert item.quality == 80


backstage = [
    pytest.param(
        0,
        10,
        -1,
        0,
        id="< zero",
    ),
    pytest.param(10, 10, 9, 12, id="More than 3 days"),
    pytest.param(5, 10, 4, 13, id="Less than 5 days"),
    pytest.param(1, 50, 0, 50, id="50 quality"),
    pytest.param(2, 10, 1, 13, id="Below 3 days"),
    pytest.param(11, 10, 10, 11, id="10 days"),
]


class TestBackstagePasses:
    item_name = "Backstage passes to a TAFKAL80ETC concert"

    @pytest.mark.parametrize("sell_in,quality,ex_sell_in,ex_quality", backstage)
    def test_scenarios(self, sell_in, quality, ex_sell_in, ex_quality):
        # Create item
        item = Item(self.item_name, sell_in, quality)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality_for_items()

        assert item.sell_in == ex_sell_in
        assert item.quality == ex_quality


#conjured = [
#    pytest.param(0, 10, -1, 0, id="< zero",),
#    pytest.param(11, 10, 10, 8, id=""),
#]
#
#
#class TestConjured:
#    item_name = "Conjured soup"
#
#    @pytest.mark.parametrize("sell_in,quality,ex_sell_in,ex_quality", conjured)
#    def test_scenarios(self, sell_in, quality, ex_sell_in, ex_quality):
#        # Create item
#        item = Item(self.item_name, sell_in, quality)
#
#        # Place it in gilded rose inn
#        gilded_rose = GildedRose([item])
#
#        # Make a day go by
#        gilded_rose.update_quality()
#
#        assert item.sell_in == ex_sell_in
#        assert item.quality == ex_quality

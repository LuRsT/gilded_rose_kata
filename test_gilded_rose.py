from gilded_rose import create_item, GildedRose


class TestGenericItem:

    item_name = "foo"

    def test_sell_in_below_0(self):
        # Create item
        item = create_item(self.item_name, 0, 0)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality()

        # Item sell_in should decrease by one
        assert item.sell_in == -1

        # Item attributes should remain
        assert item.name == "foo"
        assert item.quality == 0

    def test_two_quality_updates(self):
        # Create item
        item = create_item(self.item_name, 1, 10)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality()

        # Item sell_in should decrease by one
        assert item.sell_in == 0

        # Quality should degrade -1
        assert item.quality == 9

        # Make another day go by
        gilded_rose.update_quality()

        # Item attributes should remain
        assert item.name == "foo"

        # Quality should degrade -2 (sell-in negative)
        assert item.sell_in == -1
        assert item.quality == 7

class TestAgedBrie:

    item_name = "Aged Brie"

    def test_sell_in_below_0(self):
        # Create item
        item = create_item(self.item_name, 0, 0)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality()

        # Item sell_in should decrease by one
        assert item.sell_in == -1

        # Quality should increase
        assert item.quality == 2

    def test_two_quality_updates(self):
        # Create item
        item = create_item(self.item_name, 1, 10)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality()

        # Item sell_in should decrease by one
        assert item.sell_in == 0

        # Quality should increase
        assert item.quality == 11

        # Make another day go by
        gilded_rose.update_quality()

        # Item attributes should remain
        assert item.name == self.item_name

        # Quality should increase +2 (sell-in negative)
        assert item.sell_in == -1
        assert item.quality == 13

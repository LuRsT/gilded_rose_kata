from gilded_rose import item_builder, GildedRose


class TestGenericItem:

    item_name = "foo"

    def test_generic_item(self):
        # Create item
        item = item_builder(self.item_name, 0, 0)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality()

        # Item sell_in should decrease by one
        assert item.sell_in == -1

        # Item attributes should remain
        assert item.name == "foo"
        assert item.quality == 0

    def test_generic_item_quality_degradation(self):
        # Create item
        item = item_builder(self.item_name, 1, 10)

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

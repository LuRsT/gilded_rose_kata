from gilded_rose import Item, GildedRose


class TestGildedRose:

    def test_new_item_foo(self):
        # Create item
        item = Item('foo', 0, 0)

        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality()

        # Item sell_in should decrease by one
        assert item.sell_in == -1

        # Item attributes should remain
        assert item.name == "foo"
        assert item.quality == 0

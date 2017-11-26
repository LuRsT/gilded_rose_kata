from gilded_rose import Item, GildedRose


class TestGildedRose:

    def test_foo(self):
        # Create item
        item = Item('foo', 0, 0)
        # Place it in gilded rose inn
        gilded_rose = GildedRose([item])

        # Make a day go by
        gilded_rose.update_quality()

        # Check what happens
        assert item.name == 'fixme'

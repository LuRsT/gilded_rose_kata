# -*- coding: utf-8 -*-
from gilded_rose import Item, GildedRose

BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
PASSES = "Backstage passes to a TAFKAL80ETC concert"


def run_one_day(name, sell_in, quality):
    item = Item(name, sell_in, quality)
    GildedRose([item]).update_quality()
    return item.sell_in, item.quality


class TestGildedRoseCharacterization:
    # Normal items
    def test_normal_item_before_sell_date(self):
        assert run_one_day("foo", 5, 10) == (4, 9)

    def test_normal_item_after_sell_date_degrades_twice(self):
        assert run_one_day("foo", 0, 10) == (-1, 8)

    def test_quality_never_negative(self):
        assert run_one_day("foo", 5, 0) == (4, 0)

    # Aged Brie
    def test_brie_increases(self):
        assert run_one_day(BRIE, 5, 10) == (4, 11)

    def test_brie_increases_twice_after_sell_date(self):
        assert run_one_day(BRIE, 0, 10) == (-1, 12)

    def test_brie_quality_max_50(self):
        assert run_one_day(BRIE, 5, 50) == (4, 50)

    # Sulfuras
    def test_sulfuras_never_changes(self):
        assert run_one_day(SULFURAS, 5, 80) == (5, 80)

    # Backstage passes
    def test_passes_more_than_10_days(self):
        assert run_one_day(PASSES, 15, 10) == (14, 11)

    def test_passes_10_days_or_less(self):
        assert run_one_day(PASSES, 10, 10) == (9, 12)

    def test_passes_5_days_or_less(self):
        assert run_one_day(PASSES, 5, 10) == (4, 13)

    def test_passes_after_concert_drop_to_zero(self):
        assert run_one_day(PASSES, 0, 10) == (-1, 0)

    # Conjured (legacy code isko normal item ki tarah handle karta hai)
    def test_conjured_behaves_like_normal_item(self):
        assert run_one_day("Conjured Mana Cake", 5, 10) == (4, 9)

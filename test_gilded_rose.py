import unittest
from gilded_rose import Item, GildedRose  # Import your Item and GildedRose classes

class GildedRoseTest(unittest.TestCase):

    def test_normal_item_before_sell_date(self):
        items = [Item("Normal Item", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_normal_item_on_sell_date(self):
        items = [Item("Normal Item", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 18)
        self.assertEqual(items[0].sell_in, -1)

    def test_normal_item_after_sell_date(self):
        items = [Item("Normal Item", sell_in=-1, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 18)
        self.assertEqual(items[0].sell_in, -2)

    def test_normal_item_quality_never_negative(self):
        items = [Item("Normal Item", sell_in=10, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_before_sell_date(self):
        items = [Item("Aged Brie", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)
        self.assertEqual(items[0].sell_in, 9)

    def test_aged_brie_on_sell_date(self):
        items = [Item("Aged Brie", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)
        self.assertEqual(items[0].sell_in, -1)

    def test_aged_brie_after_sell_date(self):
        items = [Item("Aged Brie", sell_in=-1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)
        self.assertEqual(items[0].sell_in, -2)

    def test_aged_brie_quality_never_above_50(self):
        items = [Item("Aged Brie", sell_in=10, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_backstage_passes_long_before_sell_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[0].sell_in, 14)

    def test_backstage_passes_medium_close_to_sell_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 22)
        self.assertEqual(items[0].sell_in, 9)

    def test_backstage_passes_very_close_to_sell_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 23)
        self.assertEqual(items[0].sell_in, 4)

    def test_backstage_passes_on_sell_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_backstage_passes_after_sell_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -2)

    def test_conjured_item_degrades_twice_as_fast_before_sell_date(self):
        items = [Item("Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_degrades_twice_as_fast_after_sell_date(self):
        items = [Item("Conjured Mana Cake", sell_in=0, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)
        self.assertEqual(items[0].sell_in, -1)

    def test_normal_item_min_quality(self):
        items = [Item("Normal Item", sell_in=5, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_at_max_quality(self):
        items = [Item("Aged Brie", sell_in=5, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_backstage_passes_max_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_backstage_passes_near_sell_date_at_quality_limit(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_conjured_item_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", sell_in=0, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_item_after_sell_date_min_quality(self):
        items = [Item("Conjured Mana Cake", sell_in=-1, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

if __name__ == '__main__':
    unittest.main()

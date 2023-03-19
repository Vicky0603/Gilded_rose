# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_agedbrie(self):
        items = [Item("Aged Brie", 2, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[0].sell_in)

        items = [Item("Aged Brie", -1, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, gilded_rose.items[0].quality)

    def test_backstage(self):
        # quality increases by 3 when there are 5 days or less
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[0].sell_in)

        # quality increases by 2 when there are 10 days or less
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, gilded_rose.items[0].quality)
        self.assertEqual(9, gilded_rose.items[0].sell_in)

        # quality drops to 0 after the concert
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, gilded_rose.items[0].quality)
        self.assertEqual(2, gilded_rose.items[0].sell_in)

    def test_conjured(self):
        items = [Item("Conjured", 2, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[0].sell_in)


if __name__ == '__main__':
    unittest.main()

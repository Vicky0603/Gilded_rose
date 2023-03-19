# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
#if an item is not "Aged Brie" or "Backstage passes to a TAFKAL80ETC concert", its quality decreases by 1 each day, unless it is "Sulfuras, 
# Hand of Ragnaros" which does not change. If an item is "Aged Brie" or "Backstage passes to a TAFKAL80ETC concert", its quality increases by 1 
# each day until the sell_in date is reached, at which point the quality increases more rapidly, with the increase happening twice 
# as fast for "Backstage passes". 
# If an item has passed its sell_in date, its quality decreases twice as fast, unless it is "Aged Brie" which increases in quality instead.
    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

#It defines an object with a name, sell_in, and quality value, and a __repr__ method to display these values when the object is printed.
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
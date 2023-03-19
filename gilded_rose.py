# -*- coding: utf-8 -*-

from items import *

#defines a mapping between item names and their corresponding item classes. The items 
# dictionary defines the name-to-class mapping, where each item class represents a specific item type with its own rules for quality updates.
class ItemMapping(object):
    items = {
        "Aged Brie": AgedBrieItem,
        "Sulfuras, Hand of Ragnaros": SulfurasItem,
        "Backstage passes to a TAFKAL80ETC concert": BackStageItem,
        "Conjured": ConjuredItem
    }

#this method takes an item object and creates an instance of the appropriate item class 
# based on the name of the item. If the item name is not found in the items mapping, it creates an instance of the default UpdateItem class.
# It checks if the name attribute of the item passed as a parameter is in the items dictionary, 
# which contains the mapping of item names to item classes. If the name attribute is found, it returns a new instance of the corresponding item class with the item parameter passed to it. If the name attribute is not found in the dictionary, it returns a new instance of the UpdateItem class with the item parameter passed to it. 
# This way, if there is no specific class for an item, the generic UpdateItem class is used to update the item's quality.
    @classmethod
    def create(cls, item):
        if item.name in cls.items:
            return cls.items[item.name](item)
        return UpdateItem(item)

#defines the main logic for updating the quality of items. The update_quality method iterates through each item in the items list 
# and creates an instance of the appropriate 
# item class using the ItemMapping class. The update_quality method of the item instance is then called to update the quality of the item.
class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            itemMapping = ItemMapping.create(item)
            itemMapping.update_quality()

#defines the basic properties of an item, including its name, sell_in value, and quality.
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

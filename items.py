# -*- coding: utf-8 -*-
#defines a UpdateItem class that represents a generic item with no specific rules for how its quality should be updated.
#The class also has four methods:
#increase_quality: This method increases the quality of the item by 1, but only if the quality is less than the max_quality limit, 
# which is set to 50.
#decrease_quality: This method decreases the quality of the item by 1, but only if the quality is greater than 0.
#decrease_sell_in: This method decreases the sell_in value of the item by 1.
#update_quality: This method calls the decrease_quality and decrease_sell_in methods, and then decreases the quality of the item again if its sell_in value is less than 0.
class UpdateItem(object):
    #The quality of an item is never more than 50 - TASK CONDITION
    max_quality = 50

    def __init__(self, item):
        self.item = item

    def increase_quality(self):
        if self.item.quality < self.max_quality:
            self.item.quality = self.item.quality + 1

    def decrease_quality(self):
        #The quality of an item is never negative
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

    def decrease_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def update_quality(self):
        self.decrease_quality()
        self.decrease_sell_in()

        if self.item.sell_in < 0:
            self.decrease_quality()

#The AgedBrieItem class overrides the update_quality method to increase the quality of the item, 
# with the increase happening twice as fast after the sell_in date has passed.
#"Aged Brie" actually increases in quality the older it gets - TASK CONDITION
class AgedBrieItem(UpdateItem):
    def update_quality(self):
        self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.increase_quality()

#The BackStageItem class overrides the update_quality method to increase the quality of the item as the sell_in date approaches, 
# with the increase happening more rapidly when the sell_in date is very close. If the sell_in date has passed, the quality is set to 0.
#"Backstage passes", like aged brie, increases in quality as its sell-in value approaches; quality increases by 2 when there are 10 days or less 
# and by 3 when there are 5 days or less but quality drops to 0 after the concert - TASK CONDITION
class BackStageItem(UpdateItem):
    days_threshold_min = 10
    days_threshold_max = 5

    def reset_quality(self):
        self.item.quality = 0

    def update_quality(self):
        self.increase_quality()
        if self.item.sell_in <= self.days_threshold_min:
            self.increase_quality()
        if self.item.sell_in <= self.days_threshold_max:
            self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.reset_quality()

#The SulfurasItem class overrides the update_quality method to do nothing, 
# because the quality and sell_in values of Sulfuras items do not change.
#"Sulfuras", being a legendary item, never has to be sold or decreases in quality - TASK CONDITION
class SulfurasItem(UpdateItem):
    def update_quality(self):
        pass

#The ConjuredItem class overrides the decrease_quality method to decrease the quality of the item twice as fast as the UpdateItem class.
#"Conjured" items degrade in quality twice as fast as normal items - TASK CONDITION
class ConjuredItem(UpdateItem):
    def decrease_quality(self):
        UpdateItem.decrease_quality(self)
        UpdateItem.decrease_quality(self)

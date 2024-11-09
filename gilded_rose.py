# -*- coding: utf-8 -*-

class GildedRose:

    def __init__(self, items, default_quality_change_rate=1, normal_quality_min=0, normal_quality_max=50) -> None:
        self.items = items
        self.default_quality_change_rate = default_quality_change_rate
        self.normal_quality_min = normal_quality_min
        self.normal_quality_max = normal_quality_max

    def update_quality(self) -> None:
        for item in self.items:

            # handle no op items
            if self.is_legendary_item(item):
                continue

            # one day has passed
            item.sell_in = item.sell_in - 1
            is_expired = item.sell_in < 0

            if self.is_appreciating_item(item):
                self.update_appreciating_item_quality(item, is_expired)
            else:
                # handle normal itmes, where quality drops over time.  expired items and conjured items double the rate
                if item.quality > self.normal_quality_min:
                    quality_decay = self.default_quality_change_rate
                    if is_expired:
                        quality_decay *= 2
                    if self.is_conjured_item(item):
                        quality_decay *= 2
                    item.quality -= quality_decay

            self.enforce_quality_limits(item)

    def is_appreciating_item(self, item) -> bool:
        APPRECIATING_ITEMS = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]
        return item.name in APPRECIATING_ITEMS

    def is_legendary_item(self, item) -> bool:
        LEGENDARY_ITEMS = ["Sulfuras, Hand of Ragnaros"]
        return item.name in LEGENDARY_ITEMS

    def is_conjured_item(self, item) -> bool:
        # NOTE: we are assuming this is how all conjured items are, as the instructions don't specify how to identify conjured items
        return item.name.startswith("Conjured")

    def update_appreciating_item_quality(self, item, expired) -> None:
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes_quality(item, expired)
        else:
            # expired items change at double the rate
            if expired:
                item.quality += self.default_quality_change_rate * 2
            else:
                item.quality += self.default_quality_change_rate

    def update_backstage_passes_quality(self, item, expired) -> None:
        if expired:
            item.quality = self.normal_quality_min
        elif item.sell_in < 6:
            item.quality += 3
        elif item.sell_in < 11:
            item.quality += 2
        else:
            #NOTE: this isn't explicit in the instructions, but I believe it's the correct behavior
            item.quality += self.default_quality_change_rate

    def enforce_quality_limits(self, item) -> None:
        """ If above or below quality limits, set to the limit """
        if item.quality < self.normal_quality_min:
            item.quality = self.normal_quality_min
        if item.quality > self.normal_quality_max:
            item.quality = self.normal_quality_max

##### DO NOT MODIFY BELOW THIS LINE #####

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

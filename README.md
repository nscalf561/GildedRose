# Gilded Rose Refactoring Challenge

This repository contains a refactored solution for the "Gilded Rose" kata in Python. The goal of the challenge was to improve the readability and maintainability of the legacy code while preserving its original behavior.

## Project Structure

- **gilded_rose.py**: Contains the refactored `GildedRose` class and `Item` class.
- **test_gilded_rose.py**: Includes a suite of unit tests that verify the behavior of different item types, including edge cases, to ensure the refactored code functions correctly.

## Refactoring Strategy

### Key Improvements
1. **Extracted Logic**: Moved complex or unique item behaviors (e.g., `Aged Brie` and `Backstage passes`) into separate helper methods (`update_appreciating_item_quality` and `update_backstage_passes_quality`), making the `update_quality` method clearer and reducing nested conditionals.  This could also be moved to subclass types, so that each subclass of item has it's own `update_quality` method.
2. **Constants and Configurable Limits**: Replaced hard-coded values with constants and configurable attributes (e.g., `default_quality_change_rate`, `normal_quality_min`, and `normal_quality_max`) to improve flexibility.
3. **Simplified Conditionals**: Used helper methods to simplify conditions, such as checks for expired items, quality thresholds, and item-specific rules, making the code more readable.
4. **Edge Case Handling**: Implemented  checks to enforce quality limits for all items, including the new "Conjured" items that degrade twice as fast.

## Testing Strategy

A comprehensive test suite verifies the behavior of each item type under various conditions. The tests check the following scenarios:

- **Standard Items**: Quality decreases over time and at double rate past the sell date. Quality never drops below zero.
- **Aged Brie**: Quality increases over time and at double rate past the sell date, capped at a maximum quality of 50.
- **Sulfuras**: Quality and sell date remain constant.
- **Backstage Passes**: Quality increases as the sell date approaches, with specific thresholds for faster increases. Quality drops to zero after the sell date.
- **Conjured Items**: Quality degrades twice as fast as normal items, respecting quality limits.

## Considerations for future changes

Much of the work to make things like item lists easily configurable have been done.  Instead of a hardcoded list to check, it could be moved to the class init so full lists can be passed in.  Since we moved the checks to their own function, adjustments like that would be very minimal.  Instead of hardcoding some values, like the quality limits, we've made them default values within the init (in case a conjuring goes wrong and can only be half as high quality).

Another change that should be explored when revisted is error handling and logging.  Right now there is none since it was a bit out of the scope of this project, but best practices would have some logging and gracefully handling errors.  Some validation, like items starting with qualities out of normal bounds, could have unique handling that might involve throwing an error or at least logging out for further tracking.

## Instructions

To run the tests, simply execute the following:

```bash
python -m unittest test_gilded_rose.py

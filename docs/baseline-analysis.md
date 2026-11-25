# Baseline Analysis: Gilded Rose (Group 1)

## Code Smells and Planned Refactorings
| # | Code Smell | Location | Fowler Technique | Branch |
|---|---|---|---|---|
| 1 | Magic Numbers and Magic Strings (50, 0, 11, 6; item names repeated about 9 times) | update_quality, lines 8-34 | Replace Magic Number with Symbolic Constant | refactor/constants |
| 2 | Long Method (one method does everything) | update_quality, lines 6-34 | Extract Method | refactor/extract-method |
| 3 | Duplicate Code (increase/decrease quality repeated 6 times) | lines 9-11, 13-14, 17-18, 20-21, 27-29, 33-34 | Extract Method (increase_quality, decrease_quality) | refactor/extract-method |
| 4 | Deeply Nested Conditionals (up to 7 levels) | lines 8-21 and 24-34 | Decompose Conditional / Guard Clauses | refactor/guard-clauses |
| 5 | Type-checking conditionals on item name | lines 8, 10, 15, 22, 25, 26, 28 | Replace Conditional with Polymorphism | refactor/polymorphism |
| 6 | Obscure expression (quality - quality means set to 0) | line 31 | Simplify expression | refactor/guard-clauses |

## Characterization Tests
test_gilded_rose.py has 12 tests that capture the current behavior
(normal items, Aged Brie, Sulfuras, Backstage passes, Conjured).
They must pass before and after every refactoring.

## Target Design
See docs/design-model.png (after) and docs/design-before.png (before).
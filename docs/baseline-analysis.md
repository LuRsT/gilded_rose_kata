# Baseline Code Analysis - Gilded Rose

## Identified Code Smells & Refactoring Techniques

| # | Code Smell | Location | Refactoring Technique |
|---|---|---|---|
| 1 | **Magic Numbers & Strings** | Hardcoded numbers (`50`, `0`, `11`, `6`) and item strings (`"Aged Brie"`, `"Sulfuras..."`) inside `update_quality()`. | **Replace Magic Literal with Symbolic Constant** |
| 2 | **Long Method** | `update_quality()` contains all business rules for every item type in one large loop. | **Extract Method** |
| 3 | **Deeply Nested Conditionals** | Deeply nested `if-else` blocks (up to 4 levels) make the logic hard to read and maintain. | **Decompose Conditional / Guard Clauses** |
| 4 | **Duplicate Code** | Repeated checks for `item.quality < 50` and `item.quality > 0` before updating quality. | **Extract Method** |
| 5 | **Type Checking / Switch Logic** | Repeatedly checking `item.name` instead of using polymorphic classes. | **Replace Conditional with Polymorphism** |

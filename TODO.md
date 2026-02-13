# Gilded Rose Refactoring Strategies

Pick one per session, reset the code, and try again with a different approach next time.

- [ ] Replace conditional with polymorphism (Strategy/Template Method pattern)
- [ ] Extract Method + Replace Type Code with State/Strategy
- [ ] Lift-up conditional / flatten nested ifs with guard clauses
- [ ] Replace conditional logic with a lookup table / dispatch dictionary
- [ ] Decompose using the Compose Method pattern (small, same-level-of-abstraction methods)
- [ ] Use the Adapter pattern to wrap Item without modifying it
- [ ] Extract interface + dependency inversion (define an ItemUpdater protocol)
- [ ] Replace imperative logic with a declarative rules engine / data-driven config
- [ ] Strangler Fig pattern (incrementally replace branches one item type at a time)
- [ ] Use the Decorator pattern to layer quality-clamping and sell_in-decrement concerns
- [ ] Parse, don't validate: model item categories as distinct types with a factory
- [ ] Chain of Responsibility (each handler decides if it applies to the item)

# Gilded Rose kata for Python 3

This is basically a copy of https://github.com/emilybache/GildedRose-Refactoring-Kata
except that it's just the Python one, and I changed it to be used with Python 3.

I've addded some instructions for using this repo and pasted some of the README
from that original repo.

## How to setup:

Create a virtualenv with python 3.* (tested on Python3.6) and install `pytest`

## How to run:

Just use the `Makefile`:

- `make` to run unit tests
- `make gold` to run golden test

Alternatively, read the Makefile and execute the commands inside, it's just 4
lines.

## How to kata this kata:

This Kata was originally created by Terry Hughes (http://twitter.com/#!/TerryHughes). It is already on GitHub [here](https://github.com/NotMyself/GildedRose). See also [Bobby Johnson's description of the kata](http://iamnotmyself.com/2011/02/13/refactor-this-the-gilded-rose-kata/).

## How to use this Kata

The simplest way is to just clone the code and start hacking away improving the design. You'll want to look at the ["Gilded Rose Requirements"](https://github.com/lurst/gilded_rose_python/blob/master/GildedRoseRequirements.txt) which explains what the code is for. I strongly advise you that you'll also need some tests if you want to make sure you don't break the code while you refactor.

You could write some unit tests yourself, using the requirements to identify suitable test cases. I've provided a failing unit test in a popular test framework as a starting point for most languages.

Alternatively, use the "Text-Based" tests provided in this repository. (Read more about that in the next section)

Whichever testing approach you choose, the idea of the exercise is to do some deliberate practice, and improve your skills at designing test cases and refactoring. The idea is not to re-write the code from scratch, but rather to practice designing tests, taking small steps, running the tests often, and incrementally improving the design.

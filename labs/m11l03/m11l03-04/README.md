# m11l03-04 · The methods every graphics object has

**Lesson:** [Reading The graphics.py Documentation](https://learnsome.tech/learn/python-course/m11l03) (lesson 11.3, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can find any graphics method for yourself in the reference, by knowing whether it belongs to every graphics object, to one particular type, or to the window, and you know the additions this tutorial makes to Zelle's package.

In the lesson: This is the shared section, and it is the most valuable page in the reference. Draw, undraw, move and clone work on any graphics object, whether it is a point, a circle, a polygon or a piece of text. Draw makes an object visible in a window, and undraw takes it away again without destroying it. Move shifts an object by an amount in each direction; it is a shift, not a destination. Clone makes a separate copy, which sounds dull now and matters enormously in the next module. The three set methods change fill colour, outline colour and line width, but each applies only where it makes sense: setWidth is for outlines and lines, so asking a point or a piece of text for a width raises an error, and a piece of text has no outline to set either.

## Files

- [`starter/the-methods-every-graphics-object-has.txt`](starter/the-methods-every-graphics-object-has.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-methods-every-graphics-object-has.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

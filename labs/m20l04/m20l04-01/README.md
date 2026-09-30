# m20l04-01 · What a dunder method is

**Lesson:** [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) (lesson 20.4, module 20: Object Oriented Python) · Pro  
**Check:** Read along

## Goal

You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

In the lesson: You have met one already: dunder init. The word dunder is short for double underscore, because the name has two underscores before it and two after. These names are the language's own hooks. Almost every piece of Python syntax is defined as a call to a dunder method on the object involved, and so is almost every built-in function that works on many types. Asking for the length of something calls its dunder len. Adding two things calls dunder add on the left one. Comparing with the double equals calls dunder eq. So a dunder method is how your class joins in with the language rather than sitting outside it. You define them and let Python call them; you very rarely call them by hand.

## Files

- [`starter/what-a-dunder-method-is.py`](starter/what-a-dunder-method-is.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/what-a-dunder-method-is.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m20l04-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

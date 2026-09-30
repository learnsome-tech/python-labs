# m12l02-07 · Mutable objects and aliases

**Lesson:** [Chapter Two In One Sitting](https://learnsome.tech/learn/python-course/m12l02) (lesson 12.2, module 12: Files And Chapter Review) · Pro  
**Check:** Read along

## Goal

You can name every object, method and technique chapter two introduced, and say which section to return to for any of them that you cannot yet explain.

In the lesson: Care must be taken whenever a second name is assigned to a mutable object. The second name is an alias: it refers to the very same object, so a mutating method applied through either name changes the one object that both names see. That was the bug behind the rectangle that came out in the wrong place. Many mutable types offer a way to make a copy that really is a distinct object. Zelle's graphical objects have the clone method, and a copy of a list can be made with a full slice. Then appending to one list leaves the other alone, although a mutable element inside both is still shared.

## Files

- [`starter/mutable-objects-and-aliases.py`](starter/mutable-objects-and-aliases.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/mutable-objects-and-aliases.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m12l02-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m12l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

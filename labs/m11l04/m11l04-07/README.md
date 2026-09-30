# m11l04-07 · Cloning gives you a separate object

**Lesson:** [Mutable Objects And Aliases](https://learnsome.tech/learn/python-course/m11l04) (lesson 11.4, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can explain why assigning one name from another gives two names for a single object, predict when mutating through one name is visible through the other, and use clone or a full slice to get a genuinely separate object.

In the lesson: The fix is one method call. Every graphical object in graphics dot py defines clone, which creates a separate object that is a copy with an equivalent state. So change the line that sets corner two from corner into a line that sets corner two from corner dot clone. After the cloning, corner and corner two refer to points with equivalent coordinates, but they do not refer to the same object. Two arrows, two objects. Now the move changes only the clone, and the original corner stays where the caller put it. No conflict: the two names describe the two corners we actually wanted.

## Files

- [`starter/cloning-gives-you-a-separate-object.py`](starter/cloning-gives-you-a-separate-object.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/cloning-gives-you-a-separate-object.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l04-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

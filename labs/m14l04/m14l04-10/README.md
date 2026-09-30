# m14l04-10 · What or means when the operands are not Boolean

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: The meaning of a or b, and of a and b, is exactly as discussed so far if each of the operands really is Boolean. More elaborate definitions are needed when an operand is not. The top line here is the expression, and the lines below it are what that expression means. For or, if a converts to True, the value is a itself, and otherwise the value is b. Notice that neither branch produces a Boolean unless a or b happened to be one already. That is exactly why the shell handed you strings a moment ago.

## Files

- [`starter/what-or-means-when-the-operands-are-not-bool.py`](starter/what-or-means-when-the-operands-are-not-bool.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/what-or-means-when-the-operands-are-not-bool.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l04-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

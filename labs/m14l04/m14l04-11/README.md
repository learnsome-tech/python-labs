# m14l04-11 · And is the mirror image, and short circuiting

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: And is the mirror image. If a converts to True, the value of a and b is b, and otherwise the value is a. In both definitions Python stops as soon as it knows the answer, which is what people mean by short circuiting: the second operand may never be evaluated at all. That matters when the second operand would raise an error, or has an effect of its own. One operator does not behave in this way. The not operator always produces a result of type bool, either True or False, whatever kind of object you hand it.

## Files

- [`starter/and-is-the-mirror-image-and-short-circuiting.py`](starter/and-is-the-mirror-image-and-short-circuiting.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/and-is-the-mirror-image-and-short-circuiting.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l04-11` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

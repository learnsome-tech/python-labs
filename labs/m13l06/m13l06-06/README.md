# m13l06-06 · Putting them into conditions

**Lesson:** [More String Methods](https://learnsome.tech/learn/python-course/m13l06) (lesson 13.6, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can test what a string starts with, ends with or is made of, and build up conditions from string methods such as startswith, endswith, replace and isdigit.

In the lesson: Now combine what you have. The first test on screen asks whether a string is a negative whole number: it must start with a minus sign, and everything after the first character must be digits. Because both must hold, the connector is and. Short circuit evaluation helps here too, since the slice is only examined when the first test has already passed. The second shows not in front of a method call. When you write tests like these, spend as much thought on the awkward inputs as on the ordinary ones. What should a string holding nothing but a minus sign give you?

## Files

- [`starter/putting-them-into-conditions.py`](starter/putting-them-into-conditions.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/putting-them-into-conditions.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l06-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

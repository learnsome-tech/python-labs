# m13l05-12 · Which button was clicked?

**Lesson:** [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) (lesson 13.5, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

In the lesson: Most of the rest of the program is scenery: a function that makes a coloured rectangle, and calls that draw three buttons and the parts of a house. That is all above this screen. What matters is this fragment. It waits for a mouse click, then runs an elif chain asking, for each button in turn, whether the click was inside it. The first one that says yes wins, and the final else covers a click anywhere else. Below this the same block appears again for the door, which is why the program is longer than it needs to be.

## Files

- [`starter/chooseButton1.py`](starter/chooseButton1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/chooseButton1.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l05-12` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

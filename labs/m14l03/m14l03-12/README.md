# m14l03-12 · The outer loop that follows the clicks

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: Wrapped around that animation is this short function. Each mouse click should switch the ball toward the click, until the stopping condition: a click above the stop line. That is repetitive, so it needs a while loop, and the condition tests the y coordinate of the click against the height of the stop line. The body is very short, because getShift already works out the change in x and y. The last click is initialised to the centre of the ball, so it does not move at first.

## Files

- [`starter/bounce3.py`](starter/bounce3.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounce3.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-12` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

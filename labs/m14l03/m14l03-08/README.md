# m14l03-08 · checkMouse looks, getMouse waits

**Lesson:** [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) (lesson 14.3, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

In the lesson: In the earlier animations a while loop would have helped too. Rather than repeating a fixed number of times, it would be nicer for the user to click when she has watched long enough. The only way to use the mouse so far was getMouse, and that stops and waits, which is no use in an animation. Zelle's graphics registers every click anyway, and checkMouse returns that remembered click, the most recent one in the past. When there has been no click since you last looked, it returns None. So the loop never pauses.

## Files

- [`starter/checkmouse-looks-getmouse-waits.txt`](starter/checkmouse-looks-getmouse-waits.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/checkmouse-looks-getmouse-waits.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l03-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

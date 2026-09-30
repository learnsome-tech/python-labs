# m17l04-06 · Stepping until the bug is visible

**Lesson:** [Debugging: print, breakpoint, and the debugger](https://learnsome.tech/learn/python-course/m17l04) (lesson 17.4, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Read along

## Goal

You can debug a wrong answer deliberately: label your printing, stop a program with breakpoint, step through it with the pdb commands that matter, read the state instead of guessing, and choose between a debugger and a test.

In the lesson: Now watch the arrow move. Two nexts and we are at the for statement, one more and we are at the condition, with the first value in hand. The letter p, for print, evaluates any expression you like, so ask what the two variables hold: the value is minus five and the best is zero. Next again, and here is the whole bug, visible without reading a word of code: the arrow jumps from the condition straight back to the for statement, so the assignment was skipped. Round again, same thing. The letter w, for where, prints the frames you are inside. And q quits, which asks for confirmation because quitting kills the program.

## Files

- [`starter/runmaxdebug.py`](starter/runmaxdebug.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/runmaxdebug.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m17l04-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

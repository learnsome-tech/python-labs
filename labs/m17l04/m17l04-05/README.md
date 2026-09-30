# m17l04-05 · breakpoint, and where am I

**Lesson:** [Debugging: print, breakpoint, and the debugger](https://learnsome.tech/learn/python-course/m17l04) (lesson 17.4, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Read along

## Goal

You can debug a wrong answer deliberately: label your printing, stop a program with breakpoint, step through it with the pdb commands that matter, read the state instead of guessing, and choose between a debugger and a test.

In the lesson: Add one line to the program: a call to the built in breakpoint function, on the line before the interesting call. Run the program normally. Instead of finishing, it stops and hands you a prompt, and that prompt is Python's own debugger, called pdb. It has already told you where you are: the file, the line number in brackets, the name of the function, and the line about to run, marked with an arrow. The letter l, for list, shows the source around you. The letter n, for next, runs the current line and stops again. The letter s, for step, is different: at a call it goes inside, which is how we get into the function.

## Files

- [`starter/runmaxdebug.py`](starter/runmaxdebug.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/runmaxdebug.py` alongside the lesson.
2. Notes from the lesson:
   - Line 8: breakpoint() stops here and opens the debugger, pdb

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m17l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

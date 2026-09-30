# m03l01-06 · The two lines that actually start everything

**Lesson:** [A Sample Program, Explained](https://learnsome.tech/learn/python-course/m03l01) (lesson 3.1, module 3: Meet Idle And The Shell) · Pro  
**Check:** Read along

## Goal

You can read madlib.py from top to bottom and say what each line contributes, from the shebang and the documentation string to the format string, the two definitions and the two calls that start everything.

In the lesson: Two lines are left, and neither of them is indented, so both belong to the program itself rather than to a definition. The definition of tellStory above does not make the computer do anything besides remember what the instruction tellStory means. It is only in this line, with the name followed by parentheses, that the whole sequence of remembered instructions is actually carried out. And the very last line is only here to accommodate running the program in Windows by double clicking on its file icon. Without this line the story would be displayed, the program would end, and Windows would make the window immediately disappear from the screen. This line forces the program to continue being displayed until there is another response from the user, and meanwhile the user may read the output from tellStory in peace.

## Files

- [`starter/madlib.py`](starter/madlib.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/madlib.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: actually carried out
   - Lines 2: the very last line
3. Notes from the lesson:
   - Line 1: A name plus parentheses: here the remembered steps finally run
   - Line 2: Holds a double-clicked Windows console open until you respond

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

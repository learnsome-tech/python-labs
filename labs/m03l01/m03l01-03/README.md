# m03l01-03 · The story, kept as a format string

**Lesson:** [A Sample Program, Explained](https://learnsome.tech/learn/python-course/m03l01) (lesson 3.1, module 3: Meet Idle And The Shell) · Pro  
**Check:** Read along

## Goal

You can read madlib.py from top to bottom and say what each line contributes, from the shebang and the documentation string to the format string, the two definitions and the two calls that start everything.

In the lesson: Now the largest piece. The equal sign tells the computer that this is an assignment statement. The computer will associate the value of the expression between the triple quotes, a multi-line string, with the name on the left, storyFormat. Everything from there down to the closing triple quotes is the body of the string. This one contains some special symbols making it a format string, unlike the plain documentation string we just read. The parts enclosed in braces are places where a substitute string will be inserted later. The substituted text comes from a custom dictionary, created while the program runs, holding the user's own definitions. So the words in the braces, animal, food and city, tell you that animal, food and city are words in that dictionary. One more thing to notice across the whole file: the blank lines between statements. They are included for human readability, to separate logical parts, and the computer ignores them entirely. The one inside the story is part of the string, so it does get printed.

## Files

- [`starter/madlib.py`](starter/madlib.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/madlib.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: an assignment statement
   - Lines 2–15: the body of the string
3. Notes from the lesson:
   - Line 1: The equal sign ties the value on the right to the name on the left
   - Line 3: Each word in braces marks where a substitute string goes later

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

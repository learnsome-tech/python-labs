# m06l02-08 · Outdent one line and the answer changes

**Lesson:** [Several Functions, And Flow Of Control](https://learnsome.tech/learn/python-course/m06l02) (lesson 6.2, module 6: Functions) · Pro  
**Check:** Read along

## Goal

You can put several function definitions in one file, predict the order in which the lines are executed, and see how indentation decides what is remembered and what is run.

In the lesson: Now modify the file so that the second print function is outdented, as on screen. What should happen now? Try it. The answer arrives first, before the words from inside the function. The line asking when this prints is no longer part of the definition, so the interpreter runs it in order of appearance, on the way down the file. Then the last line calls f, and the one remaining line of the body prints. So the two lines of output come out in the opposite order from before. Lines indented inside a definition are remembered first and executed only when the function is invoked. Lines outside any definition are executed in order of appearance. Four spaces changed the output, which is why Python programmers are fussy about indentation.

## Files

- [`starter/outdent-one-line-and-the-answer-changes.py`](starter/outdent-one-line-and-the-answer-changes.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/outdent-one-line-and-the-answer-changes.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m10l02-05 · One pick, and all the picks

**Lesson:** [Mad Libs Revisited: The Whole Program](https://learnsome.tech/learn/python-course/m10l02) (lesson 10.2, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can read the revised mad lib program function by function, explain why getKeys returns a set, and name the creative problem solving steps that produced it.

In the lesson: The step of filling the dictionary with the user's choices now lives in functions of its own. The first one asks the user for one cue: it builds a prompt with the format method, reads the reply with the input function, and stores the reply in the dictionary under that cue. It came straight from the earlier mad lib program. Then a second function loops over the whole collection of cues, starts an empty dictionary, calls the first function once per cue, and returns the finished dictionary. Two small functions, each with one job, each easy to name. Notice that the dictionary is passed in to the first function and mutated there, which is why nothing needs to be returned from it.

## Files

- [`starter/madlib2.py`](starter/madlib2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/madlib2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: asks the user for one cue
   - Lines 9–11: a second function
   - Lines 12–18: returns the finished dictionary

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

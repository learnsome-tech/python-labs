# m10l02-06 · The story teller in five lines

**Lesson:** [Mad Libs Revisited: The Whole Program](https://learnsome.tech/learn/python-course/m10l02) (lesson 10.2, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can read the revised mad lib program function by function, explain why getKeys returns a set, and name the creative problem solving steps that produced it.

In the lesson: This is the heart of the program, and it is five lines long. The documentation string says what the parameter is: a story with dictionary references embedded in braces. Then the cues come out of the story, the user's picks come from the cues, the story format is filled in with those picks, and it prints the result. The story is a parameter now, not something baked into the function, which is what makes a new story easy to drop in. The filling in uses the format method with the double star in front of the dictionary, which hands every entry over as a keyword argument, the trick we met when we first formatted from a dictionary.

## Files

- [`starter/madlib2.py`](starter/madlib2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/madlib2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the documentation string
   - Lines 6–7: the cues come out of the story
   - Lines 8–9: prints the result
3. Notes from the lesson:
   - Line 8: The double star hands each dictionary entry to format as a keyword

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

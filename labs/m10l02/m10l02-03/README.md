# m10l02-03 · One blemish left: the duplicates

**Lesson:** [Mad Libs Revisited: The Whole Program](https://learnsome.tech/learn/python-course/m10l02) (lesson 10.2, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can read the revised mad lib program function by function, explain why getKeys returns a set, and name the creative problem solving steps that produced it.

In the lesson: There is one thing still in the way of using getKeys inside a mad lib program: the list that comes back has unwanted repetitions in it. We would prompt for the animal five times. How do we build a collection without repetitions? We could make a set out of the list at the point of use, but the neater answer is to have getKeys return a set in the first place. That is a change to one word in the return statement and a change to one word in the documentation string, which must now promise a set rather than a list. Everything else about the function stays exactly as we built it. Around that we will now assemble the revised program.

## Files

- [`starter/one-blemish-left-the-duplicates.txt`](starter/one-blemish-left-the-duplicates.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/one-blemish-left-the-duplicates.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

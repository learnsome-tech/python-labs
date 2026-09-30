# m06l04-03 · How arguments reach parameter names

**Lesson:** [Multiple Parameters](https://learnsome.tech/learn/python-course/m06l04) (lesson 6.4, module 6: Functions) · Pro  
**Check:** Read along

## Goal

You can define and call a function with several parameters, and explain how the arguments are matched to the parameter names from left to right.

In the lesson: The actual parameters in a call are evaluated left to right, and then those values are associated with the formal parameter names in the definition, also left to right. Take the call at the top of the screen, with three actual parameters, going to a function whose definition heading is underneath it. The call acts approximately as if the first lines executed inside the function were the three assignments at the bottom: each formal name given the matching actual value. Position is everything here; the only exception is the keyword parameters you met with the print function. So if you pass the numbers in the wrong order, Python cannot help you, and neither will it complain. Count the parameters, and count the arguments, and read both from the left.

## Files

- [`starter/how-arguments-reach-parameter-names.py`](starter/how-arguments-reach-parameter-names.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/how-arguments-reach-parameter-names.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

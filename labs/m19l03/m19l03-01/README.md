# m19l03-01 · Two ways to sort, and they differ

**Lesson:** [Sorting, Keys And Lambdas](https://learnsome.tech/learn/python-course/m19l03) (lesson 19.3, module 19: Data Structures In Depth) · Pro  
**Check:** Read along

## Goal

You can sort anything by any rule using sorted with a key function, write a lambda for that key, and use stability to sort by two rules in turn.

In the lesson: Sorting is the everyday job that teaches you the most about Python, so we take it slowly. There are two ways, and the difference is the same one you met between a function that returns and a function that acts. The built in function sorted takes anything you can loop over and hands back a new list, leaving your data alone. The list method sort rearranges the list itself and returns None, like append. So assigning the result of sort to a name gives you None, which is the mistake on the third line and one of the most common in the language. Prefer sorted. Reach for sort only when the list is large and you genuinely want it changed where it sits.

## Files

- [`starter/two-ways-to-sort-and-they-differ.py`](starter/two-ways-to-sort-and-they-differ.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/two-ways-to-sort-and-they-differ.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m19l03-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m14l04-08 · Two correct ways to write that condition

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: The intention of the person writing that line was presumably something like the first version here: the answer equals y, or the answer equals yes. Written out with both comparisons in full, it says what it means, and it translates directly into other languages too. There is another correct and more Pythonic alternative, which groups the alternative values together: test whether the answer is in a list of the acceptable answers. That one reads pretty much like English. Be careful to use a correct expression whenever you want a condition of this kind.

## Files

- [`starter/two-correct-ways-to-write-that-condition.txt`](starter/two-correct-ways-to-write-that-condition.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/two-correct-ways-to-write-that-condition.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l04-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

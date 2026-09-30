# m19l04-01 · Iteration is an agreement, not a type

**Lesson:** [Iterators And Generators](https://learnsome.tech/learn/python-course/m19l04) (lesson 19.4, module 19: Data Structures In Depth) · Pro  
**Check:** Read along

## Goal

You can explain what a for loop does in terms of iter and next, write a generator function with yield, and say why a generator costs no memory however long its sequence is.

In the lesson: You have looped over lists, strings, dictionaries, files and ranges, and the for loop never had to know which it was given. That is because iteration in Python is an agreement between the loop and the thing being looped over, and the agreement has only two rules. Ask a thing for an iterator over itself, with the built in function iter. Then ask that iterator for one more value, with the built in function next. When there is nothing left, next signals the end by raising an exception called StopIteration. Anything that obeys those two rules can be used in a for loop, including the objects you will write yourself in this lesson. Nothing else is required: not a length, not indexing, not being a collection at all.

## Files

- [`starter/iteration-is-an-agreement-not-a-type.py`](starter/iteration-is-an-agreement-not-a-type.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/iteration-is-an-agreement-not-a-type.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m19l04-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m19l03-03 · The key argument, and the lambda

**Lesson:** [Sorting, Keys And Lambdas](https://learnsome.tech/learn/python-course/m19l03) (lesson 19.3, module 19: Data Structures In Depth) · Pro  
**Check:** Read along

## Goal

You can sort anything by any rule using sorted with a key function, write a lambda for that key, and use stability to sort by two rules in turn.

In the lesson: Every sorting rule you will ever need comes from one argument, called key. You hand it a function. Python calls that function once for each item and sorts the items by what came back, without changing the items themselves. Notice there are no brackets after len on the first line: you are passing the function, not calling it. Sometimes the function you want has no name, and writing a whole definition for one line feels heavy. That is what lambda is for. The word lambda, then the parameters, then a colon, then one expression, whose value is returned. The two bottom forms on screen are the same function. Use lambda for the tiny throwaway, and a proper definition the moment it needs a name or a second line.

## Files

- [`starter/the-key-argument-and-the-lambda.py`](starter/the-key-argument-and-the-lambda.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-key-argument-and-the-lambda.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m19l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

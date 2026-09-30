# m09l02-04 · Counting from the right end

**Lesson:** [String Indices](https://learnsome.tech/learn/python-course/m09l02) (lesson 9.2, module 9: Objects And Methods) · Pro  
**Check:** Read along

## Goal

You can pick any character out of a string by index, count either from the front starting at zero or from the right end starting at minus one, and say why an index equal to the length raises IndexError.

In the lesson: Sometimes you are interested in the last few characters of a string and you would rather not do arithmetic with the length to reach them. Python makes that easy. You can index from the right end of the string instead. Since positive integers are used to index from the front, negative integers are used to index from the right end. Minus one is the last character, minus two the one before it, and so on. So the fuller table of indices for the word computer gives two alternatives for every character: the count from the left starting at zero, and the count from the right starting at minus one. Notice the asymmetry, because it is the thing people get wrong. Forward numbering starts at zero; backward numbering starts at minus one, since minus zero and zero would be the same number.

## Files

- [`starter/counting-from-the-right-end.txt`](starter/counting-from-the-right-end.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/counting-from-the-right-end.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m09l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

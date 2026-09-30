# m09l02-03 · The last index is the length minus one

**Lesson:** [String Indices](https://learnsome.tech/learn/python-course/m09l02) (lesson 9.2, module 9: Objects And Methods) · Pro  
**Check:** Read along

## Goal

You can pick any character out of a string by index, count either from the front starting at zero or from the right end starting at minus one, and say why an index equal to the length raises IndexError.

In the lesson: A common error is to think the last index will be the same as the length of the string, but as you just saw, that leads to an execution error. So ask yourself: if the length of some string is five, what is the index of its last character? And what if the length is thirty-five? Hopefully you did not count by ones all the way up from zero. The indices for a string of length n are the elements of the sequence range n, which goes from zero through n minus one. So the answers are four and thirty-four. That relationship, last index is length minus one, is worth fixing in your memory now, because it turns up in every loop over a string you will ever write.

## Files

- [`starter/the-last-index-is-the-length-minus-one.txt`](starter/the-last-index-is-the-length-minus-one.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-last-index-is-the-length-minus-one.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m09l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

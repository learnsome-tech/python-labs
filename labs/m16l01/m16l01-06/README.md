# m16l01-06 · Thinking your way through a type error

**Lesson:** [Reading Error Messages](https://learnsome.tech/learn/python-course/m16l01) (lesson 16.1, module 16: Reading Errors, And Platform Notes) · Pro  
**Check:** Read along

## Goal

You can tell a syntax error from a run time error, read a traceback from the bottom up, and follow the chain of calls above the failing line to your own code.

In the lesson: Think about that bottom line. It is a type error, so look for the types it names. There is an integer: clearly the ten. There is something about a string, and the other data is x. The prompt asks for a number, but what type does the input function return? Always a string. So look at the expression again: a string, a plus sign, and a number. A plus sign after a string means concatenation, not numeric addition, and as the message says, you can only concatenate a string onto a string. Notice also that the message suggests a repair you do not want, namely making the ten a string. When something does not make sense, the interpreter does not know what you meant.

## Files

- [`starter/thinking-your-way-through-a-type-error.txt`](starter/thinking-your-way-through-a-type-error.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/thinking-your-way-through-a-type-error.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m16l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m16l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

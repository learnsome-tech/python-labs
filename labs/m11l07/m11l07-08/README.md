# m11l07-08 · Only strings go in and out

**Lesson:** [Entry Objects](https://learnsome.tech/learn/python-course/m11l07) (lesson 11.7, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can put an Entry box in a graphics window with its own label, use a mouse click as the signal that typing has finished, and read or set its contents with getText and setText, converting to numbers where you need them.

In the lesson: Three lines worth memorising. An Entry gives you a string and takes a string, whatever the user has in mind. So call setText with the string zero to start the box off, call getText to read whatever is there, and call int to convert before you calculate. The same is true of the input function, which is why this should feel familiar. And the same warning applies: if what the user typed is not a whole number, the conversion fails with a ValueError rather than handing you a wrong answer, which is at least honest.

## Files

- [`starter/only-strings-go-in-and-out.py`](starter/only-strings-go-in-and-out.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/only-strings-go-in-and-out.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l07-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

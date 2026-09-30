# m20l01-03 · What actually happens when you call the class

**Lesson:** [Classes And Instances](https://learnsome.tech/learn/python-course/m20l01) (lesson 20.1, module 20: Object Oriented Python) · Pro  
**Check:** Read along

## Goal

You can write a class with an initialiser, create instances of it, store data on each instance, and explain the difference between the class and an instance of it.

In the lesson: It is worth being slow about this line, because everything else depends on it. The class name followed by parentheses is a call. Python creates a new empty object of that class, then calls dunder init with that object as the first argument and your arguments after it, then gives you the object back as the value of the whole call. So the initialiser never returns the object; it only fills it in. That is why you write no return statement there, and why the parameter list has one more name in it than the number of arguments you pass. Self is filled in for you. A name like fido then refers to the finished instance, and you use it with the dot notation you already know.

## Files

- [`starter/what-actually-happens-when-you-call-the-clas.py`](starter/what-actually-happens-when-you-call-the-clas.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/what-actually-happens-when-you-call-the-clas.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m20l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

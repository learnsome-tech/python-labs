# m20l02-01 · A method is a function in the class body

**Lesson:** [Methods, Attributes And self](https://learnsome.tech/learn/python-course/m20l02) (lesson 20.2, module 20: Object Oriented Python) · Pro  
**Check:** Read along

## Goal

You can write methods that use self, tell instance attributes from class attributes, avoid the shared mutable class attribute trap, document a method, and expose a computed value as a property.

In the lesson: A method is nothing more exotic than a function defined inside a class body. You write it with def, indented under the class, and it takes one extra parameter at the front. That parameter is the instance the method was called on, and the universal convention is to name it self. Python fills it in for you: when you write the instance, a dot, the method name and parentheses, the object in front of the dot becomes self inside the method. This is the same object dot method syntax you have been using on strings and lists since we met them. The only new thing is that you are now on the other side of it, writing the method rather than calling somebody else's.

## Files

- [`starter/a-method-is-a-function-in-the-class-body.py`](starter/a-method-is-a-function-in-the-class-body.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/a-method-is-a-function-in-the-class-body.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m20l02-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

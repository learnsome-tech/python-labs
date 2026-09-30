# m20l03-01 · Reuse, and then specialise

**Lesson:** [Inheritance And Composition](https://learnsome.tech/learn/python-course/m20l03) (lesson 20.3, module 20: Object Oriented Python) · Pro  
**Check:** Read along

## Goal

You can write a subclass that overrides a method and calls super, test types with isinstance, build the same design out of composition instead, and choose between the two on purpose.

In the lesson: Two classes often share most of their behaviour and differ in a detail. Inheritance is the language feature for that: you name a base class in parentheses after your new class name, and the new class starts out with everything the base has. Then you redefine only the parts that differ. The new class is called a subclass, or a derived class; the one it came from is the base class. The single test for whether inheritance is the right tool is whether a sentence of the form a subclass is a kind of a base class is honestly true. A dog is a kind of animal, so that is fine. Keep that sentence in mind, because in a few minutes we will meet a case where it is false and the code still runs.

## Files

- [`starter/reuse-and-then-specialise.py`](starter/reuse-and-then-specialise.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/reuse-and-then-specialise.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m20l03-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

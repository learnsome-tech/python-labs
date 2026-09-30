# m20l03-05 · Composition: has-a, not is-a

**Lesson:** [Inheritance And Composition](https://learnsome.tech/learn/python-course/m20l03) (lesson 20.3, module 20: Object Oriented Python) · Pro  
**Check:** Read along

## Goal

You can write a subclass that overrides a method and calls super, test types with isinstance, build the same design out of composition instead, and choose between the two on purpose.

In the lesson: The alternative is composition, and it is so plain that people overlook it: one object holds another in an attribute and asks it to do the work. The choice is a question about English. Is my thing a kind of that thing, or does my thing merely have one of those? A manager is a kind of employee, so inherit. A car has an engine; a car is certainly not a kind of engine, so hold one. Inheritance also costs more than it looks: a subclass can reach into everything its base does, so the two are welded together, and a change to the base can break the subclass. A composed object talks to the object it holds through that object's public methods, which is a far thinner join.

## Files

- [`starter/composition-has-a-not-is-a.py`](starter/composition-has-a-not-is-a.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/composition-has-a-not-is-a.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m20l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

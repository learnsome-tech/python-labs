# m14l04-07 · Comparisons bind tighter than or

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: The problem is that there are two binary operations in that condition: the comparison, and or. Comparison operations all have higher precedence than the logical operations or, and, and not. So the condition groups the way the parentheses show here. First the comparison of the answer with the letter y, and then an or whose right operand is the constant string yes. Other languages have the advantage of stopping with an error at such an expression, since a string is not of type bool. Python accepts it, and treats the nonempty string as True, so the whole condition is always True.

## Files

- [`starter/comparisons-bind-tighter-than-or.txt`](starter/comparisons-bind-tighter-than-or.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/comparisons-bind-tighter-than-or.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l04-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

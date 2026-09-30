# m22l01-03 · What a test file looks like

**Lesson:** [Testing With pytest](https://learnsome.tech/learn/python-course/m22l01) (lesson 22.1, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can write a test file of plain assert statements, run it with pytest, read a failure report, and say which cases are worth a test of their own.

In the lesson: A test file is an ordinary Python file whose name begins with test underscore. Inside it, each test is an ordinary function whose name also begins with test underscore, and whose body is a plain assert statement: the word assert followed by something that should be true. There is no framework to learn and no class to inherit from. The first test pins down the ordinary case. The second is an edge case, nothing off, because zero and empty and one are where bugs live. The third tests the failure itself: pytest raises, used with a with statement, passes only when the code inside it raises that error, and fails if the function quietly accepts a nonsense percentage. The name is the sentence you would say out loud.

## Files

- [`starter/test_pricing.py`](starter/test_pricing.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/test_pricing.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: a plain assert statement
   - Lines 8–11: an edge case
   - Lines 12–16: the failure itself
3. Notes from the lesson:
   - Line 6: the name says what should be true, and appears in reports
   - Line 15: pytest.raises passes only if that error is raised inside

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

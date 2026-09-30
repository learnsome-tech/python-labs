# m22l01 · Testing With pytest

Module 22: Testing, Typing And Shipping · lesson 22.1 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m22l01)

**Goal:** You can write a test file of plain assert statements, run it with pytest, read a failure report, and say which cases are worth a test of their own.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m22l01-02](m22l01-02/) | The function we are going to test | Graded |
| [m22l01-03](m22l01-03/) | What a test file looks like | Read along |
| [m22l01-04](m22l01-04/) | Arrange, act, assert | Read along |
| [m22l01-05](m22l01-05/) | Running them: pytest -q | Read along |
| [m22l01-06](m22l01-06/) | A real failure, and what it tells you | Read along |
| [m22l01-08](m22l01-08/) | How pytest finds your tests | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Tests for a function you already wrote

1. Pick a function you wrote earlier in this course that returns a value.
2. Write test_yourname.py with one test for the ordinary case.
3. Add a test for an edge case and one for an input that should be refused.
4. Break the function on purpose, run pytest, and read the failure it prints.

> **Hint:** If the function only prints and returns nothing, change it to return the string first. That is exactly why returning beats printing.

## Check yourself

- What two naming rules does pytest use to find your tests?
- What are the three parts of every test, and what belongs in each?
- How do you test that a function raises an error for bad input?
- In a failure report, what do the lines beginning with capital E tell you?
- Why is a test you have never seen fail not yet worth much?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

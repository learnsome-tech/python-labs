# m17l02 · Raising, And Writing Your Own Exception

Module 17: Errors, Exceptions And Debugging · lesson 17.2 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m17l02)

**Goal:** You can raise a built-in exception with a useful message to refuse bad input, re-raise after logging, chain one exception to another, and define a small exception class of your own when the situation calls for it.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m17l02-02](m17l02-02/) | raise, with a built-in exception and a message | Graded |
| [m17l02-03](m17l02-03/) | Choosing which built-in exception to raise | Read along |
| [m17l02-04](m17l02-04/) | Validating an argument, and the caller catching it | Graded |
| [m17l02-05](m17l02-05/) | Re-raising: handle a little, then get out of the way | Graded |
| [m17l02-06](m17l02-06/) | raise from: this failure because of that one | Graded |
| [m17l02-07](m17l02-07/) | Your own exception class, in two lines | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Exercise: refuse the impossible

1. Write a function average(numbers) that raises ValueError for an empty list.
2. Give the exception a message that says which function refused and why.
3. Call it twice from a try statement: once with three numbers, once with none.
4. Then replace ValueError with an exception class of your own called EmptyDataError.

> **Hint:** Guard first, return second. Your class needs only the word pass in its body.

## Check yourself

- Why is raising better than returning None when a function is given a bad argument?
- When would you raise TypeError rather than ValueError?
- What does the word raise, written on its own inside a handler, do?
- What does raise from add to the traceback that a plain raise does not?
- Give one situation where a custom exception class is worth writing, and one where it is not.

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

# m13l05 · Compound Boolean Expressions

Module 13: Flow Of Control · lesson 13.5 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m13l05)

**Goal:** You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m13l05-01](m13l05-01/) | Two conditions joined with and | Read along |
| [m13l05-02](m13l05-02/) | A short program that uses it | Graded |
| [m13l05-03](m13l05-03/) | Two tests, one identical block | Read along |
| [m13l05-04](m13l05-04/) | Joining conditions with or | Read along |
| [m13l05-05](m13l05-05/) | not, and who binds tighter than whom | Read along |
| [m13l05-06](m13l05-06/) | Short circuit: the second part may never run | Graded |
| [m13l05-07](m13l05-07/) | A test worth wrapping in a function | Read along |
| [m13l05-08](m13l05-08/) | Chained comparisons, and why one is not enough | Graded |
| [m13l05-09](m13l05-09/) | Do not use if else to produce True or False | Read along |
| [m13l05-10](m13l05-10/) | Building the whole test from smaller ones | Read along |
| [m13l05-11](m13l05-11/) | chooseButton one dot py: the Boolean functions | Read along |
| [m13l05-12](m13l05-12/) | Which button was clicked? | Read along |
| [m13l05-13](m13l05-13/) | Two ways to wrap a long condition | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Congress Exercise

1. Write congress.py: read an age and a length of citizenship from the user.
2. A Senator must be at least 30 years old and a citizen for at least 9 years.
3. A Representative must be at least 25 and a citizen for at least 7 years.
4. Print exactly one of: eligible for both, eligible only for the House, ineligible.

> **Hint:** Two requirements each, so each test needs an and. Then a chain to pick one message.

## Check yourself

- When is a compound condition joined by and true, and when is one joined by or false?
- Why does Python not raise an error for x not equal to zero and ten floor divide x greater than one, when x is zero?
- Why is the chained test end one less than or equal to val less than or equal to end two not enough for a rectangle corner?
- What is wrong with writing if condition return True else return False?
- Give the two ways of continuing a long condition onto a second line.

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

# m13l03 · If Elif Chains

Module 13: Flow Of Control · lesson 13.3 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m13l03)

**Goal:** You can write an if elif else chain to sort a value into any number of cases, and explain why only the first true test matters.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m13l03-02](m13l03-02/) | Nesting an if inside every else | Read along |
| [m13l03-03](m13l03-03/) | The same function with elif | Read along |
| [m13l03-04](m13l03-04/) | How a chain is read, and the rule that matters | Read along |
| [m13l03-05](m13l03-05/) | grade one dot py, run for real | Graded |
| [m13l03-06](m13l03-06/) | A chain with no else at all | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Sign Exercise

1. Write a program sign.py that asks the user for a number.
2. Print which category the number is in: 'positive', 'negative' or 'zero'.
3. Three cases, so you need an if, an elif and an else.

### Grade Exercise

1. In Idle, load grade1.py and save it as grade2.py.
2. Rewrite letterGrade so it tests in the opposite order: first F, then D, C, and so on.
3. How many tests do you need to tell five cases apart?
4. Run it and test every path, especially around the cut-off points.

> **Hint:** What should a grade of 79.6 give? What about exactly 80?

### Wages Exercise

1. Modify wages.py or wages1.py to make wages2.py, paying double time for hours over 60.
2. So at most 20 hours of overtime are paid at 1.5 times the normal rate.
3. 65 hours at $10: 10*40 + 1.5*10*20 + 2*10*5, which is $800.
4. Test all paths: changing working code can break cases that worked before.

> **Hint:** You may find wages1.py easier to adapt than wages.py.

## Check yourself

- Why does an elif chain avoid the runaway indentation of nested if else statements?
- In a chain of four tests, which block runs when the second and the fourth are both true?
- What is the difference between a chain that ends with else and one that does not?
- Why can the test for a B be written as at least eighty, with no upper bound?
- What is the spelling trap in the keyword elif?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

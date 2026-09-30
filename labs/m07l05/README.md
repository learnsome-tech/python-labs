# m07l05 · Accumulation Loops

Module 7: Dictionaries And Loops · lesson 7.5 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m07l05)

**Goal:** You can build a loop that accumulates a result, choose the right initial value for the accumulator, and recognise from an English description when a loop through a sequence is needed.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m07l05-01](m07l05-01/) | Adding up a list: begin with the heading | Read along |
| [m07l05-02](m07l05-02/) | Finding the pattern in the arithmetic | Read along |
| [m07l05-03](m07l05-03/) | One pass of work, and the handover | Read along |
| [m07l05-04](m07l05-04/) | Two steps combined into one | Read along |
| [m07l05-05](m07l05-05/) | The whole function, and a test call | Graded |
| [m07l05-06](m07l05-06/) | The accumulation pattern, and its initial value | Read along |
| [m07l05-09](m07l05-09/) | A stub with its example in the docstring | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Test sumList Exercise

1. Write a program testSumList.py containing a main function that tests sumList several times.
2. Include a test for the extreme case: a call with an empty list.

> **Hint:** Decide what the sum of an empty list ought to be before you run it, then check the function agrees.

### Join All Exercise

1. Complete joinStrings in joinAllStub.py and save your version under the new name joinAll.py.
2. Return the joined string from the function; do not print it inside the function.
3. Run main to check all three test calls, including the list of digit strings.

> **Hint:** This is a form of accumulation, but not of numbers. Starting with nothing accumulated does not mean zero here: think what nothing means for a string.

## Check yourself

- Why does writing out a concrete case by hand help you find the loop pattern?
- What does the extra step of starting from a sum of zero buy you?
- Why can the statement sum is assigned sum plus num replace the two line version?
- How do you decide the initial value of an accumulator?
- What goes wrong if the return statement is indented inside the loop body?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

# m09l03 · String Slices

Module 9: Objects And Methods · lesson 9.3 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m09l03)

**Goal:** You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m09l03-01](m09l03-01/) | Slices take a run of characters | Read along |
| [m09l03-02](m09l03-02/) | The first slices | Graded |
| [m09l03-03](m09l03-03/) | Leaving a bound out | Graded |
| [m09l03-04](m09l03-04/) | Slicing the word program | Graded |
| [m09l03-05](m09l03-05/) | Slices are forgiving about the end | Graded |
| [m09l03-06](m09l03-06/) | The find method | Read along |
| [m09l03-07](m09l03-07/) | Finding inside Mississippi | Graded |
| [m09l03-08](m09l03-08/) | Predicting find on a short line | Graded |
| [m09l03-09](m09l03-09/) | Reading the documentation from the shell | Read along |
| [m09l03-10](m09l03-10/) | Lists index and slice the same way | Graded |
| [m09l03-12](m09l03-12/) | The example program index1.py | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice with slices and find

1. Using the variable word from earlier, enter one slice expression that produces 'gra'.
2. Cover the comment rulers, predict every find answer in this module, then check each one.
3. Write a slice of 'computer' giving its last three characters without calling len.

> **Hint:** Negative bounds save you the arithmetic when you are working from the right end.

## Check yourself

- Why does the slice from two to five give three characters rather than four?
- What do you get from a slice with both bounds omitted, and why is that useful for lists?
- Why does a slice past the end of a string succeed where a single index fails?
- What does find return when the substring is not present, and why that value?
- Which expression gives every valid index of the string s to a for loop?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

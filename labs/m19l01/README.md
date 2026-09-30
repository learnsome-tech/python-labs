# m19l01 · Lists, Tuples, Sets, Dicts: Choosing One

Module 19: Data Structures In Depth · lesson 19.1 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m19l01)

**Goal:** You can choose between a list, a tuple, a set and a dictionary for a given job, say what each costs to search, and explain why a tuple can be a dictionary key when a list cannot.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m19l01-01](m19l01-01/) | Four collections, side by side | Read along |
| [m19l01-02](m19l01-02/) | Making all four, and reaching in | Graded |
| [m19l01-03](m19l01-03/) | Which of them will change under you | Graded |
| [m19l01-05](m19l01-05/) | What searching costs | Graded |
| [m19l01-06](m19l01-06/) | Why a tuple can be a key and a list cannot | Graded |
| [m19l01-07](m19l01-07/) | Nesting them inside each other | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Choose the container

1. Read jungle.txt and report how many distinct words it contains, ignoring case.
2. Then report how many times each of the five commonest words appears.
3. Use a set for the first answer and a dictionary for the second.
4. Write down, in a comment, why a list would be the wrong choice for either.

> **Hint:** The string method split gives you a list of words, and lower gives you one case.

## Check yourself

- What are the four questions that choose a container, and how do a list and a tuple differ?
- Why does a set print in an order you did not type, and what should you never do with that order?
- Why can a tuple be a dictionary key when a list cannot?
- What does asking whether a value is in a long list cost, compared with a set?
- You want to look data up by name rather than position. Which container, and why not a list?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

# m19l04 · Iterators And Generators

Module 19: Data Structures In Depth · lesson 19.4 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m19l04)

**Goal:** You can explain what a for loop does in terms of iter and next, write a generator function with yield, and say why a generator costs no memory however long its sequence is.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m19l04-01](m19l04-01/) | Iteration is an agreement, not a type | Read along |
| [m19l04-02](m19l04-02/) | Driving the protocol by hand | Graded |
| [m19l04-03](m19l04-03/) | What a for loop really does | Graded |
| [m19l04-04](m19l04-04/) | Writing a generator with yield | Graded |
| [m19l04-05](m19l04-05/) | Why it uses no memory | Graded |
| [m19l04-06](m19l04-06/) | Things that were lazy all along | Graded |
| [m19l04-07](m19l04-07/) | An iterator is good for one pass | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### A generator over a file

1. Write a generator function words that opens jungle.txt and yields one lower case word at a time.
2. Use it with the sum function to count the words, without ever building a list.
3. Use it again with max and a key to find the longest word.
4. Explain in a comment why the second use needs a second call to words.

> **Hint:** Loop over the file's lines, split each one, and yield inside the inner loop.

## Check yourself

- What two functions make up the iteration protocol, and how is the end of a sequence signalled?
- Write out in words what a for loop does underneath.
- What does yield do that return does not, and what does calling a generator function actually run?
- Why is a generator's memory the same whether it produces ten values or ten million?
- Why does collecting the same generator into a list twice give an empty list the second time?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

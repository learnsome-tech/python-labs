# Exercises — Iterators And Generators

Lesson `m19l04` · [Watch](https://learnsome.tech/courses/python-course/watch?lesson=m19l04)

## Exercise 1: A generator over a file

1. Write a generator function words that opens jungle.txt and yields one lower case word at a time.
2. Use it with the sum function to count the words, without ever building a list.
3. Use it again with max and a key to find the longest word.
4. Explain in a comment why the second use needs a second call to words.

> **Hint**: Loop over the file's lines, split each one, and yield inside the inner loop.


---

© LearnSome.tech · support@iwantto.learnsome.tech

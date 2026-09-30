# m09l04 · Split And Join

Module 9: Objects And Methods · lesson 9.4 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m09l04)

**Goal:** You can cut a string into a list of parts with split, with or without a separator, glue a sequence of strings back together with join, and use the pair in sequence to rewrite a phrase.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m09l04-01](m09l04-01/) | Split cuts a string into a list | Read along |
| [m09l04-02](m09l04-02/) | Splitting a sentence and a word | Graded |
| [m09l04-03](m09l04-03/) | Predicting split with different separators | Graded |
| [m09l04-04](m09l04-04/) | Join is roughly the reverse of split | Read along |
| [m09l04-05](m09l04-05/) | Joining with four different separators | Graded |
| [m09l04-08](m09l04-08/) | Further exploration of string methods | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Underscore Exercise

1. Write a program underscores.py that inputs a phrase from the user.
2. Print the phrase with the white space between words replaced by an underscore.
3. For the input the best one it should print the best one joined by underscores.
4. The conversion can be done in one or two statements using the recent string methods.

> **Hint:** Both methods from this section are involved, in the order the section introduced them.

### Acronym Exercise

1. Write acronym.py: the user inputs a phrase and the program prints its acronym.
2. SADD is the acronym of students against drunk driving; capitals even if the input is not.
3. Plan first: input, convert to upper case, divide into words, start an empty list letters.
4. Get each word's first letter, append it to letters, join the letters, print the acronym.

> **Hint:** Which of those steps sits inside a loop, and what for statement controls that loop?

## Check yourself

- Why does splitting Mississippi on the letter i give an empty string as its last element?
- What is the difference between splitting with no argument and splitting on a single blank?
- Which object do you call join on, and what goes inside the parentheses?
- Why does splitting and then joining with one blank not always give the original string back?
- How would you turn a list of single letters into one word with no gaps?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

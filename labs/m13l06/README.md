# m13l06 · More String Methods

Module 13: Flow Of Control · lesson 13.6 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m13l06)

**Goal:** You can test what a string starts with, ends with or is made of, and build up conditions from string methods such as startswith, endswith, replace and isdigit.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m13l06-01](m13l06-01/) | Methods that answer yes or no about a string | Read along |
| [m13l06-02](m13l06-02/) | startswith and endswith | Graded |
| [m13l06-03](m13l06-03/) | replace, with a count of how many | Read along |
| [m13l06-04](m13l06-04/) | What replace actually returns | Graded |
| [m13l06-05](m13l06-05/) | isdigit, and two old friends | Graded |
| [m13l06-06](m13l06-06/) | Putting them into conditions | Read along |
| [m13l06-07](m13l06-07/) | The function to complete | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Article Start Exercise

1. Complete startsWithArticle(title), then write a program that tests it.
2. Return True if the first word of title is The, A or An.
3. Careful: a title beginning There does not begin with an article.
4. Test titles that start with each article, and awkward ones like A and Anthem.

> **Hint:** What exactly should you be testing for, if the bare word is not enough?

### Is Number String Exercise

1. Save isNumberStringStub.py as isNumberString.py and complete both functions.
2. isIntStr(s): True when s is digits, possibly after a minus sign.
3. isDecimalStr(s): as above, but a decimal point is allowed, though not required.
4. Test that bad strings return False, not only that good ones return True.

> **Hint:** isdigit is not enough on its own. Slicing, count and the methods here all help.

## Check yourself

- Which of the string methods in this section return a Boolean, and which returns a string?
- Why does isdigit answer False for a string holding a minus sign and three digits?
- What does replace do when the piece you asked it to find is not there?
- How would you test that a string is a negative whole number?
- Why is a title beginning with the word There a problem for the article test?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

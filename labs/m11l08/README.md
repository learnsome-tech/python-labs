# m11l08 · Colours, Custom And Random

Module 11: Graphics · lesson 11.8 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m11l08)

**Goal:** You can use the many built-in colour names, build a colour of your own from red, green and blue intensities with color_rgb, and choose random values from a range with the random module's randrange function.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m11l08-02](m11l08-02/) | Custom colours: red, green and blue | Read along |
| [m11l08-03](m11l08-03/) | randomCircles: a colour at random | Read along |
| [m11l08-04](m11l08-04/) | A random size and a random place | Read along |
| [m11l08-05](m11l08-05/) | range, and choosing from a range | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Ranges Exercise

1. Write ranges.py in three parts, testing after each. Not a graphics program.
2. Part one: use range and a for loop to print 1, 2, 3, 4, one number per line.
3. Part two: read an integer n, then print 1, 2, 3, ... , n, including n.
4. Part three: use a simple repeat loop to print five random numbers from 1 to n.

> **Hint:** Label each sequence, as in Numbers 1-4 or Numbers 1-n. It should be possible for n itself to be printed.

### Text Triangle Exercise

1. Write texttriangle.py. Prompt for a small positive integer n. Not a graphics program.
2. Print a triangle of '#' whose last row has n of them: #, ##, ###, #### when n is 4.
3. Leave a blank line, then print the same triangle starting from the longest row.

> **Hint:** A row of '#' is easiest with the string multiplication operator *. A negative step in range helps the second half.

## Check yourself

- How do you ask for a darker version of a built-in colour name?
- What do the three arguments to color_rgb mean, and what values may they take?
- How does randrange differ from range, given the same arguments?
- What is the largest value random.randrange(5, 295) can return?
- Why does the program choose a radius from 3 upwards rather than from 0?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

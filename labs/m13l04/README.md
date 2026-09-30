# m13l04 · Nesting Control Flow Statements

Module 13: Flow Of Control · lesson 13.4 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m13l04)

**Goal:** You can nest if statements inside loops and loops inside if statements, and read the indentation to see which block belongs to which heading.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m13l04-01](m13l04-01/) | An if inside a for loop | Read along |
| [m13l04-02](m13l04-02/) | onlyPositive dot py | Graded |
| [m13l04-03](m13l04-03/) | A bouncing ball needs a test every step | Read along |
| [m13l04-04](m13l04-04/) | Four tests, one for each wall | Read along |
| [m13l04-05](m13l04-05/) | bounceInBox: an if inside a for loop | Read along |
| [m13l04-06](m13l04-06/) | Choosing a random starting point | Read along |
| [m13l04-07](m13l04-07/) | bounceBall sets the scene | Read along |
| [m13l04-08](m13l04-08/) | and then hands over to the animation | Read along |
| [m13l04-09](m13l04-09/) | Nesting in every direction | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Short String Exercise

1. Write short.py with a function printShort(strings).
2. Given a list of strings, it prints the ones with at most three characters.
3. In your main program, test it by calling it with several different lists.
4. Give printShort a docstring saying in one line what it prints.

> **Hint:** Find the length of each string with the len function.

### Even Print Exercise

1. Write even1.py with a function printEven(nums).
2. Given a list of integers, it prints the even ones.
3. Test it from your main program with several different lists.

> **Hint:** A number is even if its remainder, when divided by 2, is 0.

### Even List Exercise

1. Write even2.py with a function chooseEven(nums).
2. Given a list of integers, it returns a new list containing only the even ones.
3. Print the results in your main program, not inside the function.

> **Hint:** Create a new list in the function and append the numbers you want before returning it.

### Unique List Exercise

1. Copy madlib2.py to madlib2a.py and add a function uniqueList(aList).
2. It returns a new list with the first occurrence of each value, in their original order.
3. Then change the last line of getKeys so it uses uniqueList instead of forming a set.
4. Check that madlib2a.py prompts for cues in the order they first appear.

> **Hint:** Process aList in order, and use in to append only values that are not already there.

## Check yourself

- In onlyPositive, how many times does the test run for a list of six numbers?
- Why is the vertical test in bounceInBox a plain if rather than an elif?
- What would change if the print in onlyPositive were indented under the for instead of the if?
- Why does the bounce bound sit a radius in from the edge of the window?
- How do you decide, reading unfamiliar code, which heading owns a given line?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

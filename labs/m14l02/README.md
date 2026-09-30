# m14l02 · Interactive While Loops

Module 14: While Loops · lesson 14.2 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m14l02)

**Goal:** You can write a while loop that reads input until a sentinel value arrives, initialising the test data before the loop and resetting it at the end of the body so the loop can stop.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m14l02-02](m14l02-02/) | readLines0.py, ask for a count first | Graded |
| [m14l02-03](m14l02-03/) | readLines1.py, ask before every line | Graded |
| [m14l02-04](m14l02-04/) | Set up the test data twice | Read along |
| [m14l02-05](m14l02-05/) | A sentinel says when the data ends | Read along |
| [m14l02-06](m14l02-06/) | readLines2.py, an empty line to quit | Graded |
| [m14l02-07](m14l02-07/) | Comment out one line and it never stops | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Interactive Sum Exercise

1. Write sumAll.py: prompt for numbers, one per line, ending with a line containing only 0.
2. Keep a running sum as you read, and print the sum only after all numbers are entered.
3. Do not create a list: use each number for the sum as soon as you have read it.

> **Hint:** The sentinel here is a number, so convert the input before the test, and remember both places.

### Safe Number Input Exercise

1. Save safeNumberInputStub.py as safeNumberInput.py and complete the three functions in it.
2. safeWholeNumber: keep prompting until the string entered is a legal whole number.
3. safeInt: the same shape, using the function isIntStr from the previous exercise.
4. safeDecimal: the same again, using the function isDecimalStr.

> **Hint:** Test the string before converting it, and loop back for another try while it is still illegal.

### Savings Exercise

1. Write savings.py, prompting for an initial balance, an interest rate as a decimal, and a target.
2. Print every amount rounded to exactly two decimal places, starting with the initial balance.
3. Each year multiply the balance by one plus the rate; stop at or past the target.
4. For 500, .04 and 550 the program prints 500.00, 520.00, 540.80, 562.43.

> **Hint:** The number of years is unknown in advance, which is your signal to reach for a while loop.

### Strange Sequence Exercise

1. Recall jump: jump(n) is n//2 when n is even and 3*n+1 when n is odd, so jump(3) is 10.
2. Save jumpSeqStub.py as jumpSeq.py and complete printJumps and listJumps, stopping at 1.
3. Save that as jumpSeqLengths.py and print just the length of the sequence for an entered n.
4. Then prompt for a lowest and a highest start and report the length for every n in between.

> **Hint:** Each new value is computed from the most recent one, so the loop variable is the number itself.

## Check yourself

- Why does a repeat loop not suit input whose length the user does not know?
- What is a sentinel, and why is an empty line a convenient one?
- Why must the variable tested in the heading be set in two places?
- What is the difference between a termination condition and a continuation condition?
- What happens if you comment out the last line of the body of readLines2, and how do you stop it?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

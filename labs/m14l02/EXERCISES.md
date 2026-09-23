# Exercises — Interactive While Loops

Lesson `m14l02` · [Watch](https://learnsome.tech/courses/python-course/watch?lesson=m14l02)

## Exercise 1: Interactive Sum Exercise

1. Write sumAll.py: prompt for numbers, one per line, ending with a line containing only 0.
2. Keep a running sum as you read, and print the sum only after all numbers are entered.
3. Do not create a list: use each number for the sum as soon as you have read it.

> **Hint**: The sentinel here is a number, so convert the input before the test, and remember both places.


## Exercise 2: Safe Number Input Exercise

1. Save safeNumberInputStub.py as safeNumberInput.py and complete the three functions in it.
2. safeWholeNumber: keep prompting until the string entered is a legal whole number.
3. safeInt: the same shape, using the function isIntStr from the previous exercise.
4. safeDecimal: the same again, using the function isDecimalStr.

> **Hint**: Test the string before converting it, and loop back for another try while it is still illegal.


## Exercise 3: Savings Exercise

1. Write savings.py, prompting for an initial balance, an interest rate as a decimal, and a target.
2. Print every amount rounded to exactly two decimal places, starting with the initial balance.
3. Each year multiply the balance by one plus the rate; stop at or past the target.
4. For 500, .04 and 550 the program prints 500.00, 520.00, 540.80, 562.43.

> **Hint**: The number of years is unknown in advance, which is your signal to reach for a while loop.


## Exercise 4: Strange Sequence Exercise

1. Recall jump: jump(n) is n//2 when n is even and 3*n+1 when n is odd, so jump(3) is 10.
2. Save jumpSeqStub.py as jumpSeq.py and complete printJumps and listJumps, stopping at 1.
3. Save that as jumpSeqLengths.py and print just the length of the sequence for an entered n.
4. Then prompt for a lowest and a highest start and report the length for every n in between.

> **Hint**: Each new value is computed from the most recent one, so the loop variable is the number itself.


---

© LearnSome.tech · support@iwantto.learnsome.tech

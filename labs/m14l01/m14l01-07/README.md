# m14l01-07 · The range function with a step

**Lesson:** [While Loops, And The General Range](https://learnsome.tech/learn/python-course/m14l01) (lesson 14.1, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop whose condition is tested before every pass, spot a loop that will never stop, and use the three argument range function to replace a counting while loop with a for loop.

In the lesson: Enter these lines separately in the shell. The range function takes a third argument, the step size, needed whenever the step from one element to the next is not one. As with the simpler ranges, the values are generated one at a time, as needed, so to see them all at once you convert the sequence to a list before printing. The most general form is range with a start, a value past the end, and a step. The second argument is always past the final element, which is why the next two calls give the same three numbers. The step can also be negative, so counting down works too, and zero is past the end of that descending list. Try it yourself: make a range call that gives the temperatures from the tea example, and you get exactly the three that cool dot py printed.

## Files

- [`starter/shell-the-range-function-with-a-step.py`](starter/shell-the-range-function-with-a-step.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l01/m14l01-07/starter`
2. Read `shell-the-range-function-with-a-step.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   nums = range(4, 9, 2)
   print(list(nums))
   list(range(4, 10, 2))
   list(range(10, 0, -1))
   list(range(115, 112, -1))
   ```
4. Run it: `python3 -i < shell-the-range-function-with-a-step.py`.
5. Check it from the repository root: `./check m14l01-07`.

## Expected output

```text
[4, 6, 8]
[4, 6, 8]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[115, 114, 113]
```

## How to check

`./check m14l01-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-range-function-with-a-step.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

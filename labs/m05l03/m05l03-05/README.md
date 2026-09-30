# m05l03-05 · Three ways to the same sentence

**Lesson:** [The String Format Method](https://learnsome.tech/learn/python-course/m05l03) (lesson 5.3, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can build a string with the format method, substituting values into replacement fields by position, repeating a field, and showing a literal brace.

In the lesson: Back to the interview program, where we want a full stop at the end with no space before it. Using the analogy, we want to fill in three blanks. The format approach extends to multiple substitutions: at each place in the format string where there is a pair of braces, format substitutes the value of the next parameter in the list. The example file interview two dot py does the job three ways. The first line joins everything with plus signs. The second uses the print function with the separator set to nothing. The third uses one format string with three pairs of braces. Run it and check that the results from all three match.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/interview2.py`](starter/interview2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-05/starter`
2. Read `interview2.py` the way the lesson builds it:
   - Lines 1–6: joins everything with plus signs
   - Lines 7: the separator set to nothing
   - Lines 8: one format string
3. Run it: `python3 interview2.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m05l03-05`.

## Expected output

```text
Enter the applicant's name: Enter the interviewer's name: Enter the appointment time: Bob Jones will interview Anna Smith at 2:30 pm.
Bob Jones will interview Anna Smith at 2:30 pm.
Bob Jones will interview Anna Smith at 2:30 pm.
```

## How to check

`./check m05l03-05` copies `starter/` into a scratch directory and runs `python3 interview2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

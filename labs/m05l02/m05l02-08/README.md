# m05l02-08 · A string of digits is not a number

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: Let us see the distinction in the Shell. Two quoted digits joined end to end give a two character string, not a number. For arithmetic we need numeric operands, and we can use type names as functions to convert types, as mentioned in the whirlwind introduction. The int function takes a string of digits and gives back the integer it spells, and now plus adds. The float function does the same for numbers with a decimal point. The last entry is asking for trouble: handing int a string with a point in it raises a value error, because int wants whole digits only. Use float for anything with a fractional part.

## Files

- [`starter/shell-a-string-of-digits-is-not-a-number.py`](starter/shell-a-string-of-digits-is-not-a-number.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-08/starter`
2. Read `shell-a-string-of-digits-is-not-a-number.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   '2' + '3'
   int('2') + int('3')
   float('3.5')
   int('3.5')
   ```
4. Run it: `python3 -i < shell-a-string-of-digits-is-not-a-number.py`.
5. Check it from the repository root: `./check m05l02-08`.

## Expected output

```text
'23'
5
3.5
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '3.5'
```

## How to check

`./check m05l02-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-a-string-of-digits-is-not-a-number.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

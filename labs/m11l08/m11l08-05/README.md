# m11l08-05 · range, and choosing from a range

**Lesson:** [Colours, Custom And Random](https://learnsome.tech/learn/python-course/m11l08) (lesson 11.8, module 11: Graphics) · Pro  
**Check:** Graded

## Goal

You can use the many built-in colour names, build a colour of your own from red, green and blue intensities with color_rgb, and choose random values from a range with the random module's randrange function.

In the lesson: Let us pin down range and randrange in the Shell. You know range already. With one argument it describes all the whole numbers from zero up to, but not including, that argument, so range of two hundred fifty six is exactly the set of possible colour intensities. The random module's randrange takes the same arguments, but instead of describing the whole sequence it selects one element of it at random, which is why the membership test comes back True. With two arguments you give a starting value as well, and you still name a value past the end, so the smallest member is three and the largest is thirty nine.

## Files

- [`starter/shell-range-and-choosing-from-a-range.py`](starter/shell-range-and-choosing-from-a-range.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m11l08/m11l08-05/starter`
2. Read `shell-range-and-choosing-from-a-range.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import random
   range(256)
   random.randrange(256) in range(256)
   range(3, 40)
   min(range(3, 40))
   max(range(3, 40))
   random.randrange(3, 40) in range(3, 40)
   ```
4. Run it: `python3 -i < shell-range-and-choosing-from-a-range.py`.
5. Check it from the repository root: `./check m11l08-05`.

## Expected output

```text
range(0, 256)
True
range(3, 40)
3
39
True
```

## How to check

`./check m11l08-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-range-and-choosing-from-a-range.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l08) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

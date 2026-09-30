# m11l04-05 · Two names, one object

**Lesson:** [Mutable Objects And Aliases](https://learnsome.tech/learn/python-course/m11l04) (lesson 11.4, module 11: Graphics) · Pro  
**Check:** Graded

## Goal

You can explain why assigning one name from another gives two names for a single object, predict when mutating through one name is visible through the other, and use clone or a full slice to get a genuinely separate object.

In the lesson: Before we go back to points, watch the same trap with a list, where no window is needed. Make a list of one, two, three and call it nums. Now say numsAlias is assigned nums. That does not build a second list. It gives the one list a second name. Append four using the name nums, then ask for numsAlias. Four is there. Append five using numsAlias, then ask for nums. Five is there too. One object, two names, and a change made through either name is visible through both. That is what an alias is, and mutable objects are the only place where it can hurt you.

## Files

- [`starter/shell-two-names-one-object.py`](starter/shell-two-names-one-object.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m11l04/m11l04-05/starter`
2. Read `shell-two-names-one-object.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   nums = [1, 2, 3]
   numsAlias = nums
   nums.append(4)
   numsAlias
   numsAlias.append(5)
   nums
   ```
4. Run it: `python3 -i < shell-two-names-one-object.py`.
5. Check it from the repository root: `./check m11l04-05`.

## Expected output

```text
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
```

## How to check

`./check m11l04-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-two-names-one-object.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

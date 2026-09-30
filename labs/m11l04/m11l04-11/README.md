# m11l04-11 · A list, an alias and a clone

**Lesson:** [Mutable Objects And Aliases](https://learnsome.tech/learn/python-course/m11l04) (lesson 11.4, module 11: Graphics) · Pro  
**Check:** Graded

## Goal

You can explain why assigning one name from another gives two names for a single object, predict when mutating through one name is visible through the other, and use clone or a full slice to get a genuinely separate object.

In the lesson: Now the tutorial's own shell exercise, with all three names side by side. Start again with nums as one, two, three. Make numsAlias another name for it. Then make numsClone using the slice notation, with nothing before or after the colon, which copies the list. Append four through nums, and append five through numsAlias. Ask for all three. Nums and numsAlias both show one, two, three, four, five, because they are the same object. NumsClone still shows one, two, three, because it never was. One footnote worth knowing: cloning a list clones the list, not the objects inside it, so a mutable element is still shared with the original.

## Files

- [`starter/shell-a-list-an-alias-and-a-clone.py`](starter/shell-a-list-an-alias-and-a-clone.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m11l04/m11l04-11/starter`
2. Read `shell-a-list-an-alias-and-a-clone.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   nums = [1, 2, 3]
   numsAlias = nums
   numsClone = nums[:]
   nums.append(4)
   numsAlias.append(5)
   nums
   numsAlias
   numsClone
   ```
4. Run it: `python3 -i < shell-a-list-an-alias-and-a-clone.py`.
5. Check it from the repository root: `./check m11l04-11`.

## Expected output

```text
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3]
```

## How to check

`./check m11l04-11` copies `starter/` into a scratch directory and runs `python3 -i < shell-a-list-an-alias-and-a-clone.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

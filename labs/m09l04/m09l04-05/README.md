# m09l04-05 · Joining with four different separators

**Lesson:** [Split And Join](https://learnsome.tech/learn/python-course/m09l04) (lesson 9.4, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can cut a string into a list of parts with split, with or without a separator, glue a sequence of strings back together with join, and use the pair in sequence to rewrite a phrase.

In the lesson: First rebuild the list of words from the previous section, then predict and try each join. With a single blank as the separator we get the sentence back, though not quite the original sentence: the double space was thrown away when we split, and join cannot know about it. With the empty string as the separator the words are jammed together with nothing in between, which is exactly what you want when you are assembling an acronym. Two slashes fill each gap with two slashes, and two hashes with two hashes; a separator can be any length. And the last line joins a list written out on the spot, three words with a colon between them, to make the point that the sequence can be any list of strings.

## Files

- [`starter/shell-joining-with-four-different-separators.py`](starter/shell-joining-with-four-different-separators.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l04/m09l04-05/starter`
2. Read `shell-joining-with-four-different-separators.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   seq = 'Go:  Tear some strings apart!'.split()
   ' '.join(seq)
   ''.join(seq)
   '//'.join(seq)
   '##'.join(seq)
   ':'.join(['one', 'two', 'three'])
   ```
4. Run it: `python3 -i < shell-joining-with-four-different-separators.py`.
5. Check it from the repository root: `./check m09l04-05`.

## Expected output

```text
'Go: Tear some strings apart!'
'Go:Tearsomestringsapart!'
'Go://Tear//some//strings//apart!'
'Go:##Tear##some##strings##apart!'
'one:two:three'
```

## How to check

`./check m09l04-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-joining-with-four-different-separators.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

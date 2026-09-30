# m20l03-04 · isinstance, issubclass and the search order

**Lesson:** [Inheritance And Composition](https://learnsome.tech/learn/python-course/m20l03) (lesson 20.3, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write a subclass that overrides a method and calls super, test types with isinstance, build the same design out of composition instead, and choose between the two on purpose.

In the lesson: Two empty classes, one inheriting the other, are enough to show how types are tested. Make a dog. It is a Dog, of course, and it is also an Animal, because inheritance means it really is one. An unrelated class gives false. Compare that with the line below it: asking whether the type is exactly Animal asks for an exact match and gives false, which is almost never the question you mean. So use isinstance, not a type comparison. Issubclass compares two classes rather than an object and a class. And the last line shows the method resolution order: the list of classes, in the order it searches them, when you ask an object for a method. Dog first, then Animal, then object, which every class inherits from.

## Files

- [`starter/shell-isinstance-issubclass-and-the-search-order.py`](starter/shell-isinstance-issubclass-and-the-search-order.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l03/m20l03-04/starter`
2. Read `shell-isinstance-issubclass-and-the-search-order.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   class Animal: pass
   class Dog(Animal): pass
   d = Dog()
   isinstance(d, Dog)
   isinstance(d, Animal)
   isinstance(d, str)
   type(d) is Animal
   issubclass(Dog, Animal)
   [c.__name__ for c in Dog.__mro__]
   ```
4. Run it: `python3 -i < shell-isinstance-issubclass-and-the-search-order.py`.
5. Check it from the repository root: `./check m20l03-04`.

## Expected output

```text
True
True
False
False
True
['Dog', 'Animal', 'object']
```

## How to check

`./check m20l03-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-isinstance-issubclass-and-the-search-order.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

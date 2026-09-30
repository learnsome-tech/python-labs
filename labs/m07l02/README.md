# m07l02 · Dictionaries And String Formatting

Module 7: Dictionaries And Loops · lesson 7.2 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m07l02)

**Goal:** You can build strings with the format method and a dictionary unpacked by two stars, and use locals or an f-string to drop local variable values straight into a format string.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m07l02-02](m07l02-02/) | Words in braces, and keyword parameters | Graded |
| [m07l02-03](m07l02-03/) | Two stars unpack a dictionary into keywords | Read along |
| [m07l02-04](m07l02-04/) | The main function of spanish3.py | Read along |
| [m07l02-05](m07l02-05/) | The general form, and back to the mad lib | Read along |
| [m07l02-08](m07l02-08/) | arithDict.py formats with locals | Graded |
| [m07l02-09](m07l02-09/) | hello_you4.py, with a dictionary reference | Graded |
| [m07l02-10](m07l02-10/) | F-strings: the same thing, shorter | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Mad Lib Exercise

1. Load madlib.py in the editor and save it under the new name myMadlib.py.
2. Modify it to have a less lame story, with more and different dictionary entries.
3. Make sure addPick is called for each key that appears in your format string.
4. Test your version by running it.

> **Hint:** Every name in braces in the story must be a key that addPick puts in the dictionary.

### Quotient String Dictionary Exercise

1. Copy quotientReturn.py from the earlier exercise and save it as quotientDict.py.
2. Change quotientString to put local variable names inside the braces of a format string.
3. Process the format string with the format method and locals, or make it an f-string.

> **Hint:** If you use meaningful names for the variables, the format string should be particularly easy to understand.

## Check yourself

- What goes inside the braces of a format string when you use keyword parameters?
- What do the two stars in front of a dictionary actually do to the call?
- What does the function call locals return, and what are its keys?
- How would you rewrite a format string with locals as an f-string?
- Why must dictionary keys used this way be legal Python identifiers?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

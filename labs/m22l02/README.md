# m22l02 · Type Hints

Module 22: Testing, Typing And Shipping · lesson 22.2 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m22l02)

**Goal:** You can annotate a function's parameters and return value, write the common types including lists, dictionaries and optional values, explain that hints change nothing at runtime, and check them with mypy.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m22l02-01](m22l02-01/) | Saying out loud what you already assumed | Read along |
| [m22l02-02](m22l02-02/) | Annotating parameters and the return | Graded |
| [m22l02-03](m22l02-03/) | The handful of types you actually need | Graded |
| [m22l02-04](m22l02-04/) | Nothing checks them while the program runs | Graded |
| [m22l02-05](m22l02-05/) | mypy: the tool that does check them | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Annotate something you wrote

1. Take a file of your own with three or four functions and annotate them all.
2. Include one function whose return is a type or None, and one taking a list.
3. Install mypy and run it on the file; fix or explain everything it reports.
4. Then pass a wrong type on purpose and confirm Python still runs it.

> **Hint:** If mypy complains about a value that could be None, the fix is usually an if statement, not a wider hint.

## Check yourself

- How do you annotate a parameter, and how do you annotate what comes back?
- What does a vertical bar between two types mean, and when do you use it with None?
- What happens at runtime if you pass a string where an int was annotated?
- What does mypy do that Python itself does not?
- Name a place where hints clearly pay off and one where they are noise.

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

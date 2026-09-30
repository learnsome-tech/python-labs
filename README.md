<p>
  <a href="https://learnsome.tech/courses/python-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Hands-on Python: Complete Video Course & Book

**From Processor Fundamentals to OOP, Data Structures & Typing**

A complete Python course as IDE-style videos, plus a written companion built from the same scripts. 22 modules, 98 lessons, five to ten minutes each. Beginner level, about 11 hours.

This repository holds the labs of the LearnSome.tech course [Hands-on Python: Complete Video Course & Book](https://learnsome.tech/courses/python-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/python-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7, as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/python-labs.git
  cd python-labs
  ./check m01l03-07
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7. Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l03-07`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 300 |
| Runs, not graded | Runs the program and shows its output; the site gives no pass or fail, and the lab README says why. | 4 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 390 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: Before You Write Code

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [What A Program Really Is](https://learnsome.tech/learn/python-course/m01l01) | [3 labs](labs/m01l01/) | Free |
| 1.2 | [How Python Runs Your Code](https://learnsome.tech/learn/python-course/m01l02) | [2 labs](labs/m01l02/) | Free |
| 1.3 | [What Python Is, And Where It Came From](https://learnsome.tech/learn/python-course/m01l03) | [4 labs](labs/m01l03/) | Free |
| 1.4 | [Editors, IDEs And Shells](https://learnsome.tech/learn/python-course/m01l04) | [3 labs](labs/m01l04/) | Free |

### Module 2: Install Python Properly

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Installing Python On Windows](https://learnsome.tech/learn/python-course/m02l01) | [11 labs](labs/m02l01/) | Pro |
| 2.2 | [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) | [10 labs](labs/m02l02/) | Pro |
| 2.3 | [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) | [10 labs](labs/m02l03/) | Pro |
| 2.4 | [Where Python Lives: PATH And Versions](https://learnsome.tech/learn/python-course/m02l04) | [8 labs](labs/m02l04/) | Pro |
| 2.5 | [First Run, And Fixing A Broken Install](https://learnsome.tech/learn/python-course/m02l05) | [11 labs](labs/m02l05/) | Pro |
| 2.6 | [Your Python Folder And A First Program](https://learnsome.tech/learn/python-course/m02l06) | [3 labs](labs/m02l06/) | Pro |

### Module 3: Meet Idle And The Shell

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [A Sample Program, Explained](https://learnsome.tech/learn/python-course/m03l01) | [5 labs](labs/m03l01/) | Pro |
| 3.2 | [Idle And The Python Shell](https://learnsome.tech/learn/python-course/m03l02) | [1 lab](labs/m03l02/) | Pro |
| 3.3 | [Types And Functions, A Whirlwind Tour](https://learnsome.tech/learn/python-course/m03l03) | [6 labs](labs/m03l03/) | Pro |

### Module 4: Data And Expressions

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [Integer Arithmetic And Precedence](https://learnsome.tech/learn/python-course/m04l01) | [5 labs](labs/m04l01/) | Pro |
| 4.2 | [Division, Quotients And Remainders](https://learnsome.tech/learn/python-course/m04l02) | [5 labs](labs/m04l02/) | Pro |
| 4.3 | [Strings, Delimiters And Concatenation](https://learnsome.tech/learn/python-course/m04l03) | [6 labs](labs/m04l03/) | Pro |
| 4.4 | [Variables And Assignment](https://learnsome.tech/learn/python-course/m04l04) | [8 labs](labs/m04l04/) | Pro |
| 4.5 | [Literals, Identifiers And Keywords](https://learnsome.tech/learn/python-course/m04l05) | [6 labs](labs/m04l05/) | Pro |
| 4.6 | [The Print Function And String Literals](https://learnsome.tech/learn/python-course/m04l06) | [6 labs](labs/m04l06/) | Pro |

### Module 5: Programs, Input, Output

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [The Idle Editor And Running Programs](https://learnsome.tech/learn/python-course/m05l01) | [5 labs](labs/m05l01/) | Pro |
| 5.2 | [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) | [10 labs](labs/m05l02/) | Pro |
| 5.3 | [The String Format Method](https://learnsome.tech/learn/python-course/m05l03) | [10 labs](labs/m05l03/) | Pro |

### Module 6: Functions

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [Defining Your First Function](https://learnsome.tech/learn/python-course/m06l01) | [5 labs](labs/m06l01/) | Pro |
| 6.2 | [Several Functions, And Flow Of Control](https://learnsome.tech/learn/python-course/m06l02) | [6 labs](labs/m06l02/) | Pro |
| 6.3 | [Function Parameters](https://learnsome.tech/learn/python-course/m06l03) | [5 labs](labs/m06l03/) | Pro |
| 6.4 | [Multiple Parameters](https://learnsome.tech/learn/python-course/m06l04) | [3 labs](labs/m06l04/) | Pro |
| 6.5 | [Returning Values](https://learnsome.tech/learn/python-course/m06l05) | [7 labs](labs/m06l05/) | Pro |
| 6.6 | [Local Scope And Global Constants](https://learnsome.tech/learn/python-course/m06l06) | [6 labs](labs/m06l06/) | Pro |

### Module 7: Dictionaries And Loops

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 7.1 | [Dictionaries](https://learnsome.tech/learn/python-course/m07l01) | [6 labs](labs/m07l01/) | Pro |
| 7.2 | [Dictionaries And String Formatting](https://learnsome.tech/learn/python-course/m07l02) | [7 labs](labs/m07l02/) | Pro |
| 7.3 | [Lists, Range And The For Loop](https://learnsome.tech/learn/python-course/m07l03) | [10 labs](labs/m07l03/) | Pro |
| 7.4 | [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) | [11 labs](labs/m07l04/) | Pro |
| 7.5 | [Accumulation Loops](https://learnsome.tech/learn/python-course/m07l05) | [7 labs](labs/m07l05/) | Pro |
| 7.6 | [Playing Computer](https://learnsome.tech/learn/python-course/m07l06) | [7 labs](labs/m07l06/) | Pro |
| 7.7 | [The Print Function Keyword End](https://learnsome.tech/learn/python-course/m07l07) | [7 labs](labs/m07l07/) | Pro |

### Module 8: Numbers In Depth

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 8.1 | [Floats, Division And Mixed Types](https://learnsome.tech/learn/python-course/m08l01) | [7 labs](labs/m08l01/) | Pro |
| 8.2 | [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) | [10 labs](labs/m08l02/) | Pro |
| 8.3 | [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) | [10 labs](labs/m08l03/) | Pro |

### Module 9: Objects And Methods

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 9.1 | [Objects, Methods And String Case](https://learnsome.tech/learn/python-course/m09l01) | [6 labs](labs/m09l01/) | Pro |
| 9.2 | [String Indices](https://learnsome.tech/learn/python-course/m09l02) | [6 labs](labs/m09l02/) | Pro |
| 9.3 | [String Slices](https://learnsome.tech/learn/python-course/m09l03) | [11 labs](labs/m09l03/) | Pro |
| 9.4 | [Split And Join](https://learnsome.tech/learn/python-course/m09l04) | [6 labs](labs/m09l04/) | Pro |
| 9.5 | [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) | [12 labs](labs/m09l05/) | Pro |

### Module 10: Mad Libs Revisited

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 10.1 | [Mad Libs Revisited: Finding The Cues](https://learnsome.tech/learn/python-course/m10l01) | [9 labs](labs/m10l01/) | Pro |
| 10.2 | [Mad Libs Revisited: The Whole Program](https://learnsome.tech/learn/python-course/m10l02) | [6 labs](labs/m10l02/) | Pro |

### Module 11: Graphics

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 11.1 | [A Graphics Introduction](https://learnsome.tech/learn/python-course/m11l01) | [10 labs](labs/m11l01/) | Pro |
| 11.2 | [Sample Graphics Programs](https://learnsome.tech/learn/python-course/m11l02) | [10 labs](labs/m11l02/) | Pro |
| 11.3 | [Reading The graphics.py Documentation](https://learnsome.tech/learn/python-course/m11l03) | [7 labs](labs/m11l03/) | Pro |
| 11.4 | [Mutable Objects And Aliases](https://learnsome.tech/learn/python-course/m11l04) | [7 labs](labs/m11l04/) | Pro |
| 11.5 | [Animation: Moving One Shape](https://learnsome.tech/learn/python-course/m11l05) | [5 labs](labs/m11l05/) | Pro |
| 11.6 | [Animation: Loops, Bouncing, Flushing](https://learnsome.tech/learn/python-course/m11l06) | [8 labs](labs/m11l06/) | Pro |
| 11.7 | [Entry Objects](https://learnsome.tech/learn/python-course/m11l07) | [8 labs](labs/m11l07/) | Pro |
| 11.8 | [Colours, Custom And Random](https://learnsome.tech/learn/python-course/m11l08) | [4 labs](labs/m11l08/) | Pro |

### Module 12: Files And Chapter Review

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 12.1 | [Files: Writing And Reading](https://learnsome.tech/learn/python-course/m12l01) | [6 labs](labs/m12l01/) | Pro |
| 12.2 | [Chapter Two In One Sitting](https://learnsome.tech/learn/python-course/m12l02) | [9 labs](labs/m12l02/) | Pro |

### Module 13: Flow Of Control

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 13.1 | [Conditions And Simple If Statements](https://learnsome.tech/learn/python-course/m13l01) | [7 labs](labs/m13l01/) | Pro |
| 13.2 | [If Else, And Conditional Expressions](https://learnsome.tech/learn/python-course/m13l02) | [10 labs](labs/m13l02/) | Pro |
| 13.3 | [If Elif Chains](https://learnsome.tech/learn/python-course/m13l03) | [5 labs](labs/m13l03/) | Pro |
| 13.4 | [Nesting Control Flow Statements](https://learnsome.tech/learn/python-course/m13l04) | [9 labs](labs/m13l04/) | Pro |
| 13.5 | [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) | [13 labs](labs/m13l05/) | Pro |
| 13.6 | [More String Methods](https://learnsome.tech/learn/python-course/m13l06) | [7 labs](labs/m13l06/) | Pro |
| 13.7 | [Loops And Tuples](https://learnsome.tech/learn/python-course/m13l07) | [12 labs](labs/m13l07/) | Pro |

### Module 14: While Loops

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 14.1 | [While Loops, And The General Range](https://learnsome.tech/learn/python-course/m14l01) | [8 labs](labs/m14l01/) | Pro |
| 14.2 | [Interactive While Loops](https://learnsome.tech/learn/python-course/m14l02) | [6 labs](labs/m14l02/) | Pro |
| 14.3 | [Graphical Applications With While](https://learnsome.tech/learn/python-course/m14l03) | [12 labs](labs/m14l03/) | Pro |
| 14.4 | [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) | [10 labs](labs/m14l04/) | Pro |
| 14.5 | [Chapter Three In One Sitting](https://learnsome.tech/learn/python-course/m14l05) | [10 labs](labs/m14l05/) | Pro |

### Module 15: Dynamic Web Pages

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 15.1 | [How A Web Page Reaches You](https://learnsome.tech/learn/python-course/m15l01) | [4 labs](labs/m15l01/) | Pro |
| 15.2 | [Composing Web Pages In Python](https://learnsome.tech/learn/python-course/m15l02) | [8 labs](labs/m15l02/) | Pro |
| 15.3 | [CGI: Dynamic Web Pages](https://learnsome.tech/learn/python-course/m15l03) | [9 labs](labs/m15l03/) | Pro |
| 15.4 | [HTML Forms And Dynamic Programs](https://learnsome.tech/learn/python-course/m15l04) | [7 labs](labs/m15l04/) | Pro |
| 15.5 | [Chapter Four In One Sitting](https://learnsome.tech/learn/python-course/m15l05) | [3 labs](labs/m15l05/) | Pro |

### Module 16: Reading Errors, And Platform Notes

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 16.1 | [Reading Error Messages](https://learnsome.tech/learn/python-course/m16l01) | [7 labs](labs/m16l01/) | Pro |
| 16.2 | [Windows And Mac Specifics](https://learnsome.tech/learn/python-course/m16l02) | [2 labs](labs/m16l02/) | Pro |

### Module 17: Errors, Exceptions And Debugging

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 17.1 | [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) | [9 labs](labs/m17l01/) | Pro |
| 17.2 | [Raising, And Writing Your Own Exception](https://learnsome.tech/learn/python-course/m17l02) | [6 labs](labs/m17l02/) | Pro |
| 17.3 | [Reading A Traceback Like A Professional](https://learnsome.tech/learn/python-course/m17l03) | [7 labs](labs/m17l03/) | Pro |
| 17.4 | [Debugging: print, breakpoint, and the debugger](https://learnsome.tech/learn/python-course/m17l04) | [6 labs](labs/m17l04/) | Pro |

### Module 18: Organising Code

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 18.1 | [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) | [8 labs](labs/m18l01/) | Pro |
| 18.2 | [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) | [8 labs](labs/m18l02/) | Pro |
| 18.3 | [Virtual Environments](https://learnsome.tech/learn/python-course/m18l03) | [6 labs](labs/m18l03/) | Pro |
| 18.4 | [pip, requirements, and installing packages](https://learnsome.tech/learn/python-course/m18l04) | [7 labs](labs/m18l04/) | Pro |

### Module 19: Data Structures In Depth

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 19.1 | [Lists, Tuples, Sets, Dicts: Choosing One](https://learnsome.tech/learn/python-course/m19l01) | [6 labs](labs/m19l01/) | Pro |
| 19.2 | [Comprehensions](https://learnsome.tech/learn/python-course/m19l02) | [7 labs](labs/m19l02/) | Pro |
| 19.3 | [Sorting, Keys And Lambdas](https://learnsome.tech/learn/python-course/m19l03) | [7 labs](labs/m19l03/) | Pro |
| 19.4 | [Iterators And Generators](https://learnsome.tech/learn/python-course/m19l04) | [7 labs](labs/m19l04/) | Pro |

### Module 20: Object Oriented Python

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 20.1 | [Classes And Instances](https://learnsome.tech/learn/python-course/m20l01) | [6 labs](labs/m20l01/) | Pro |
| 20.2 | [Methods, Attributes And self](https://learnsome.tech/learn/python-course/m20l02) | [7 labs](labs/m20l02/) | Pro |
| 20.3 | [Inheritance And Composition](https://learnsome.tech/learn/python-course/m20l03) | [7 labs](labs/m20l03/) | Pro |
| 20.4 | [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) | [8 labs](labs/m20l04/) | Pro |

### Module 21: Files, Formats And The Standard Library

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 21.1 | [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) | [8 labs](labs/m21l01/) | Pro |
| 21.2 | [JSON And CSV](https://learnsome.tech/learn/python-course/m21l02) | [5 labs](labs/m21l02/) | Pro |
| 21.3 | [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) | [8 labs](labs/m21l03/) | Pro |
| 21.4 | [A Standard Library Tour](https://learnsome.tech/learn/python-course/m21l04) | [6 labs](labs/m21l04/) | Pro |

### Module 22: Testing, Typing And Shipping

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 22.1 | [Testing With pytest](https://learnsome.tech/learn/python-course/m22l01) | [6 labs](labs/m22l01/) | Pro |
| 22.2 | [Type Hints](https://learnsome.tech/learn/python-course/m22l02) | [5 labs](labs/m22l02/) | Pro |
| 22.3 | [Formatting, Linting And Style](https://learnsome.tech/learn/python-course/m22l03) | [6 labs](labs/m22l03/) | Pro |
| 22.4 | [Shipping: scripts, entry points and git](https://learnsome.tech/learn/python-course/m22l04) | [7 labs](labs/m22l04/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech

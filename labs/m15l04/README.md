# m15l04 · HTML Forms And Dynamic Programs

Module 15: Dynamic Web Pages · lesson 15.4 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m15l04)

**Goal:** You can read and edit an HTML form, make its field names match the names your CGI script asks for, and recognise the text, submit, radio, checkbox and hidden input tags.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m15l04-07](m15l04-07/) | Where you could take this next | Read along |
| [m15l04-08](m15l04-08/) | The raw markup of a simple page | Read along |
| [m15l04-10](m15l04-10/) | An output template in raw markup | Read along |
| [m15l04-11](m15l04-11/) | Characters that need a substitute | Read along |
| [m15l04-12](m15l04-12/) | A form, in full | Read along |
| [m15l04-14](m15l04-14/) | Optional: radio buttons | Read along |
| [m15l04-15](m15l04-15/) | Optional: check boxes and a hidden field | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### QuotientWeb Form Exercise

1. Create a web form quotient.html that is intelligible to a user
2. Have it supply the data your quotient.cgi script needs
3. Test it on the local server, through the localhost address, not by clicking the file

> **Hint:** Every file must sit in the same directory as the server program you are running.

### Dynamic Web Programming Exercise

1. Make a complete dynamic presentation using at least three user inputs
2. Call the form dynamic.html, the script dynamic.cgi, the template dynamicTemplate.html
3. Start the server, then test it a few times through the localhost address

> **Hint:** The simplest version just adds three numbers instead of two.

## Check yourself

- Which attribute of a form decides where the data goes when the button is pressed?
- What has to be true of a field's name attribute and the call in your script?
- Why is it useful to point a new form's action at the dump script first?
- How do you read a group of check boxes, and why not with getfirst?
- What is a hidden input for, given that no user ever sees it?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)

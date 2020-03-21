# Readings: Week 12

We continue our discussion of object-oriented programming (OOP) and class
design by exploring class *inheritance*. Leveraging inheritance allows you
to write specialized versions of a class that inherit the attributes and
methods of the base or parent class (I'll use the terms *supertype* and
*subtype*). While inheriting the supertype's characteristics the subtype is
free to both add additional attributes and methods as well as *override*
supertype methods and attributes of the same name. We will explore this aspect
of class modeling but also discuss some of the hazards associated with an
over-reliance on inheritance. While discussing some of the dangers of designing
for inheritance, I'll introduce a second design pattern called *composition*,
one I implemented in last week's Jerk Pit menu exercise.

I also want to introduce a second topic of discussion.  Up to now we've worked exclusively with single Python modules (eg.,`lecture_17_solution.py`) that we
execute as a script from the command line or from within VS Code. These scripts
import, at most, 1-2 modules from the Python standard library
(e.g., `import csv`). However, we can also write our own custom modules and
import them into our script or program in order to access their functionality.
We will start exploring this form of code modularization in class this week.

## Class Inheritance; importing modules

**Eric Matthes, [Python Crash Course](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/), 2nd Edition (No Starch Press, 2019).**

Read Chapter 9 ["Classes"](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch09.xhtml#ch09).

Read sections:

* "Inheritance"
* "Importing Classes"

**Lisa Tagliaferri, ["Understanding Class Inheritance in Python 3"](https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3) (Digital Ocean, March 2018).**

Lisa's take on class inheritance.

**Lisa Tagliaferri, ["How To Import Modules in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3) (Digital Ocean, February 2017).**

A good read; short but covers the basics well.

## Optional

### Inheritance and Composition

**Isaac Rodriguez, ["Inheritance and Composition: A Python OOP Guide"](https://realpython.com/inheritance-composition-python) (RealPython, 7 Aug 2019).**

This is article illustrates the pitfalls of an overreliance on object
inheritance in software design. I include it for those who want to tackle a
challenging "long read" on inheritance and composition as it pertains to Python
programming. As the sub-heading above makes clear it is an *optional* reading.

### "Dunder" methods

**Bob Belderbos, ["Enriching your Python Classes with Dunder (Magical, Special) Methods"](https://dbader.org/blog/python-dunder-methods) (dbader.org, nd).**

Everything you ever wanted to know about double underscore methods. Another
*optional* reading. If you choose to peruse it, read, at a minimum, the following
sections:

* What are Dunder Methods?
* Special Methods and the Python Data Model
* Enriching a Simple Account Class _(note: excerpts)_
  * Object Initialization: `__init__`
  * Object Representation: `__str__`, `__repr__`

## Canvas Files

:exclamation: C. Severance, [Python for Everybody](https://www.py4e.com/book) EPUB and PDF versions are available in Canvas Files. Chuck's book has been translated into several languages and is available in various formats (i.e., HTML, PDF, EPUB, Mobi) at [https://www.py4e.com/book](https://www.py4e.com/book). All Tagliaferri articles are republished in L. Tagliaferri, [How to Code in Python 3](https://www.digitalocean.com/community/books/digitalocean-ebook-how-to-code-in-python) (Digital Ocean, Feb 2018). [PDF](https://do.co/python-book-pdf) and [EPUB](https://do.co/python-book-epub) versions are also available in Canvas Files.

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

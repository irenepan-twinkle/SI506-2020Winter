# Readings: Week 11

Over the next two weeks we will explore object-oriented programming (OOP) by way of the Python class. When you define a class, say `Person()`, you provide a blueprint, a template, or better yet, a model comprising attributes and methods that objects based on the class are provisioned with when created or instantiated (e.g. `ella = Musician('Ella', 'Fitzgerald', 'Vocalist')`).

Class design allows you to create multiple objects of the same type. As I've noted previously, you have been interacting with classes since week 3 of this course.

```
>>> ella = 'Ella Fitzgerald'
>>> type(ella)
<class 'str'>
>>> ella_names = ella.split() <-- method (behavior)
>>> ella_names
['Ella', 'Fitzgerald']
>>> louis = ['Louis', 'Armstrong']
>>> type(louis)
<class 'list'>
>>> john = ('John', 'Coltrane')
>>> type(john)
<class 'tuple'>
>>> miles = {'first_name': 'Miles', 'last_name': 'Davis'}
>>> type(miles)
<class 'dict'>
>>> first_name, last_name = miles.items() <-- method (behavior)
>>> first_name
('first_name', 'Miles')
>>> last_name
('last_name', 'Davis')
>>> type(first_name)
<class 'tuple'>
>>> type(last_name)
<class 'tuple'>
```

Now you get to write your own.

I have also included a short article on Python modules. This piece is a warmup foreshadowing future work involving writing code that you will import into another Python file as a module.

## Classes and Objects

**Eric Matthes, [Python Crash Course](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/), 2nd Edition (No Starch Press, 2019).**

Read Chapter 9 ["Classes"](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch09.xhtml#ch09).

Read sections:

* "Creating and Using a Class".
* "Working with Classes and Instances".

**Lisa Tagliaferri, ["How To Construct Classes and Define Objects in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3) (Digital Ocean, March 2017).**

**Lisa Tagliaferri, ["Understanding Class and Instance Variables in Python 3"](https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3) (Digital Ocean, March 2017).**

## Modules

**Lisa Tagliaferri, ["How To Create Modules in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3) (Digital Ocean, Feb 2017).**

## Canvas Files

:exclamation: C. Severance, [Python for Everybody](https://www.py4e.com/book) EPUB and PDF versions are available in Canvas Files. Chuck's book has been translated into several languages and is available in various formats (i.e., HTML, PDF, EPUB, Mobi) at [https://www.py4e.com/book](https://www.py4e.com/book). All Tagliaferri articles are republished in L. Tagliaferri, [How to Code in Python 3](https://www.digitalocean.com/community/books/digitalocean-ebook-how-to-code-in-python) (Digital Ocean, Feb 2018). [PDF](https://do.co/python-book-pdf) and [EPUB](https://do.co/python-book-epub) versions are also available in Canvas Files.

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

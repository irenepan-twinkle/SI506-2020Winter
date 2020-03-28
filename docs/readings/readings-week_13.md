# Readings: Week 13

This week you will learn how to connect over HTTP to a web application programming interface (API)
in order to retrieve resources (i.e., data) serialized as Javascript Object Notation (JSON), a
standard data interchange format. You will use `pip`, a Python package manager, to install the
`requests` module in order to simplify communicating with the [Star Wars API](https://swapi.co/)
endpoint. You will also learn how to use the `json` module to both read and write JSON documents.

## APIs

**Arnaud Lauret, [The Design of Web APIs](https://learning.oreilly.com/library/view/the-design-of/9781617295102/OEBPS/Text/c01.xhtml#h1-295102c01-0001) (Manning, 2019).**

Chapter 1 provides a high-level overview of the purpose of APIs with useful analogies. Read only the following sections and subsections:

* 1.1 What is an API?
  * 1.1.1 An API is a Web Interface for Software
  * 1.1.2 APIs turn Software into LEGO® Bricks
* 1.2 Why API Design matters
  * 1.2.1 A Public or Private API is an Interface for other Developers
  * 1.2.2 An API is made to hide the Implementation

## Pip Package Manager

**Isaac Rodriguez, ["What is Pip? A Guide for new Pythonistas"](https://realpython.com/what-is-pip/) (RealPython, April 2019).**

You will be installing your first Python package this week.  Isaac's article describes how to use `pip`, a package manager that comes bundled with Python 3.

## Requests Module

**Adam Snyder, ["Crash Course in HTTP Requests Using Python"](https://medium.com/better-programming/crash-course-in-http-requests-using-python-59246373a187) (Medium, May 2019).**

Quick read that covers the absolute basics of communicating with an API over HTTP in order to retrieve data.

**Alex Ronquillo, ["Python's Request Library (Guide)"](https://realpython.com/python-requests/) (RealPython, Jan 2019).**

Alex's article provides a solid overview of the requests module. Concentrate on the following sections and subsections:

* Getting started with requests
* The GET Request
* The Response
  * Status Code
* Query String Parameters

**Kenneth Reitz, Requests: [HTTP for Humans](https://requests.kennethreitz.org/en/master/). (A Kenneth Reitz Project).**

Official documentation for the Python [`requests`](https://pypi.org/project/requests/) module.  Review the ["Quickstart"](https://requests.kennethreitz.org/en/master/user/quickstart/) guide.  Familiarize yourself (minimally) with making requests, passing parameters in URLs, and JSON response content.

## Working with JSON

**Lindsey Basset, [Introduction to Javascript Object Notation](https://learning.oreilly.com/library/view/introduction-to-javascript/9781491929476/) (O'Reilly Media, Inc., 2015).**

Review the following chapters:

* Chapter 1 ["What is JSON"](https://learning.oreilly.com/library/view/introduction-to-javascript/9781491929476/ch01.html).
* Chapter 2 ["JSON Syntax"](https://learning.oreilly.com/library/view/introduction-to-javascript/9781491929476/ch02.html#chapter_jsonsyntax).
* Chapter 3 ["JSON Data Types"](https://learning.oreilly.com/library/view/introduction-to-javascript/9781491929476/ch03.html#chapter_jsondatatypes).

Chapter 1 is a quick read.  Chapters 2 and 3 describe how to craft JSON documents and the data types that can be expressed as values.

**Lucas Lofaro, ["Working with JSON data in Python"](https://realpython.com/python-json/) (RealPython, nd).**

Read Lucas's article on interacting with JSON data using the `json` and `requests` modules.

## The Star Wars API (SWAPI)

**The Star Wars API, ["Documentation"](https://swapi.co/documentation).**

Familiarize yourself with the resources that you can request from SWAPI. You will be working with
"SWAPI" JSON representations of Star Wars planets, people, species, starships, and vehicles from
now until the end of the semester.

## Optional

**Shif Ben Avraham, ["What is REST — A Simple Explanation for Beginners, Part 1: Introduction"](https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f)" (Medium, Sept 2017).**

**Shif Ben Avraham, ["What is REST — A Simple Explanation for Beginners, Part 2: REST Constraints"](https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-2-rest-constraints-129a4b69a582)" (Medium, Sept 2017).**

The terms Web API and REST API are often used interchangeably. However, not all Web APIs are REST APIs. A _RESTful_ API is an API whose design is influenced by a set of principles articulated by Roy Fielding. Shif outlines the style in two parts.

## Canvas Files

:exclamation: C. Severance, [Python for Everybody](https://www.py4e.com/book) EPUB and PDF versions are available in Canvas Files. Chuck's book has been translated into several languages and is available in various formats (i.e., HTML, PDF, EPUB, Mobi) at [https://www.py4e.com/book](https://www.py4e.com/book). All Tagliaferri articles are republished in L. Tagliaferri, [How to Code in Python 3](https://www.digitalocean.com/community/books/digitalocean-ebook-how-to-code-in-python) (Digital Ocean, Feb 2018). [PDF](https://do.co/python-book-pdf) and [EPUB](https://do.co/python-book-epub) versions are also available in Canvas Files.

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
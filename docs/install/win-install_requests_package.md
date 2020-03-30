# Windows 10: Using pip to install the requests package

`pip` is a Python package installer. `pip` provides a pain-free way of installing
community-developed Python packages that extend the Python standard library.

Since Python 3.4 `pip` comes bundled with the release so you will not
need to install it, although you may need to upgrade it if the version
installed on your machine is outdated.

## 1.0 Install the requests package

Follow the steps below to install the `requests` package.

### 1.1 Open Bash terminal

Click the start menu icon (lower left corner).  Type "Git" in the search
box. This should highlight the `Git Bash` app. Click the highlighted app
selection or the "Open" or "run as administrator" links to start the shell.

### 1.2 Check Python version

Not strictly necessary, but always a good practice.

```bash
$ python --version
Python 3.8.1
```

### 1.3 Check pip version

Enter the following command:

```bash
$ python -m pip --version

pip 20.0.2 from /usr/local/lib/python.7/site-packages/pip (python 3.7)
```

:bulb: The `-m` option instructs the Python interpreter to run the `pip` module as a script.

:warning: If you try to invoke `pip` directly you are liable to encounter the following warning:

```bash
$ pip --version

WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.

pip 20.0.2 from /usr/local/lib/python.7/site-packages/pip (python 3.7)
```

### 1.4 Update pip

If running a version of `pip` < 20.0.2 consider updating it:

```bash
$ python -m pip install -U pip
```

### 1.5 List installed packages

Check currently installed packages. The example output below is a minimal listing of installed packages. You may encounter more packages, indeed, significantly more packages, if you installed Python 3.x using Anaconda or have installed
Python packages previously.

```bash
$ python -m pip list

Package    Version
---------- -------
pip        20.0.2
setuptools 46.0.0
wheel      0.34.2
```

### 1.6 Install the requests package

Install the [requests](https://pypi.org/project/requests/) package.

```bash
$ python -m pip install requests

Collecting requests
  Downloading requests-2.23.0-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 1.3 MB/s
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 3.5 MB/s
Collecting certifi>=2017.4.17
  Downloading certifi-2019.11.28-py2.py3-none-any.whl (156 kB)
     |████████████████████████████████| 156 kB 19.2 MB/s
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Downloading urllib3-1.25.8-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 10.1 MB/s
Collecting idna<3,>=2.5
  Downloading idna-2.9-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 11.2 MB/s
Installing collected packages: chardet, certifi, urllib3, idna, requests
Successfully installed certifi-2019.11.28 chardet-3.0.4 idna-2.9 requests-2.23.0 urllib3-1.25.8
```

### 1.7 List installed packages (recheck)

As noted in the output above, five new packages were installed: `requests`
together with the required dependencies `chardet`, `certifi`, `urllib3`, and `idna`.

```bash
$ python -m pip list

Package    Version
---------- ----------
certifi    2019.11.28
chardet    3.0.4
idna       2.9
pip        20.0.2
requests   2.23.0
setuptools 46.0.0
urllib3    1.25.8
wheel      0.34.2
```

## 2.0 Confirm installation

Open VS Code or your source code editor or IDE of choice and create a file
called `scratch.py`. Write the following code and then run the file from
the command line (preferred, for practice) or from your source code editor
or IDE:

```python
import requests

# HTTP GET request to SWAPI service
# Chain requests.get() method to retrieve a specific person resource
# (i.e., /api/people/:id/) and requests.json() method to convert the
# response (a JSON document) to a dictionary.
response = requests.get('https://swapi.co/api/people/4/').json()

# Print response
print(f"{response}\n")

# Print person name
print(f"{response['name']}\n")
```

If you return the SWAPI representation of Darth Vader declare victory. If not,
ping Piazza for help.

```bash
$ python scratch.py

{'name': 'Darth Vader', 'height': '202', 'mass': '136', 'hair_color': 'none', 'skin_color': 'white', 'eye_color': 'yellow', 'birth_year': '41.9BBY', 'gender': 'male', 'homeworld': 'https://swapi.co/api/planets/1/', 'films': ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/6/', 'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/'], 'species': ['https://swapi.co/api/species/1/'], 'vehicles': [], 'starships': ['https://swapi.co/api/starships/13/'], 'created': '2014-12-10T15:18:20.704000Z', 'edited': '2014-12-20T21:17:50.313000Z', 'url': 'https://swapi.co/api/people/4/'}

Darth Vader
```

## 3.0 Other useful pip commands

### 3.1 Check for outdated packages

```bash
$ python -m pip list --outdated

Package    Version Latest Type
---------- ------- ------ -----
setuptools 46.0.0  46.1.3 wheel
```

### 3.2 Upgrade a package

```bash
$ python -m pip install --upgrade setuptools

Collecting setuptools
  Downloading setuptools-46.1.3-py3-none-any.whl (582 kB)
     |████████████████████████████████| 582 kB 1.6 MB/s
Installing collected packages: setuptools
  Attempting uninstall: setuptools
    Found existing installation: setuptools 46.0.0
    Uninstalling setuptools-46.0.0:
      Successfully uninstalled setuptools-46.0.0
Successfully installed setuptools-46.1.3
```

### 3.3 Delete a package

```bash
$ python -m pip uninstall requests

Found existing installation: requests 2.23.0
Uninstalling requests-2.23.0:
  Would remove:
    /Users/arwhyte/Development/python_playground/test_venv/venv/lib/python.7/site-packages/requests-2.23.0.dist-info/*
    /Users/arwhyte/Development/python_playground/test_venv/venv/lib/python.7/site-packages/requests/*
Proceed (y/n)? y
  Successfully uninstalled requests-2.23.0
```

## 4.0 Documentation

pip: [https://pip.pypa.io/en/stable/](https://pip.pypa.io/en/stable/)

requests: [https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)